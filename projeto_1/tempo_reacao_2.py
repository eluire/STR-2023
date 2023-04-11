import graphics as gs
import random
import time
import keyboard
import statistics as st




circle_x=0
circle_y=0


cores = [['red', 'left'], ['blue', 'up'], ['yellow', 'right'], ['green', 'down']]
tentativas = 3
pontuacao = tentativas
tempos_de_reacao = []

win = gs.GraphWin("Tempo de Reação", 750,500)
message = gs.Text(gs.Point(350,250),"Click anywhere to start the game!")
message.draw(win)
win.getMouse()
message.undraw()

for i in range(tentativas):
    
    circle_x = random.randint(50,700)
    circle_y = random.randint(0,450)

    p = gs.Point(circle_x,circle_y)

    radius_x = random.randint(20,50)

    c = gs.Circle(p,radius_x)

    cor = random.choice(cores)

    fill = cor[0]

    c.setFill(fill)

    c.draw(win)

    inicio = time.time()

    while True:

        event = keyboard.read_event()

        if event.name == cor[1]:
            final = time.time()
            tempo_reacao = round(final - inicio, 2)
            tempos_de_reacao.append(tempo_reacao)

            correct = gs.Text(gs.Point(350, 450), f"Resposta correta! \n Tempo de reacao: {tempo_reacao}s \n Pontuação: {pontuacao}")
            correct.draw(win)

            time.sleep(2)
            correct.undraw()

            break

        else:
            final = time.time()
            tempo_reacao = round(final - inicio, 2)
            tempos_de_reacao.append(tempo_reacao)
            pontuacao = pontuacao - 1

            wrong =  gs.Text(gs.Point(350, 450), f"Resposta errada! \n Tempo de reacao: {tempo_reacao}s \n Pontuação: {pontuacao}")
            wrong.draw(win)
            time.sleep(2)
            wrong.undraw()
            break

    c.undraw()

    

tempo_reacao_mean = round(st.mean(tempos_de_reacao), 2)
finish = gs.Text(gs.Point(350, 250), f"Game Over! \n Resultados: \n Pontuação: {pontuacao} \n Tempo de reação médio: {tempo_reacao_mean}s")
finish.draw(win)

win.getMouse()

