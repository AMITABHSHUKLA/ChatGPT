from tkinter import *
import wolframalpha
import wikipedia
from tkinter import messagebox
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("jarvis")
training = ChatterBotCorpusTrainer(chatbot)
training.train("chatterbot.corpus.english")
#main function
def jarvis():
    #store the input in query variable
    global answer
    query = query_input.get()
    print(query)
    try:
        #it will try wolframalpha
        app_id = "T5VEJ9-KXP684Q2A4"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        
    except:
        #wikipedia we can write whole summary but it will be hard to read.
        #we are displaying summary upto 5 sentence only
        answer =  wikipedia.summary(query,sentences = 5) 
    
    else:
        
        answer= chatbot.get_response(query)
        
    l1["text"] = answer
     
    return answer


root = Tk()
root.geometry("600x500")
root.config(bg="Grey")
root.title("CHATGPT")
root_label = Label(root, text = "CHATGPT",bg="BLACK",fg = "white",
                   padx=10,pady=10,borderwidth=7,
                   relief = RAISED,font='Helvetica 10 bold')
root_label.pack()
f1 = LabelFrame(root,bg= "white")
f1.pack()
l1 = Label(f1,bg="grey",fg = "black",font= "Helvetica 10 bold",wraplength= 900)
l1.pack()
#takes input
query_input = Entry(root,width=100)
query_input.pack(ipady=6,pady=(1,15),side = BOTTOM)
btn = Button(root,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,
             command = jarvis)
btn.place(x=100,y=0)
btn.pack(side = BOTTOM)
root.mainloop()
