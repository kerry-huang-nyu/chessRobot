#from re import S
from phrase import *
from chess import *

def cleanData(command):
    REMOVE_CHARACTERS = [" ", "-", "."]

    for char in REMOVE_CHARACTERS:
        while char in command: #remove space
            command = command.replace(char, '')
    command = command.lower() #lowercase
    return(command)
  
def parse(command):
    for word in key_phrase:
        if word in command:
            return word

    for word in replacement_dictionary:
        if word in command: #clean up the command into a phrase  
            command = command.replace(word, replacement_dictionary[word])

    PROMOTABLE_PIECE = ['q', 'r', 'b', 'n']
    #checks if the command is an actual valid move 
    if len(command) == 4:
        if command[:2] == command[2:]: #takes care of the e2e2 exception
            return None
        if command[:2] in SQUARE_NAMES and command[2:] in SQUARE_NAMES:
            return command
    
    elif len(command) == 5: 
        if command[:2] in SQUARE_NAMES and command[2:4] in SQUARE_NAMES:
            if command[4] in PROMOTABLE_PIECE: 
                return command
        
    return None

#checks if the system parses 5 letter commands
#print(parse(cleanData("e2e8")))