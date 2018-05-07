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
    print(definition);

def get_word():
  word = input("type a word: ")
  return word.lower()

return_definition( get_word() )
