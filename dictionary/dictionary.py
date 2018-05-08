import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

def return_definition( input ):
    definition = dictionary.get(input)
    if definition == None:
        matches =  get_close_matches(input, dictionary.keys())
        if matches:
            print("I could not find that word. Did you mean " + matches[0] + "?")
        else:
            print("I could not find this word")
    else:
        if type(definition) == list:
            for d in definition:
                print("- %s" % d)
        else:
            print( definition )
    process_input( get_word() )

def get_word():
      print("enter q to quit")
      word = input("type a word: ")
      return word

def process_input(input):
    if input == "q":
        return None
    else:
        return_definition(input)


process_input( get_word() )
