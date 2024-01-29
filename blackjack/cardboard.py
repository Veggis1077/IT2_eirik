from tkinter import *

root = Tk()
root.title('BLACKJACK - Vegard "Josef K." R. R.')
root.geometry("900x500")
root.configure(background="green")

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=0, padx=20, ipadx=20)




root.mainloop()