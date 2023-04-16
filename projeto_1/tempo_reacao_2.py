import graphics as gs
import random
import time
import keyboard
import statistics as st

circle_x = 0
circle_y = 0

cores = [['red', 'left'], ['blue', 'up'], ['yellow', 'right'], ['green', 'down']]
tentativas = 10
pontuacao = tentativas
tempos_de_reacao = []

win = gs.GraphWin("Tempo de Reação", 750, 500)

card = gs.Rectangle(gs.Point(647, 40), gs.Point(748, 175))
card.setFill(gs.color_rgb(200, 200, 200))
card.draw(win)

red_text = gs.Text(gs.Point(700, 60), "Bem-Vindo!\nRed: <-")
red_text.setTextColor("red")

blue_text = gs.Text(gs.Point(700, 90), "Blue: ^")
blue_text.setTextColor("blue")

yellow_text = gs.Text(gs.Point(700, 120), "Yellow: ->")
yellow_text.setTextColor("yellow")

green_text = gs.Text(gs.Point(700, 150), "Green: v")
green_text.setTextColor("green")

red_text.draw(win)
blue_text.draw(win)
yellow_text.draw(win)
green_text.draw(win)

message = gs.Text(gs.Point(350, 250), "Click anywhere to start the game!")
message.draw(win)
win.getMouse()
message.undraw()


def reiniciar_jogo():
    global pontuacao, tempos_de_reacao
    pontuacao = tentativas
    tempos_de_reacao = []
    main_loop()


def main_loop():
    global finish, pontuacao, tempos_de_reacao, tentativa_text

    tentativa_text = gs.Text(gs.Point(50, 10),
                        f"tentativa: 1")
    tentativa_text.draw(win)

    for i in range(tentativas):

        tentativa_text.undraw()
        tentativa_text = gs.Text(gs.Point(50, 10),
                            f"tentativa: {i+1}")
        tentativa_text.draw(win)

        circle_x = random.randint(50, 700)
        circle_y = random.randint(0, 450)

        p = gs.Point(circle_x, circle_y)

        radius_x = random.randint(20, 50)

        c = gs.Circle(p, radius_x)

        cor = random.choice(cores)

        fill = cor[0]

        c.setFill(fill)

        c.draw(win)

        inicio = time.time()

        while True:

            event = keyboard.read_event()

            if event.name == cor[1]:  # left
                final = time.time()
                tempo_reacao = round(final - inicio, 2)
                tempos_de_reacao.append(tempo_reacao)

                correct = gs.Text(gs.Point(350, 450),
                                  f"Resposta correta! \n Tempo de reacao: {tempo_reacao}s \n Pontuação: {pontuacao}")
                correct.draw(win)

                time.sleep(0.5)
                correct.undraw()

                break

            else:
                final = time.time()
                tempo_reacao = round(final - inicio, 2)
                tempos_de_reacao.append(tempo_reacao)
                pontuacao = pontuacao - 1

                wrong = gs.Text(gs.Point(350, 450),
                                f"Resposta errada! \n Tempo de reacao: {tempo_reacao}s \n Pontuação: {pontuacao}")
                wrong.draw(win)
                time.sleep(2)
                wrong.undraw()
                break

        c.undraw()

    tempo_reacao_mean = round(st.mean(tempos_de_reacao), 2)
    finish = gs.Text(gs.Point(350, 250), f"Game Over! \n Resultados: \n Pontuação: {pontuacao}/{tentativas} \n Tempo de reação médio: {tempo_reacao_mean}s")
    finish.draw(win)
    
main_loop()
# Adicione o botão de reset e o evento de clique do mouse

reset_button = gs.Rectangle(gs.Point(625, 410), gs.Point(750, 490))
reset_button.setFill("orange")
reset_button.draw(win)

reset_text = gs.Text(gs.Point(687.5, 450), "Reset")
reset_text.draw(win)

while True:
    click_point = win.getMouse()
    if 625 <= click_point.getX() <= 750 and 410 <= click_point.getY() <= 490:
        finish.undraw()
        reset_text.undraw()
        reset_button.undraw()
        tentativa_text.undraw()
        reiniciar_jogo()

