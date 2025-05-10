from sound import Voice

class Lesson5:

    def __init__(self):
        self.voice = Voice()

    def start_lesson5(self):
        self.voice.speak("Starting our fifth lesson about programming .")
        self.voice.speak("In this lesson, we will learn about loops in programming.")
        
        print("THE FIFTH LESSON IS ABOUT LOOPS IN PROGRAMMING\n")
        input("Press ENTER to continue\n")
        
        print("WHAT DO YOU THINK LOOPS ARE??")
        self.voice.speak("What do you think loops are?")
        input("")
        
        print("Loops allow us to execute a block of code multiple times until a certain condition is met.")
        self.voice.speak("Loops allow us to execute a block of code multiple times until a certain condition is met.")
        input("")
        
        print("\033[31mWhy do we need Loops?\033[0m\n")
        self.voice.speak("Why do we need loops?")
        
        print("\033[32mLoops help us automate repetitive tasks, making our code more efficient.\n"
              "\n  * loops can Reduce code duplication"
              "\n  * they Improve efficiency"
              "\n  * they also Automate repetitive tasks\033[0m\n")
        self.voice.speak("these loops help us automate repetitive tasks and also making our code more efficient.")
        input()
        
        print("\033[31mNow I'm Going To Teach You Different Types of Loops Step By Step\033[0m\n")
        self.voice.speak("Now I'm going to teach you different types of loops step by step.")
        input()
        
        print("\033[33m STEP 1: for Loop\033[0m\n")
        self.voice.speak("First, let's learn about the 'for' loop. It is used to iterate over a sequence like a list, tuple, or range.")
        
        print("\033[32mThe 'for' loop is used to iterate over a sequence like a list, tuple, or range.\n"
              "\nExample:\n"
              "\n  for i in range(5):" 
              "\n      print(i)\033[0m\n")
        self.voice.speak("For example, a for loop can print numbers from zero to four using range.")
        input()
        
        print("\033[33m STEP 2: while Loop\033[0m\n")
        self.voice.speak("Next, let's learn about the 'while' loop. It executes a block of code as long as a condition remains true.")
        
        print("\033[32mThe 'while' loop executes a block of code as long as a condition remains true.\n"
              "\nExample:\n"
              "\n  x = 0"
              "\n  while x < 5:" 
              "\n      print(x)"
              "\n      x += 1\033[0m\n")
        self.voice.speak("For example, a while loop can print numbers while x is less than five.")
        input()
        
        print("\033[33m STEP 3: break and continue Statements\033[0m\n")
        self.voice.speak("Now let's learn about 'break' and 'continue' statements. The 'break' statement stops the loop, while 'continue' skips to the next iteration.")
        
        print("\033[32mThe 'break' statement stops the loop, while 'continue' skips to the next iteration.\n"
              "\nExample:\n"
              "\n  for i in range(5):" 
              "\n      if i == 3:" 
              "\n          break"
              "\n      print(i)\n"
              "\n  for i in range(5):" 
              "\n      if i == 3:" 
              "\n          continue"
              "\n      print(i)\033[0m\n")
        self.voice.speak("For example, using break will stop a loop when i equals three, while continue will skip the value three and continue looping.")
        input()
        
        print("\033[33m SUMMARY \033[0m\n")
        self.voice.speak("Now let's summarize the lesson.")
        
        print("\033[34mLoops help us repeat code efficiently.\n"
              "\n  * 'for' loop iterates over a sequence."
              "\n  * 'while' loop runs while a condition is true."
              "\n  * 'break' stops a loop early."
              "\n  * 'continue' skips to the next iteration.\033[0m\n")
        self.voice.speak("Summary: The 'for' loop iterates over a sequence. The 'while' loop runs while a condition is true. The 'break' statement stops a loop early, and the 'continue' statement skips to the next iteration.")
        input()
        
        print("\033[31mHaha, My turn is over. Now it's your turn!!\033[0m\n")
        self.voice.speak("ok ok, now I give you a chance to check your knowledge about this lesson, you readyy,")
    
    def start_quiz5(self):
        self.voice.speak("Which loop is best for iterating over a sequence like a list or range?")
        
        print(" \nWhich loop is best for iterating over a sequence like a list or range?\n")
        print(" A) while")
        print(" B) for")
        print(" C) if")
        print(" D) switch")
        
        answer = input("\nEnter the correct answer (A/B/C/D): ").upper()
        
        if answer == "B":
            print("\n✅  Wow congratulations! Correct. Now let's move to the next lesson.")
            self.voice.speak("Congratulations, that is correct! Now let's move to the next lesson.")
        else:
            print("\n\033[31m❌ Incorrect answer! Try again.\033[0m")
            self.voice.speak("Incorrect answer! Try again.")
            self.start_quiz5()
