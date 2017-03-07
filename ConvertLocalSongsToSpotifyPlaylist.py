import os
import re
import webbrowser

def search(directory):
    
        extensions = (".mp3", ".mp4", ".m4a", ".ogg", ".oga", ".raw", ".wav") #if you change this to any extension that is not exactly 4 characters long, this will break
        with open("songs.txt", "w+") as output:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    try:
                        if file.endswith((extensions)):
                            file = file[:-4]
                            output.write(file +"\n")
                            print(file)
                    except Exception as ex:
                        print("There was something wrong with the song printed just now**************************************************************************")
        
            webbrowser.open("http://www.playlist-converter.net/#/", new=2)
            webbrowser.open("songs.txt")
            
search(input("Enter the directory you wish to search: "))