import random
import turtle

import simpleaudio
import simpleaudio as sa
import time

screen = turtle.Screen()
screen.setup(1000,600)
screen.title("TOSBAĞAYI YAKALA!")
screen.bgcolor("light blue")
wave_obj = sa.WaveObject.from_wave_file("background.wav")

player_name = turtle.textinput("Merhaba!", "Tosbağayı Yakala oyununa hoş geldin!\n\nOyunun kuralları basit, senden kaçmaya çalışan tosbağaları tıklayarak yakalayacaksın!\nAma oyun zor, çünkü onlar çok hızlı kaçıyorlar (sıradan değiller!).\n30 tosbağayı yakalaman gerekiyor, bunun için 60 saniyen var.\n\nAdınızı girerek oyuna başlayabilirsiniz. Başarılar!")
if player_name == "":
    player_name = "KAHRAMAN"

game_over = False
FONT = ('Times New Roman', 20, 'normal')

turtle_list = []

count_down_turtle = turtle.Turtle()

score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    score_turtle.setposition(0, y)
    score_turtle.write(arg='YAKALANAN TOSBAĞA: 0', move=False, align='center', font=FONT)

grid_size = 10

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        if not game_over:
            global score
            score += + 1
            score_turtle.clear()
            beep_wave_obj = sa.WaveObject.from_wave_file("beep.wav")
            beep_play_obj = beep_wave_obj.play()
            score_turtle.write("YAKALANAN TOSBAĞA: {}".format(score), move=False, align="center", font=FONT)
            print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(Time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()

    if Time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("KALAN ZAMAN: {}".format(Time),move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(Time - 1), 1000)
    else:
        global player_name
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        if score>=30:
            clap_wave_obj = sa.WaveObject.from_wave_file("clap.wav")
            clap_play_obj = clap_wave_obj.play()
            count_down_turtle.write(f"OYUN BİTTİ! BAŞARDIN {player_name.upper()}! :)", align='center', font=FONT)
        else:
            sad_wave_obj = sa.WaveObject.from_wave_file("sad.wav")
            sad_play_obj = sad_wave_obj.play()
            count_down_turtle.write(f"OYUN BİTTİ! TEKRAR DENE {player_name.upper()}! :(", align='center', font=FONT)

        one_more_game()

def one_more_game():
    one_more_game_turtle = turtle.Turtle()
    one_more_game_turtle.shape("turtle")
    one_more_game_turtle.shapesize(2, 2)
    one_more_game_turtle.color("firebrick1")
    one_more_game_turtle.penup()
    one_more_game_turtle.setposition(0, 0)
    one_more_game_turtle.write("BİR OYUNA DAHA VAR MISIN?\n", align='center', font=FONT)

    def handle_click(x, y):
        one_more_game_turtle.hideturtle()
        one_more_game_turtle.clear()
        score_turtle.clear()
        start_game_up()

    one_more_game_turtle.onclick(handle_click)

def start_game_up(x=0,y=0):
    global game_over
    global player_name
    global score
    game_over = False
    score = 0
    simpleaudio.stop_all()
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(60), 10)
    play_obj = wave_obj.play()

start_game_up()

turtle.mainloop()