import tkinter as tk
import random
import time
import statistics as st


class ReactionTimeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tempo de Reação")
        self.master.geometry("750x500")

        self.colors = [['red', 'Left'], ['blue', 'Up'], ['yellow', 'Right'], ['green', 'Down']]
        self.max_attempts = 10
        self.score = self.max_attempts
        self.reaction_times = []

        self.card = tk.Canvas(self.master, bg="white", width=100, height=135)
        self.card.place(x=647, y=40)

        self.red_text = tk.Label(self.master, text="Bem-Vindo!\nRed: <-", fg="red")
        self.red_text.place(x=700, y=60)

        self.blue_text = tk.Label(self.master, text="Blue: ^", fg="blue")
        self.blue_text.place(x=700, y=90)

        self.yellow_text = tk.Label(self.master, text="Yellow: ->", fg="yellow")
        self.yellow_text.place(x=700, y=120)

        self.green_text = tk.Label(self.master, text="Green: v", fg="green")
        self.green_text.place(x=700, y=150)

        self.message = tk.Label(self.master, text="Click anywhere to start the game!")
        self.message.place(x=350, y=250)

        self.master.bind("<Button-1>", self.start_game)

    def start_game(self, event):
        self.message.destroy()
        for i in range(self.max_attempts):
            circle_x = random.randint(50, 700)
            circle_y = random.randint(0, 450)
            radius_x = random.randint(20, 50)

            self.circle = self.card.create_oval(circle_x - radius_x, circle_y - radius_x, circle_x + radius_x, circle_y + radius_x)

            color = random.choice(self.colors)
            self.card.itemconfig(self.circle, fill=color[0])

            self.start_time = time.time()

            self.master.bind(f"<{color[1]}>", self.check_reaction_time)
            self.master.wait_variable(self.key_pressed)

            if self.key_pressed.get():
                self.key_pressed.set(0)
                self.stop_game(True)
                break
            else:
                self.stop_game(False)

    def check_reaction_time(self, event):
        self.stop_time = time.time()
        reaction_time = round(self.stop_time - self.start_time, 2)
        self.reaction_times.append(reaction_time)

        self.master.unbind(event.keysym)
        self.key_pressed.set(1)

    def stop_game(self, correct):
        self.card.delete(self.circle)

        if correct:
            self.score -= 1
            text = f"Resposta correta! \n Tempo de reacao: {self.reaction_times[-1]}s \n Pontuação: {self.score}"
        else:
            text = f"Resposta errada! \n Tempo de reacao: {self.reaction_times[-1]}s \n Pontuação: {self.score}"
        
        self.result = tk.Label(self.master, text=text)
        self.result.place(x=350, y=450)

        time.sleep(0.5)
        self.result.destroy()

        if self.score == 0 or len(self.reaction_times) == self.max_attempts:
            self.finish_game()

    def finish_game(self):
        mean_reaction_time = round(st.mean(self.reaction_times), 2)

def main():
    root = tk.Tk()
    game = ReactionTimeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
