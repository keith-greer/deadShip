import time,sys

def typingPrint(text):
  
  for character in text: 
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

    return typingPrint