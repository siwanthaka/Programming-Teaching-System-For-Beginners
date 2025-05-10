from sound import Voice

class Lesson4:

    def __init__(self):
        self.voice = Voice()

    def start_lesson4(self):
        self.voice.speak("Starting lesson four.")
        self.voice.speak("In this lesson, we will learn about control flow in programming.")

        print("THE FOURTH LESSON IS ABOUT CONTROL FLOW IN PROGRAMMING\n")
        input("Press ENTER to continue\n")

        print("WHAT DO YOU THINK CONTROL FLOW IS??")
        self.voice.speak("What do you think control flow is?")
        input("")

        print("Control flow refers to the order in which individual statements, instructions, or functions are executed in a program.")
        self.voice.speak("Control flow refers to the order in which statements, instructions, or functions are executed in a program.")
        input("")

        print("\033[31mWhy do we need Control Flow?\033[0m\n")
        self.voice.speak("Why do we need control flow?")

        print("\033[32mControl flow helps us make decisions and execute specific blocks of code based on conditions.\n"
              "\n  * Allows decision-making"
              "\n  * Helps control program execution"
              "\n  * Improves program logic and efficiency\033[0m\n")
        self.voice.speak("Control flow helps us make decisions, control execution, and improve program logic.")
        input()

        print("\033[31mNow I'm Going To Teach You Conditional Statements Step By Step\033[0m\n")
        self.voice.speak("Now I’m going to teach you conditional statements step by step.")
        input()

        print("\033[33m STEP 1: if Statement\033[0m\n")
        self.voice.speak("First, let's learn about the 'if' statement. It executes a block of code only if a condition is true.")

        print("\033[32mThe 'if' statement is used to execute a block of code only if a condition is true.\n"
              "\nExample:\n"
              "\n  age = 18"
              "\n  if age >= 18:" 
              "\n      print(\"You are eligible to vote.\")\033[0m\n")
        self.voice.speak("For example, if age is greater than or equal to eighteen, print 'You are eligible to vote.'")
        input()

        print("\033[33m STEP 2: if-else Statement\033[0m\n")
        self.voice.speak("Next, we have the 'if-else' statement. It allows us to execute one block of code if the condition is true and another if it is false.")

        print("\033[32mThe 'if-else' statement allows us to execute one block of code if the condition is true and another if it's false.\n"
              "\nExample:\n"
              "\n  number = 5"
              "\n  if number % 2 == 0:" 
              "\n      print(\"Even number\")"
              "\n  else:" 
              "\n      print(\"Odd number\")\033[0m\n")
        self.voice.speak("For example, if a number is divisible by two, print 'Even number.' Otherwise, print 'Odd number.'")
        input()

        print("\033[33m STEP 3: if-elif-else Statement\033[0m\n")
        self.voice.speak("Now, let's learn about the 'if-elif-else' statement. It is used when multiple conditions need to be checked sequentially.")

        print("\033[32mThe 'if-elif-else' statement is used when multiple conditions need to be checked sequentially.\n"
              "\nExample:\n"
              "\n  marks = 85"
              "\n  if marks >= 90:" 
              "\n      print(\"Grade: A\")"
              "\n  elif marks >= 75:"
              "\n      print(\"Grade: B\")"
              "\n  else:"
              "\n      print(\"Grade: C\")\033[0m\n")
        self.voice.speak("For example, if marks are ninety or above, print 'Grade A.' If marks are seventy-five or above, print 'Grade B.' Otherwise, print 'Grade C.'")
        input()

        print("\033[33m SUMMARY \033[0m\n")
        self.voice.speak("Now let's summarize the lesson.")

        print("\033[34mControl flow statements allow decision-making in programs.\n"
              "\n  * 'if' executes code when a condition is true."
              "\n  * 'if-else' executes one block if true, another if false."
              "\n  * 'if-elif-else' checks multiple conditions sequentially.\033[0m\n")
        self.voice.speak("Summary: The 'if' statement executes code when a condition is true. The 'if-else' statement executes one block if true, another if false. The 'if-elif-else' statement checks multiple conditions sequentially.")
        input()

        print("\033[31mHaha, My turn is over. Now it's your turn!!\033[0m\n")
        self.voice.speak("ok now I want to try you,  so try this ")

    def start_quiz4(self):
        self.voice.speak("Which of the following statements is used for decision-making in Python?")

        print(" \nWhich of the following statements is used for decision-making in Python?\n")
        print(" A) for")
        print(" B) while")
        print(" C) if")
        print(" D) def")

        answer = input("\nEnter the correct answer (A/B/C/D): ").upper()

        if answer == "C":
            print("\n✅  Wow congratulations! Correct. Now let's move to the next lesson.")
            self.voice.speak("Congratulations, that is correct! Now let's move to the next lesson.")
        else:
            print("\n\033[31m❌ Incorrect answer! Try again.\033[0m")
            self.voice.speak("Incorrect answer! Try again.")
            self.start_quiz4()
