from PyDictionary import PyDictionary

def check_word(word):
    dictionary = PyDictionary()
    # The word is not found in the dictionary
    if dictionary.meaning(word,True) is None:
        return False
    # The word is found in the dictionary
    else:
        return True

def encryptCC(sentence, shift):
  # Return the encrypted sentence using the shift number
  return 
  
def decryptCC(sentence, shift):
  # Return the decrypted sentence using the shift number
  return

# EXTRA CREDIT OR MARBLES!!!
def solveCC(sentence):
  # Return the decrypted sentence for an input in which you DO NOT know the shift. Use either brute force or a heuristic algorithm. 
  # HINT: You will need the check_word method found above
  
