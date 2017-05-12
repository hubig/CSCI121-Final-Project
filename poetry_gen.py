#the_poetry_generator 2017
import random #needed for random selection of words

def main(file):
   #"""Opens up one of the two random files."""
   poem = open("Poem_Generator.txt","w") #Opens up new file "Poem_Generator.txt"
   sentence = []
   for i in range(5): #Create 5 sentences
      sentence[i] = create_sentence() 
      poem.write(sentence[i])
      poem.write("\n")
   poem.close()
                 
def create_sentence():
        articles1 = ["the","an"]
        articles2 = ['the','a']
        animal = file.open("Animals.txt", "r") #Opens up the animals string
        animal_list = animal.split(",") #Splits the string into a list
        subject = animals[random.range(0,len(animal_list)+1)] #Subject is a random word
      
        verb = file.open("Verbs.txt","r") #Opens verbs
        verb_list = verb.split(",")
        verbs = verb_list[random.randrange(0,len(verb_list)+1)] #verbs is random verb
                          
        if (random.randrange(1,2) == 1): #if a random number between 1 and 2 is equal to 1:
           object_file = file.open("Objects.txt","r") #we choose an objects.txt entry as an object
           object_list = object_file.split(",")
           objects = object_list[random.randrange(0,len(object_list)+1)] #random object
                          
        else:
           objects = animal_list[random.randrange(0,len(animal_list)+1)] #object is an animal entry
        
        #chooses a random adjective
        adj = file.open("Adj.txt","r")
        adj_list = adj.split(",")
        adjs = adj_list[random.randrange(0,len(adj_list)+1)]
                          
        if adjs[0] in "aeiouAEIOU":
           article = articles1[random.randrange(0,len(articles1+1))] #if adjective begins with vowel, article is either the or a
                          
        else:
           article = articles2[random.randrange(0,len(articles2+1))]                   
            
        nounphrase = noun_phrase(subject,adjs,article) #nounphrase is a concatenation of the article, the adjective, and the subject
        
        #adverbs
        adv = file.open("Adv.txt")
        adv_list = adv.split(",")
        advs = adv_list[random.randrange(0,len(adv_list)+1)]
        verbphrase = verb_phrase(verbs,advs)
      
        #close all the open files
        animal.close()
        verb.close()
        object_file.close()
        adj.close()
        adv.close()
                          
        return nounphrase.nounphrase + verbphrase.verbphrase #return the sentence
                          
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
                         
        def nounphrase(noun):
                return str(noun.z)+" "+str(noun.y)+" "+str(noun.z)

class verb_phrase:
        def __intit__(verb,word,adv):
                verb.x = word
                verb.y = adv

        def getVerb(verb):
                return verb.x

        def getAdv(verb):
                return verb.y

        def verbphrase(verb):
                return str(verb.y) + " " + str(verb.x)

def articlenounmix(noun):
        article_chooser = random.randrange(2) #assigns article_chooser a int between 0 and 1
        if article_chooser == 0:
                noun = "the " + noun #use article "the" if == 0
                return noun
        elif article_chooser ==1:
                for i in noun:
                        if i in "a, A, e, E, i, I, o, O, u, U":
                                noun = "an " + noun
                        break #only iterates through the first char in the word
                return noun
        else:
                noun = "a " + noun
                return noun
