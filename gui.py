#Importing libraries for creating a GUI interface

import tkinter as tk
from tkinter import messagebox
from backend import shuffle_word, guess_correct, get_word_random

#Creating a class for Guess The Word Game for GUI Building

class GuessTheWord:

    #Function for initializing the Window
    def __init__ (self, master):
        self.master = master
        self.master.title("Guess the Word Game")
        self.master.geometry("500x400")
        self.master.config(bg="#3C3D37") #The background color of the window

        ##GUI Elements that are used 

        self.title_label = tk.Label(
            master, text="Guess the Word!", font=("Verdana", 26, "bold"), bg="#ECDFCC", fg="#181C14"
        )
        self.title_label.pack(padx=15, pady= 15)

        self.word_label = tk.Label(
            master, text="", font=("Verdana", 24, "bold"), bg="#ECDFCC", fg="#3C3D37"
        )
        self.word_label.pack(padx=20, pady=20)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            master, textvariable=self.entry_var, font=("Verdana", 20),
            bg="#ECDFCC", fg="#697565", justify="center"
        )
        self.entry.pack(padx=25, pady=25)

        self.check_button = tk.Button(
            master, text="Check", command=self.check_guess, font=("Verdana", 16),
            bg="#3C3D37", fg="#ECDFCC"
        )
        self.check_button.pack(padx=25, pady=25)

        self.new_game_button = tk.Button(
            master, text="New Game", command=self.new_game, font=("Verdana", 16),
            bg="#3C3D37", fg="#ECDFCC"
        )
        self.new_game_button.pack(padx=5, pady=5) 

        #starting the first game
        self.new_game()

    #Function to launch new game round
    def new_game(self):
        self.select_word = get_word_random()
        shuffled = shuffle_word(self.select_word)
        self.word_label.config(text=shuffled)
        self.entry_var.set("") #This will clear the input field
    
    #Function that checks if the guess is correct or not

    def check_guess(self):
        guess = self.entry_var.get()
        if guess_correct(guess, self.select_word):
            messagebox.showinfo("Congratulations!", "You guessed it right!")
            self.new_game()
        else:
            messagebox.showerror("Incorrect!", "Try again!")
    
#Creating the tkinter window and running the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheWord(root)
    root.mainloop()
