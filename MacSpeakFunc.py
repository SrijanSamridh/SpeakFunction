

from os import system

def speak(Audio):
  print(f": {Audio}")
  system("say {}".format(Audio))
  
  
  
