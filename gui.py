from tkinter import messagebox
from tkinter import *
from webbrowser import open as op
import os
import random
import pyttsx3
import wikipedia
from PIL import Image, ImageTk
from threading import Thread, Timer, main_thread
import speech_recognition as sr
import datetime
import socket
import time
import fileinput
from tkinter import filedialog



mdir=open("./music_dir.txt","r")
music_dir=mdir.readline()
mdir.close()

udir=open("./username.txt","r")
user_name=udir.readline()
udir.close()
# voice code for output starts
engine = pyttsx3.init(None)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Code to check internet
def Isconnect():
    print("Checking Internet.....")
    try:
        socket.create_connection(("www.google.com", 80))
        neticon.config(image=connlogo)
        nettext.config(text="Connected :)", fg="green")
        return True
    except OSError:
        pass
    neticon.config(image=notconn)
    nettext.config(text="No Internet ;( ", fg="red")
    return False

defcolor = "blue"
# Wise me code here
def wiseme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        update("Good Morning !!","green")
        speak("Good Morning!")
    elif 12 <= hour < 18:
        update("Good Afternoon !!","green")
        speak("Good Afternoon!")
    else:
        update("Good Evening !!","green")
        speak("Good Evening!")
    update("I am Jarvis. Your Personal Assistant!! ","yellow")
    speak("I am Jarvis!! your personal assistant!!.")
    update("How May I Help You !!","yellow")
    speak("Please Tell Me How may I help You !! ")


def update(message,color):
    msg.config(text=message,fg=color)


def commandReceiver():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        update("Listening....","green")

        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        update("Recognising....","orange")
        Isinternet = Isconnect()
        print(Isinternet)
        if (Isinternet):
            query = r.recognize_google(audio, language="en-IN")
        else:
            query = r.recognize_sphinx(audio, language="en-in")

        print("You Said", query)
        update(f"You Said: {query} ","green")
        time.sleep(1)


    except Exception as e:
        print(e)
        print("say that again please...")
        update("Say That Again Please !!","red")
        speak("say that again please...")
        return "None"

    return query


flag = 1
message = "OFF"
terminate = 0

