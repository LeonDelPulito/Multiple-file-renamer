#This simple command make you rename a lot of file in short time, like you "casually have some file that have a certain word behind the name" and you don't want that, with this
#you can simply insert the path and the word or phrase to remove, and the program will do all in some seconds even less and 
#give you all the file without the word that you have inserted
#WARNING!!!
#Before executing the python file, you have to have the os library installed for make the program able to run so from a terminal you have to run this command: pip install os

#casual error: if you have the folder in the desktop and the program says you some error try inserting in the path ONLY the forder name
#(depend on where you have stored this python file)

#Made by LeonDelPulito 16/10/2023


import os

def rinomina_file(directory, parola_da_rimuovere):
    for filename in os.listdir(directory):
        if parola_da_rimuovere in filename:
            nuovo_nome = filename.replace(parola_da_rimuovere, '')
            vecchio_percorso = os.path.join(directory, filename)
            nuovo_percorso = os.path.join(directory, nuovo_nome)
            os.rename(vecchio_percorso, nuovo_percorso)
            print(f"Rinominato '{filename}' in '{nuovo_nome}'")

#Variabili

directory = input("enter the path:") 
parola_da_rimuovere = input("enter the word or phrase:")

rinomina_file(directory, parola_da_rimuovere)