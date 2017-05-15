#the_poetry_generator 2017
import random #needed for random selection of words
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def main():
   #"""Opens up one of the two random files."""
   poem = open("Poem_Generator.txt","w") #Opens up new file "Poem_Generator.txt"
   sentence = []
   for i in range(5): #Create 5 sentences
      sentence.append(create_sentence()) 
      poem.write(sentence[i])
      poem.write("\n")
   poem.close()
                 
def create_sentence():
        #Articles
        articles1 = ["the","an"]
        articles2 = ['the','a']
        articles3 = ['The','An']
        articles4 = ['The',"A"]

        #Subject
        animal = open("Animals.txt", "r") #Opens up the animals string
        animal_list =animal.readline().split(",") #Splits the string into a list
        subject = animal_list[random.randrange(0,len(animal_list))] #Subject is a random word
        
        #Verb
        verb = open("Verbs.txt","r") #Opens verbs
        verb_list = verb.readline().split(",")
        verbs = verb_list[random.randrange(0,len(verb_list))] #verbs is random verb
        
        #Object                 
        if (random.randrange(1,2) == 1): #if a random number between 1 and 2 is equal to 1:
           object_file = open("Objects.txt","r") #we choose an objects.txt entry as an object
           object_list = object_file.readline().split(",")
           objects = object_list[random.randrange(0,len(object_list))] #random object
                          
        else:
           objects = animal_list[random.randrange(0,len(animal_list))] #object is an animal entry
        
        #chooses a random adjective
        adj = open("Adj.txt","r")
        adj_list = adj.readline().split(",")
        adjs = adj_list[random.randrange(0,len(adj_list))]
                          
        if adjs[0] in "aeiouAEIOU":
           Article = articles3[random.randrange(0,len(articles1))] #if adjective begins with vowel, article is either the or a
                          
        else:
           Article = articles4[random.randrange(0,len(articles2))]
           
        # Noun Phrase + Object Phrase   
        nounphrase = noun_phrase(subject,adjs) #nounphrase is a concatenation of the article, the adjective, and the subject
        if objects[0] in "aeiouAEIOU":
           articles = articles1[random.randrange(0,len(articles1))] #if adjective begins with vowel, article is either the or a
                          
        else:
           articles = articles2[random.randrange(0,len(articles2))]
        objectphrase = obj_phrase(objects)

        
        #adverbs
        adv = open("Adverbs.txt")
        adv_list = adv.readline().split(",")
        advs = adv_list[random.randrange(0,len(adv_list))]

        #Creates the verb phrase and decides the present ending of the verb depending on the object of the sentence
        if verbs[len(verbs)-1] == 's' or verbs[len(verbs)-1] == 'h' or verbs[len(verbs)-1] == 'x':
           verbs = verbs +("es")
        
        else:
           verbs = verbs + 's'
        verbphrase = verb_phrase(verbs,advs)
        
        
        #close all the open files
        animal.close()
        verb.close()
        object_file.close()
        adj.close()
        adv.close()
                          
        return Article+" "+repr(nounphrase) + repr(verbphrase) + " " + articles + " "+ repr(objectphrase) #return the sentence

class noun_phrase:
        def __init__(noun,word,adj):
                noun.x = word
                noun.y = adj
                
        def getNoun(noun):
                """Gets the noun"""
                return noun.x
                          
        def getAdj(noun):
                """Gets the adjective"""
                return noun.y
                         
        def __repr__(noun):
                return str(noun.y)+" "+str(noun.x)+" "

class verb_phrase: #gets verbphrase
        def __init__(verb,word,adv):
                verb.x = word
                verb.y = adv

        def getVerb(verb):
                return verb.x

        def getAdv(verb):
                return verb.y

        def __repr__(verb):
                return str(verb.y) + " " + str(verb.x)
class obj_phrase: #gets object of the sentence phrase
      def __init__(obj,word):
         obj.x = word
      def getWord(obj):
         return obj.x
      def __repr__(obj):
         return str(obj.x) + "."
      
class user_gui:
        def __init__(self):
                self.create_window() #creates window with title
                self.create_widgets() #creates widgets
                
        def open_file(self):
                """opens and returns poem text"""
                f = open("Poem_Generator.txt", "r")
                poems = f.read()
                return poems

        def create_window(self):
                """creates the window."""
                self.root= tk.Tk() #creating window
                self.root.title("Poem Generator")

        def poetry(self):
                poetry_frame = ttk.Frame(self.root, width = 240, height = 300)
                poetry_frame.grid(row = 1, column = 2)
                main()
                poetry_text = self.open_file()
                poetry_label = ttk.Label(poetry_frame, wraplength = 240,text = poetry_text)
                poetry_label.grid(row = 0, column = 0, sticky=tk.N+tk.E, ipadx =10, ipady = 10)
                poetry_label.columnconfigure(0, weight = 1)
                poetry_label.rowconfigure(0, weight = 1)
                
        def create_widgets(self):
                """creates all the widgets and their frames."""
                s = ttk.Style() #using ttk style
                s.configure('.', font=('Helvetica', 12), sticky=tk.N+tk.E+tk.S+tk.W)

                """ABOUT"""
                about_frame = ttk.Frame(self.root, width = 240, height = 300)
                about_frame.grid(row = 1, column = 1, sticky=tk.N+tk.E, ipadx = 10, ipady = 10)
                about_frame.columnconfigure(0, weight = 1)
                about_frame.rowconfigure(0, weight = 1)

                about_text = """ABOUT
         
This is a random poem generator created by Charlie Carlson, Iain Irwin, and Nic Hubig for the CSCI121 final project."""

                about_label = ttk.Label(about_frame, wraplength = 240, text = about_text)
                about_label.grid(row = 0, column = 0, sticky=tk.N+tk.E, ipadx = 10, ipady = 10)
                about_label.columnconfigure(0, weight = 1)
                about_label.rowconfigure(0, weight = 1)
                

                """GENERATE BUTTON"""
                generate = ttk.Button(self.root, text="Generate poetry", command = self.poetry)
                generate.grid(row=3, column= 1)
                generate.columnconfigure(0, weight = 1)
                generate.rowconfigure(0, weight = 1)
                

                """QUIT BUTTON"""
                quit_button = ttk.Button(self.root, text="Quit")
                quit_button.grid(row=3, column=2)
                quit_button['command'] = self.root.destroy
                
program = user_gui()
program.root.mainloop()