session=1
def runnow():
    global session
    if session==1:
        wiseme()
        session=0
    
    
    count = 0
    
    while 1:
        if main_thread().is_alive():
            pass
        else:
            break
        if terminate == 1:
            break
        speak("Listening.....")
        query = commandReceiver().lower()
        speak(f"You Said :{query} ")
        if 'wikipedia' in query:
            update("Searching Wikipedia....","white")
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            update(results,defcolor)
            print(results)
            speak(results)
        elif 'search' in query:
            update("Searching In Google...",defcolor)
            speak('searching google')
            query = query.replace("google", "")
            query = query.replace("search", "")
            url = f"https://www.google.com/search?hl=%(en-in)s&q={query}"
            op(url)
            started()
            break
        elif 'music' in query:
            try:
                
                songs = os.listdir(music_dir)
                update("Playing a Random Music For You","pink")
                speak("Playing a random music for you!!")
                song = random.choice(songs)
                print(song) 
                update(f"Playing song : {song}","pink")
                os.startfile(os.path.join(music_dir,song))                
            except FileNotFoundError:
                speak(FileNotFoundError)
                update("Wrong Music Directory or directory not found","red")
                speak("It's Seems That, you have not specified the music directory")
                update("Please set the music directory first, from setting menu","yellow")
                speak("please set the music directory from setting")
                speak("opening setting..")
                Settingwindow()                
            finally:
                started()
                break            
                
            

        elif 'who are you' in query:
            update("I have already introduced myself in beginning.",defcolor)
            speak("I have already introduced myself in beginning. Just Kidding!!")
            update("I think you need to do your ear checkup.",defcolor)
            speak("I think you need to do your ear checkup.")
            update("Just Kidding!!",defcolor)
            speak("Just Kidding!!")
        elif 'chrome' in query:
            update("Starting Google Chrome..",defcolor)
            speak("starting google chrome")
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            started()
            break
        elif 'code' in query:
            update("Starting Visual Studio Code !!","red")
            speak("Starting visual studio code !!")
            os.startfile("C:\\Users\\Swaraj Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            started()
            break
        elif 'stop' in query:
            update("Thankyou for using my services. Bye!","black")

            speak("Thankyou for using my services. Bye !!")
            update("I Hate You !!","red")
            speak("I Hate you!")
            started()
            break
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            update(f"Sir  The Time Is {strTime}","red")
            speak(f"Sir the Time is {strTime}")

        elif 'change colour' in query:
            colorchange()

        else:
            if count == 3:
                update("Your Limit Has Crossed. Exiting Now","red")
                speak("You Are Out Of Limit!!")
                speak("Exiting Now")
                started()
                break
            update("Say That Again!!","red")
            speak("say it again!!")
            count = count + 1




def started():
    global terminate,flag
    if flag==1:
        l1.config(image=stop)
        
        try:
            t1 = Thread(target=runnow)
            t1.start()
            update("I am Jarvis!! .How May I help You","white")
            flag=0
            terminate=0
        except RuntimeError:
            update(RuntimeError,"red")
    else:
        update("Stoped","red")
        l1.config(image=play)
        flag = 1
        terminate = 1
        engine.stop()

def colorchange():

    color1="#dbff33"
    color2="#75ff33"
    color3="#33ffbd"
    color4="#33ff57"
    color5="#eef9bf"
    
    colors=[color1,color2,color3,color4,color5,"#a7e9af","#6a8caf","#fd5e53","#f9fcfb","#b0eacd","#21bf73","#be8abf","#ea9abb","#fea5ad","#f8c3af"]
    color=random.choice(colors)
    msgcolor=random.choices(colors)
    root.config(background=color)
    l1.config(background=color)
    neticon.config(background=color)
    nettext.config(background=color)
    logolab.config(background=color)
    msg.config(background=msgcolor)
    ccb.config(background=random.choice(colors),fg=msgcolor)

def helpwindow():
    helproot =Tk()
    # helproot.geometry("500x400")
    textarea=Text(helproot,height="30",width="80")
    textarea.pack(padx=20,pady=20)
    with open('./helpfile.txt','r') as target:
        textarea.insert(INSERT,target.read())

    textarea.config(state=DISABLED)
    helproot.mainloop()



def Settingwindow():
    global music_dir,dirlabel,uname
    Set=Tk()
    Set.bell()
    Set.iconbitmap("./icon.ico")
    Set.title("Jarvis Setting")
    Set.geometry("600x500")
    Label(Set,text="Your Name",font="bell 14 italic").place(x=30,y=50)
    uname=Entry(Set,font="bell 14 italic")
    uname.place(x=250,y=50)
    uname.insert(INSERT,user_name)
    Label(Set,text="Music Directory : ",font="bell 14 italic").place(x=30,y=100)
    dirlabel = Label(Set,text=music_dir,font="bell 12 italic",border=0,bg="white")
    dirlabel.place(x=250,y=100)
    Button(Set,text="Select Path",font="bell 10",command=getmusicdir).place(x=400,y=100)
    Button(Set,text="Submit",font="bell 15 bold",command=saveuserdata).place(x=260,y=400)

    Set.mainloop()

def saveuserdata():
    udir=open("./username.txt","w")
    udir.writelines(uname.get())
    udir.close()
    
    messagebox.showinfo(f"Welcome {uname.get()} ","Data Saved")
    

def getmusicdir():
    music_dir_path=filedialog.askdirectory()
    f=open("./music_dir.txt","w")
    f.write(music_dir_path)
    f.close()
    dirlabel.config(text=music_dir_path)





if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("./icon.ico")
    netlogo = Image.open("./defaulticon.png")
    netlogo = netlogo.resize((30, 30), Image.ANTIALIAS)
    netlogo = ImageTk.PhotoImage(netlogo)

    connlogo = Image.open("./connected.png")
    connlogo = connlogo.resize((30, 30), Image.ANTIALIAS)
    connlogo = ImageTk.PhotoImage(connlogo)

    notconn = Image.open("./notconnected.png")
    notconn = notconn.resize((30, 30), Image.ANTIALIAS)
    notconn = ImageTk.PhotoImage(notconn)

    logo = Image.open("./icon.ico")
    logo = logo.resize((60, 60), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    root.geometry("800x550")
    root.resizable(FALSE, FALSE)
    root.title("Jarvis")

    play = Image.open("./microphone.png")
    play = play.resize((100, 120), Image.ANTIALIAS)
    play = ImageTk.PhotoImage(play)
    stop = Image.open("./stop.png")
    stop = stop.resize((100, 100), Image.ANTIALIAS)
    stop = ImageTk.PhotoImage(stop)
    # menu code started......
    menu=Menu(root)
    root.config(menu=menu)
    submenu=Menu(menu,tearoff=False)
    menu.add_cascade(label="Options",menu=submenu)
    submenu.add_command(label="Setting",command=Settingwindow)
    submenu.add_command(label="About us")
    submenu.add_separator()
    submenu.add_command(label="Exit",command=exit)
    helpmenu=Menu(menu,tearoff=False,bg="white")
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="help",command=helpwindow)

    
    


    # menu code ends.......
    root.config(background="#dbff33")
    l1 = Button(root, image=play, bg="#dbff33", command=started, borderwidth=0)
    l1.place(x=350, y=300)
    msg = Label(root, text=message, height="2",width="50", font="bell 16 italic", bg="#123487", fg="Blue")
    msg.place(x=80, y=120)
    neticon = Label(root, image=netlogo, bg="#dbff33")
    neticon.place(x=620, y=10)
    nettext = Label(root, text="Checking...", bg="#dbff33", fg="Yellow", font="bell 10 bold")
    nettext.place(x=665, y=15)
    logolab=Label(root,image=logo,bg="#dbff33")
    logolab.place(x=20,y=10)
    Timer(1.0, Isconnect).start()
    ccb=Button(root,text="Change Color",font="comic 12 bold italic",bg="#75ff33",border=0.3,command=colorchange)
    ccb.place(x=350,y=500)
    




    # print(t1.is_alive())
    # def close():
    #     while main_thread().is_alive():
    #         if t1.is_alive():
    #             print("hello")
    #         else:
    #             print("i Am else")
    # Timer(3,close).start()
    root.mainloop()


