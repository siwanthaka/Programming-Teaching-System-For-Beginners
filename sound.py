import pyttsx3

class Voice:

  def __init__(self, rate=150,volume=1):
   self.engine = pyttsx3.init()
   self.engine.setProperty('rate',rate)
   self.engine.setProperty('volume', volume)
   

  def speak(self, text):
   self.engine.say(text)
   self.engine.runAndWait()

  def change_rate(self, rate):
   self.engine.setProperty('rate', rate)

  def change_volume(self, volume):
   self.engine.setProperty('volume', volume)
