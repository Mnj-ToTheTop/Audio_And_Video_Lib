import mysql.connector as mod
from tkinter import *
import vlc
from functools import partial
import base64

#Creating connection to SQL database 
connect_001 = mod.connect(host = "localhost", user = "MnjRaj", passwd = "LeoValdez#7", database = "project")
cursor_audio = connect_001.cursor()
cursor_base = connect_001.cursor()
cursor_video = connect_001.cursor()
cursor_request = connect_001.cursor()
cursor_requested = connect_001.cursor()
cursor_cust = connect_001.cursor()
cursor_emp = connect_001.cursor()
cursor_reg = connect_001.cursor()
cursor_reg1 = connect_001.cursor()

cursor_base.execute("SET GLOBAL max_allowed_packet=1073741824;")

#Creating customer actions
def cust():    
    def videoPlayer(p):
        video = Tk(className = "player")
        video.geometry("400x150")
        cursor = connect_001.cursor()
        
        cursor.execute("select file from video where name = '" + p[0] + "';")
        data_list = cursor.fetchall()
        
        data = data_list[0][0]
        binary_data = base64.b64decode(data)
        
        l = open("Video.mp4", 'wb')
        l.write(binary_data)
        l.close()

        def media_player_exit():
            media_player.stop()
            video.destroy()
        
        media_player = vlc.MediaPlayer("Video.mp4")
        play = Button(video, text = "Play", command = media_player.play, font = "Georgia", width = 15).pack()
        pause = Button(video, text = "Pause and Play", command = media_player.pause, font = "Georgia", width = 15).pack()
        stop = Button(video,text = "Stop", command = media_player_exit, font = "Georgia", width = 15).pack()
        video.mainloop()


    def audioPlayer(x):
        audio = Tk(className = "player")
        audio.geometry("400x150")
        cursor = connect_001.cursor()
        
        cursor.execute("select file from audio where name = '" + x[0] + "';")
        data_list = cursor.fetchall()
        
        data = data_list[0][0]
        
        binary_data = base64.b64decode(data)
        
        file = open("Audio.mp3", "wb")
        file.write(binary_data)
        file.close()

        def media_player_exit():
            media_player.stop()
            audio.destroy()
        
        media_player = vlc.MediaPlayer("Audio.mp3")
        play = Button(audio, text = "Play", command = media_player.play, font = "Georgia", width = 15).pack()
        pause = Button(audio, text = "Pause and Play", command = media_player.pause, font = "Georgia", width = 15).pack()
        stop = Button(audio,text = "Stop", command = media_player_exit, font = "Georgia", width = 15).pack()
        audio.mainloop()
                               
    def audio():
        audio = Tk(className = 'Available Audios')
        audio.geometry("400x300")
        cursor_audio.execute("Select name from audio")
        audio_data = cursor_audio.fetchall()
        for k in audio_data:
            Button(audio, text = k[0], command = partial(audioPlayer, k), font = "Georgia", width = 20).pack()
        
    
    def video():
        video = Tk(className = 'Avaliable Videos')
        cursor_video.execute("select name from video")
        video_data = cursor_video.fetchall()
        for v in video_data:
            Button(video, text = v[0], command = partial(videoPlayer,v), font = "Georgia", width = 25).pack()

    def request():
        request = Tk()
        request.geometry("400x200")
        frame = Frame(request)
        frame.pack()
        down = Frame(request)
        down.pack()
        def submit():
            name = name_ent.get()
            media = media_ent.get()
            cursor_request.execute("insert into requested values( '"+nm+"','"+name+"','"+media+"');")
            connect_001.commit()
            Label(request, text = "Your request has been submitted.").pack()
        Label(frame, text = "Title", font = "Georgia", width = 10).pack(side = LEFT)
        name_ent = Entry(frame, width = 20)
        name_ent.pack(side = RIGHT)
        Label(down, text = "Media", font = "Georgia", width = 10).pack(side = LEFT)
        media_ent = Entry(down, width = 20)
        media_ent.pack(side = RIGHT)
        btn = Button(request, text = "SUBMIT", command = submit, font = "Georgia", width = 7).pack()
        request.mainloop()


        
    def coreofcrust():        
        win = Tk(className = "E-Library")
        win.geometry("400x300")
        head = Label(win, text = 'Welcome to E-library,\n '+ nm , font = "Broadway", width = 20).pack()
        Button(win, text = 'Available video', command = video, font = "Georgia", width = 15).pack()
        Button(win, text = 'Available audio', command = audio, font = "Georgia", width = 15).pack()
        Button(win, text = 'Request content', command = request, font = "Georgia", width = 15).pack()
        win.mainloop()


    def registry():
        reg = Tk()
        reg.geometry("400x200")
        frame = Frame(reg)
        frame.pack()
        mid = Frame(reg)
        mid.pack()
        down = Frame(reg)
        down.pack()
        
        def submit():
            name = name_ent.get()
            user_id = user_id_ent.get()
            pass_word = pass_word_ent.get()
            cursor_reg1.execute("select * from customer;")
            pro = cursor_reg1.fetchall()
            K = []
            for i in pro:
                K.append(i[1])
            if user_id in K:
                Label(reg, text ="User Id Taken!", font = "Georgia").pack()
            else:
                cursor_reg.execute("insert into customer values( '"+name+"','"+user_id+"','"+pass_word+"');")
                Label(reg, text = "Registered. Pls Login using your credentials").pack()
                connect_001.commit()
                
        Label(frame, text = "Name", font = "Georgia", width = 10).pack(side = LEFT)
        name_ent = Entry(frame, width = 20)
        name_ent.pack(side = RIGHT)
        Label(mid, text = "User Id", font = "Georgia", width = 10).pack(side = LEFT)
        user_id_ent = Entry(mid, width = 20)
        user_id_ent.pack(side = RIGHT)
        Label(down, text = "Password", font = "Georgia", width = 10).pack(side = LEFT)
        pass_word_ent = Entry(down)
        pass_word_ent.pack(side = RIGHT)
        btn = Button(reg, text = "SUBMIT", command = submit, font = "Georgia", width = 7).pack()
        reg.mainloop()



    cat = Tk(className = "Customer page")
    Label(cat, text = "Customer Login", font = "Georgia").pack()
    cat.geometry("400x300")
    frame = Frame(cat)
    frame.pack()
    down = Frame(cat)
    down.pack()
    def submit():
        user_id = user_id_ent.get()
        paswrd = paswrd_ent.get()
        M = []
        cursor_cust.execute("select * from customer;")
        value = cursor_cust.fetchall()
        for i in value:
            M.append(i[1])
        if user_id not in M:
            Label(cat, text = "Incorrect User ID").pack()
        else:
            for k in value:
                if k[1] == user_id:
                    if k[2] == paswrd:
                        cat.destroy()
                        global nm
                        nm = k[0]
                        coreofcrust()
                    else:
                        Label(cat, text = "Incorrect Password").pack()           
    Label(frame, text = "User ID", font = "Georgia", width = 10).pack(side = LEFT)
    user_id_ent = Entry(frame, width = 20)
    user_id_ent.pack(side = RIGHT)
    Label(down, text = "Password", font = "Georgia", width = 10).pack(side = LEFT)
    paswrd_ent = Entry(down, width = 20)
    paswrd_ent.pack(side = RIGHT)
    btn = Button(cat, text = "SUBMIT", command = submit, font = "Georgia", width = 7).pack()
    Button(cat, text = "New User? Register here", command = registry).pack()
    cat.mainloop()


