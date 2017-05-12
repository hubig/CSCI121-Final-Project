#the_poetry_generator 2017
import random #needed for random selection of words

def main(file):
   #"""Opens up one of the two random files."""
        articles1 = ["the","an"]
        articles2 = ['the','an']
        animal = file.open("Animals-"+str(random.randrange(1,2), "r")
        animal_list = animal.split(",")
        subject = animals[random.range(0,len(animal_list)+1)
        verb = file.open("Animals-"str(random.randrange(1,2),"r")
        verb_list = verb.split(",")
        verbs = verb_list[random.randrange(0,len(verb_list)+1)
        if(random.randrange(1,2) == 1):
           object_file = file.open("Objects-"+str(random.randrange(1,2),"r")
           object_list = object_file.split(",")
           obects = object_list[random.randrange(0,len(object_list)+1)]
        else:
           obects = animal_list[random.randrange(0,len(animal_list)+1)]  
        adj = file.open("Adj-"+str(random.randrange(1,2)),"r")
        adj_list = adj.split(",")
        adjs = adj_list[random.randrange(0,len(adj_list)+1)]
        if adjs[0] in "aeiouAEIOU":
           article = articles1[random.randrange(0,len(articles1+1))]
        else:
           article = articles2[random.randrange(0,len(articles2+1))]                      
        nounphrase = noun_phrase(subject,adjs,article)
        adv = file.open("Adv")
        adv_list = adv.split(",")
        advs = adv_list[random.randrange(0,len(adv_list)+1)]
        verbphrase = verb_phrase(verbs,advs)
                                   
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
                          

                          
        def __str__(noun):
                return str(noun.z)+" "+str(noun.y)+" "+str(noun.z)

class verb_phrase:
        def __intit__(verb,word,adv):
                verb.x = word
                verb.y = adv

        def getVerb(verb):
                return verb.x

        def getAdv(verb):
                return verb.y

        def __str__(verb):
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
