from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
from words import word_list

def main():
    window = Tk()
    window.title("Hangman")
    window.resizable(False, False)

    photos = [
        (PhotoImage(file="images/hang0.png")), (PhotoImage(file="images/hang1.png")),
        (PhotoImage(file="images/hang2.png")), (PhotoImage(file="images/hang3.png")),
        (PhotoImage(file="images/hang4.png")), (PhotoImage(file="images/hang5.png")),
        (PhotoImage(file="images/hang6.png")), (PhotoImage(file="images/hang7.png")),
        (PhotoImage(file="images/hang8.png")), (PhotoImage(file="images/hang9.png")),
        (PhotoImage(file="images/hang10.png")), (PhotoImage(file="images/hang11.png"))
    ]

    def newGame():
        global answer_spaces
        global answer
        global num_guesses
        num_guesses = 0
        imgLabel.config(image=photos[0])
        answer = random.choice(word_list)
        answer_spaces = " ".join(answer)
        lblWord.set(" ".join("_"*len(answer)))

    def guess(letter):
        global num_guesses
        if num_guesses<11:
            txt = list(answer_spaces)
            guessed = list(lblWord.get())
            if answer_spaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                    lblWord.set("".join(guessed))
                    if lblWord.get() == answer_spaces:
                        messagebox.showinfo("Hangman", "You guessed correctly!")
            else:
                num_guesses += 1
                imgLabel.config(image=photos[num_guesses])
                if num_guesses == 11:
                    messagebox.showinfo("Hangman", f"Game Over :( \n The correct word was {answer}")


    imgLabel = Label(window)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    imgLabel.config(image=photos[0])

    lblWord = StringVar()
    Label(window, textvariable=lblWord, font=("Helvetica 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

    n = 0
    for lett in ascii_uppercase:
        Button(window, text=lett, command=lambda lett=lett: guess(lett), font=("Helvetica 18"), width=4).grid(row=1+n//9, column=n%9)
        n +=1


    Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

    newGame()
    window.mainloop()

if __name__ == "__main__":
    main()