#Creating Employee side
def emp():

    def update():
        pup = Tk()
        pup.geometry("400x400")
        frame = Frame(pup)
        frame.pack()
        down = Frame(pup)
        down.pack()
        last = Frame(pup)
        last.pack()
        def submit():
            Title = title_new_ent.get()
            loco = loc_ent.get()
            typee = type_ent.get()
            try:
                if typee == ".mp3" or typee == ".MP3":
                    curs_ins_aud = connect_001.cursor()
                    curs_out_aud = connect_001.cursor()
                    file = open(loco ,'rb').read()
                    data = base64.b64encode(file)
                    args = (Title, data)
                    query = 'INSERT INTO audio VALUES(%s, %s)'
                    curs_ins_aud.execute(query, args)
                    curs_out_aud.execute('DELETE FROM REQUESTED WHERE Name = "' + Title + '";')
                    connect_001.commit()
                    Label(pup, text = "Success").pack()
                elif typee == ".mp4" or typee == ".MP4":
                    curs_ins_vid = connect_001.cursor()
                    curs_out_vid = connect_001.cursor()
                    file = open(loco ,'rb').read()
                    data = base64.b64encode(file)
                    args = (Title, data)
                    query = 'INSERT INTO video VALUES(%s, %s)'
                    curs_ins_vid.execute(query,args)
                    curs_out_vid.execute('DELETE FROM REQUESTED WHERE Name = "' + Title + '";')
                    connect_001.commit()
                    Label(pup, text = "Success").pack()
                else:
                    Label(pup, text = "Enter a proper file type").pack()
            except FileNotFoundError:
                Label(pup, text = "File Not Found").pack()
        Label(frame, text = "Ttile", font = "Georgia", width = 10).pack(side = LEFT)
        title_new_ent = Entry(frame, width = 20)
        title_new_ent.pack(side = RIGHT)
        Label(down, text = "Location", font = "Georgia", width = 10).pack(side = LEFT)
        loc_ent = Entry(down, width = 20)
        loc_ent.pack(side = RIGHT)
        Label(last, text = "Type", font = "Georgia", width = 10).pack(side = LEFT)
        type_ent = Entry(last, width = 20)
        type_ent.pack(side = RIGHT)
        Button(pup, text = "Submit", command = partial(submit), font = "Georgia").pack()
      
    def requested():
        requested = Tk(className = "Requested Content")
        requested.geometry("600x500")
        cursor_requested.execute("select * from requested")
        requested_data = cursor_requested.fetchall()
        Label(requested, text = "Customer Name, Title - Media Type", font = "Georgia").pack()
        for m in requested_data:
            Label(requested, text = m[0] + ","+ m[1] + "-" + m[2], font = "Georgia").pack()
    def core():
        cat.destroy()
        win = Tk(className = "E-Library")
        win.geometry("400x300")
        head = Label(win, text = 'Welcome to E-library,\n'+ op, font = "Broadway", width = 20).pack()
        Button(win, text = 'Requested content', command = requested, font = "Georgia", width = 15).pack()
        Button(win, text = 'Update library', command = partial(update), font = "Georgia", width = 15).pack()
        win.mainloop()

        
    cat = Tk(className = "Emp login page")
    Label(cat, text = "Employee Login", font ="Georgia").pack()
    cat.geometry("400x200")
    frame = Frame(cat)
    frame.pack()
    down = Frame(cat)
    down.pack()
    def submit():
        emp_id = emp_id_ent.get()
        paswrd = paswrd_ent.get()
        M = []
        cursor_emp.execute("select * from employee;")
        value = cursor_emp.fetchall()
        for i in value:
            M.append(i[1])
        if emp_id not in M:
            Label(cat, text = "Incorrect Emp ID").pack()
        else:
            for k in value:
                if k[1] == emp_id:
                    if k[2] == paswrd:
                        global op
                        op = k[0]
                        core()
                    else:
                        Label(cat, text = "Incorrect Password").pack()
        
       
            
    Label(frame, text = "Emp ID", font = "Georgia", width = 10).pack(side = LEFT)
    emp_id_ent = Entry(frame, width = 20)
    emp_id_ent.pack(side = RIGHT)
    Label(down, text = "Password", font = "Georgia", width = 10).pack(side = LEFT)
    paswrd_ent = Entry(down, width = 20)
    paswrd_ent.pack(side = RIGHT)
    btn = Button(cat, text = "SUBMIT", command = submit, font = "Georgia", width = 7).pack()
    cat.mainloop()


dog = Tk(className = "page")
dog.geometry("200x100")
Button(dog, text = "Customer", font = "Georgia", command = partial(cust)).pack()
Button(dog, text = "Employee", font = "Georgia", command = partial(emp)).pack()
dog.mainloop()
