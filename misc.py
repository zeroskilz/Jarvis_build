#!/usr/local/bin/python
import os
import random
import speech_recognition as sr
r = sr.Recognizer()							
m = sr.Microphone()
#set the Threshold to 4000 lowing microphone sensitivity..........................................................
r.energy_threshold=4000 
with m as source: r.adjust_for_ambient_noise(source)#<!----Auto adjust for noise in the room----!>
print("Set MINIMUM ENERGY THRESHOLD to {}".format(r.energy_threshold))

def notes():
    os.system('espeak "hello what category should this note be placed"')
    cat=['"meeting"', '"job"', '"important"', '"notes"']
    print(cat[0], cat[1], cat[2], cat[3])
    try:
        with sr.Microphone() as source:
            listen=r.listen(source)
            directory=r.recognize_google(listen)
            print(directory)
            os.system('espeak "what should the note say"')

            audio=r.listen(source)
            Command = r.recognize_google(audio)
            print(Command)
            if 'meeting' in directory:
                os.system('espeak "ok i will add it to the meeting directory"')
                f=open('/root/python/notes/meeting', 'a')
                f.write(Command)
                f.close()
            elif 'job' in directory:
                os.system('espeak "how unexpected of you"')
                os.system('espeak "The note will be added to the job directory good luck"')
                f=open('/root/python/notes/jobs', 'a')
                f.write(Command)
                f.close()
            elif 'important' in directory:
                os.system('espeak "Important ok i will protect this note with my life sir placing in the important directory"')
                f=open('/root/python/notes/important', 'a')
                f.write(Command)
                f.close()
                
            elif 'notes' in directory:
                os.system('espeak "ok sir the note will be added"')
                f=open('/root/python/notes/notes', 'a')
                f.write(Command)
            else:
                os.system('espeak "sorry sir i seem to have misplaced the note haha haha"')

    except sr.UnknownValueError:
        print("exception unknown value")
        

    except sr.RequestError as e:
        print("ERROR ERROR".format(e))

