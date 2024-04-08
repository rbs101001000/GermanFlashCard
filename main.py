from tkinter import *
from tkinter import messagebox
import pandas as pd
import random


#--------------CSV---------------
csv_file_path = "./csv/source.csv"
data = pd.read_csv(csv_file_path)

status = {
    "german":"",
    "english":"",
    "correct":0,
    "wrong":0,
    "skipped":0,
    "state":0
}

words = []
wordsFrame = pd.DataFrame.from_dict(words)

current_word = {
    "german word":"",
    "english meaning":""
    }

difficulty = 0

cheat_questions = ["Is Saber the most handsome guy in the world", "Is Saber the most smart guy that the world have ever seen?", "Is Saber the most talented programmer in the world?", "Is Farah the best sister?", "Is Saber the best Mama Jan for Falakee, Mahsaee, and Duaee?", "Does everyone love Saber very much?"]

#-----------------functions--------------------
    
def next_card():
    global data,current_word
    
    if status["state"]>=20:
        result()
    
    data_dict = data.to_dict(orient="records")
    random_row = random.choice(data_dict)
    random_german_word = random_row["German"]
    random_german_word_english_meaning = random_row["English"]
    canvas.itemconfig(word, text=random_german_word)
    current_word["german word"]=random_german_word
    current_word["english meaning"]=random_german_word_english_meaning
    score["text"]=f"{status['state']}/20"

    button_shuffle()
    row = f"{random_german_word} | {random_german_word_english_meaning}"+"\n"
    words.append(row)
    
    
    
def button_shuffle():
    global buttons_list,data,current_word
    data_dict = data.to_dict(orient="records")
    for i in buttons_list:
        random_row = random.choice(data_dict)
        i["text"]=random_row["English"]
    answer = current_word["english meaning"]
    answer_button = random.choice(buttons_list)
    answer_button["text"]=answer

    

def check_answer(button):
    
    chossen_answer = button.cget("text")
    if chossen_answer  == current_word["english meaning"]:
        status["correct"]+=1
    else:
        status["wrong" ]+=1
        
    
        
        
    status["state"]+=1
    next_card()
    
def skip():
    if status["state"]>=20:
        result()
    status["skipped"]+=1
    status["state"]+=1
    next_card()
    

def start():
    button_start.config(state="disable")
    button_light.config(state="normal")
    button_reset.config(state="normal")
    button_next.config(state="normal")
    button_a.config(state="normal")
    button_b.config(state="normal")
    button_c.config(state="normal")
    button_d.config(state="normal")
    
    next_card()
    
    
def restart():
    start()
    words.clear()
    status["correct"]=0
    status["skipped"]=0
    status["state"]=0
    status["wrong"]=0
    score.config(text=f"{status['state']}/20")
    next_card()
    
def light():
    global cheat_questions
    cheat = messagebox.askyesno(title="cheat!",message=random.choice(cheat_questions))
    if cheat:
        messagebox.showinfo(title="Answer",message=f"😎 \nGood job! \nI knew you're smart, here is the answer: \n{current_word['german word']} = {current_word['english meaning']}")
        
    else:
        lose = False
        while not lose:
            lose = messagebox.askyesno(title="😒",message="You probably gonna lose.")
        
        
def result():
    global words
    messagebox.showinfo(title="Result",message=f"score: {status['correct']}/20 \nskipped: {status['skipped']} \nwrong: {status['wrong']}")
    
    end()
    
def save_result():
    pass
    
    
def end():
    button_start.config(state="disable")
    button_light.config(state="disable")
    button_reset.config(state="normal")
    button_next.config(state="disable")
    button_a.config(state="disable")
    button_b.config(state="disable")
    button_c.config(state="disable")
    button_d.config(state="disable")
    

#--------------------layout------------------
window = Tk()
window.minsize(width=800,height=500)
window.maxsize(width=800,height=500)
window.config(padx=50,pady=50,bg="white",background= "white")

# card_photo2 = PhotoImage("./images/back_card.png")
card_photo = PhotoImage(file="./images/front_card.png")
# option_img = PhotoImage(file="./images/option_square.png",height=100,width=100)
reset_img = PhotoImage(file="./images/reset.png",height=50,width=50)
next_image = PhotoImage(file="./images/nextImage.png")
light_image = PhotoImage(file="./images/light1.png")
start_image = PhotoImage(file="./images/start.png")

score = Label(text=f"{status['state']}/20",fg="#638889",font=("Courier",20))
canvas = Canvas(width=700,height=250,bg="white",highlightthickness=0)
front_card=canvas.create_image(350,125,image=card_photo)
# back_card=canvas.create_image(350,125,image=card_photo2)

title = canvas.create_text(350,80,text="German",font=("arial",20,"italic"))
word = canvas.create_text(350,150,text="word",font=("arial",40,"bold"))

button_a = Button(state="disabled",text="a",padx=20,font=("arial",20,"normal"),bg="#9DBC98", command=lambda: check_answer(button_a))
button_b = Button(state="disabled",text="b",padx=20,font=("arial",20,"normal"),bg="#9DBC98", command=lambda: check_answer(button_b))
button_c = Button(state="disabled",text="c",padx=20,font=("arial",20,"normal"),bg="#9DBC98", command=lambda: check_answer(button_c))
button_d = Button(state="disabled",text="d",padx=20,font=("arial",20,"normal"),bg="#9DBC98", command=lambda: check_answer(button_d))

buttons_list = [button_a,button_b,button_c,button_d]
button_reset = Button(state="disabled",image=reset_img,command=restart)
button_next = Button(state="disabled",image=next_image,command=skip)
button_light = Button(state="disabled",image=light_image,command=light)
button_start = Button(state="active",image=start_image,command=start)

#-------------------position-----------------------
score.place(x=600)
button_reset.place(x=0)
button_next.place(x=650,y=150)
button_light.place(x=0,y=150)
button_start.place(x=340)

canvas.grid(row=1,column=0,columnspan=4,pady=40)
button_a.grid(row=2,column=0)
button_b.grid(row=2,column=1)
button_c.grid(row=2,column=2)
button_d.grid(row=2,column=3)

window.mainloop()

# knika kapoor 
# mohammad irfan