from sound import Voice

class Lesson6:
    def __init__(self):
        self.voice = Voice()  
    
    def start_lesson6(self):
        self.voice.speak("Starting lesson six.")
        self.voice.speak("In this lesson, we will learn about functions in programming.")
        
        print("THE SIXTH LESSON IS ABOUT FUNCTIONS IN PROGRAMMING\n")
        input("Press ENTER to continue\n") 

        print("WHAT DO YOU THINK FUNCTIONS ARE??")
        self.voice.speak("What do you think functions are?")
        input("") 
        
        
        print("Functions are reusable blocks of code that perform a specific task. "
              "They help make our code more modular and efficient.")
        self.voice.speak("Functions are reusable blocks of code that perform a specific task. "
                         "They make our code more modular and efficient.")
        input("")  

       
        print("\033[31mWhy do we need Functions?\033[0m\n")
        self.voice.speak("Why do we need functions?")

        print("\033[32mFunctions help us organize our code, avoid repetition, and make programs easier to understand.\n"
              "\n  * Improve code reusability"
              "\n  * Make programs more modular"
              "\n  * Simplify debugging and maintenance\033[0m\n")
        self.voice.speak("Functions help us organize code, improve reusability, and simplify debugging.")
        input()  

        
        print("\033[31mNow I'm Going To Teach You Functions in Different Languages Step By Step\033[0m\n")
        self.voice.speak("Now I’m going to teach you functions in different languages step by step.")
        input()

        
        print("\033[33m STEP 1: Defining a Function\033[0m\n")
        self.voice.speak("First, let's learn how to define a function.")

        print("\033[32mA function is defined differently in various languages.\n")
        self.voice.speak("Functions are defined differently in Python, JavaScript, and Java.")
        input()
        
        print("Python:")
        print("  def greet():")
        print("      print(\"Hello, World!\")\n")
        self.voice.speak("In Python, a function is defined using the 'def' keyword, followed by a name and parentheses.")
        input()

        
        print("\033[33m STEP 2: Calling a Function\033[0m\n")
        self.voice.speak("Now let's see how to call a function.")

        print("\033[32mTo execute a function, we simply call it by its name followed by parentheses.\n")
        self.voice.speak("To call a function, we use its name followed by parentheses.")
        input()
        
        print("Python: greet()")
        print("JavaScript: greet();")
        print("Java: greet();\033[0m\n")
        input()
        
       
        print("\033[33m STEP 3: Function with Parameters\033[0m\n")
        self.voice.speak("Now, let's learn about functions with parameters.")

        print("\033[32mFunctions can accept inputs, called parameters, to make them more dynamic.\n")
        self.voice.speak("Functions can accept inputs called parameters, which allow passing values.")
        input()
        
        print("Python:")
        print("  def greet(name):")
        print("      print(\"Hello,\", name)")
        print("  greet(\"Alice\")\n")
        self.voice.speak("In Python, we define parameters inside the parentheses after the function name.")
        input()

        
        print("\033[33m STEP 4: Function with Return Value\033[0m\n")
        self.voice.speak("Finally, let's learn about functions that return values.")

        print("\033[32mA function can return a value using the 'return' statement.\n")
        self.voice.speak("A function can return a value using the 'return' statement.")
        input()

        print("Python:")
        print("  def add(a, b):")
        print("      return a + b")
        print("  result = add(3, 5)")
        print("  print(result)\n")
        self.voice.speak("For example, a function called 'add' can take two numbers and return their sum.")
        input()
        
      
        print("\033[33m SUMMARY \033[0m\n")
        self.voice.speak("Now let's summarize the lesson.")

        print("\033[34mFunctions allow us to write reusable code blocks in different languages.\n"
              "\n  * 'def' (Python), 'function' (JavaScript), 'public static' (Java) define functions."
              "\n  * Functions are called using their names."
              "\n  * Parameters allow passing values to functions."
              "\n  * 'return' gives a value back from a function.\033[0m\n")
        self.voice.speak("Summary: Functions are reusable, can have parameters, and can return values.")
        input()

        print("\033[31mHaha, My turn is over. Now it's your turn!!\033[0m\n")
        self.voice.speak("ok, I think I teach you at my best so i want ask you a question about this lesson...")

    def start_quiz6(self):
        self.voice.speak("Which keyword is used to define a function in JavaScript?")
        
        print("\nWhich keyword is used to define a function in JavaScript?\n")
        print(" A) func")
        print(" B) define")
        print(" C) function")
        print(" D) method")
        
        answer = input("\nEnter the correct answer (A/B/C/D): ").strip().upper()

        if answer == "C":
            print("\n✅  Wow congratulations! Correct. Now let's move to the next lesson.")
            self.voice.speak("Congratulations, that is correct! Now let's move to the next lesson.")
        else:
            print("\n\033[32m❌ Incorrect answer! Try again.\033[0m")
            self.voice.speak("Incorrect answer! Try again.")
            self.start_quiz6()  
