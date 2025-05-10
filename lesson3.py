from sound import Voice

class Lesson3:

    def __init__(self):
        self.voice = Voice()

    def start_lesson3(self):
        self.voice.speak("Starting lesson three.")
        self.voice.speak("In this lesson, we will learn about operators in programming.")

        self.voice.speak("An operator is a special symbol that performs operations on variables and values.")
        print("THE THIRD LESSON IS ABOUT OPERATORS IN PROGRAMMING\n")
        input("Press ENTER to continue\n")

        print("WHAT DO YOU THINK AN OPERATOR IS??")
        self.voice.speak("What do you think an operator is?")
        input("")

        print("An operator is a special symbol that performs operations on variables and values.")
        self.voice.speak("An operator is a special symbol that performs operations on variables and values.")
        input("")

        print("\033[31mWhy do we need Operators?\033[0m\n")
        self.voice.speak("Why do we need operators?")

        print("\033[32mOperators help us perform calculations and manipulate data in programming.\n"
              "\n  * Used for arithmetic calculations"
              "\n  * Used to compare values"
              "\n  * Used to combine logical conditions"
              "\n  * Used to assign values\033[0m\n")
        self.voice.speak("Operators help us perform calculations, compare values, combine logical conditions, and assign values.")
        input()

        print("\033[31mNow I'm Going To Teach Different Types of Operators Step By Step\033[0m\n")
        self.voice.speak("Now I’m going to teach you different types of operators step by step.")
        input()

        print("\033[33m STEP 1: Arithmetic Operators\033[0m\n")
        self.voice.speak("First, let's learn about arithmetic operators. These perform mathematical operations like addition, subtraction, BLa BLA.")

        print("\033[32mThese operators perform mathematical operations like addition, subtraction, etc.\n"
              "\nExamples:\n"
              "\n  * Addition: a + b"
              "\n  * Subtraction: a - b"
              "\n  * Multiplication: a * b"
              "\n  * Division: a / b\033[0m\n")
        self.voice.speak("For example: a plus b, a minus b, a times b, a divided by b.")
        input()

        print("\033[33m STEP 2: Comparison Operators\033[0m\n")
        self.voice.speak("Next, we have comparison operators. These compare two values and return either True or False.")

        print("\033[32mThese operators compare two values and return True or False.\n"
              "\nExamples:\n"
              "\n  * Equal to: a == b"
              "\n  * Not equal to: a != b"
              "\n  * Greater than: a > b"
              "\n  * Less than: a < b\033[0m\n")
        self.voice.speak("For example: a equals b, a does not equal b, a is greater than b, a is less than b.")
        input()

        print("\033[33m STEP 3: Logical Operators\033[0m\n")
        self.voice.speak("Next, let's look at logical operators. These are used to combine multiple conditions.")

        print("\033[32mThese operators combine multiple conditions.\n"
              "\nExamples:\n"
              "\n  * AND: (a > 5 and b < 10)"
              "\n  * OR: (a > 5 or b < 10)"
              "\n  * NOT: not(a > 5)\033[0m\n")
        self.voice.speak("For example: a greater than 5 and b less than 10, a greater than 5 or b less than 10, not a greater than 5.")
        input()

        print("\033[33m STEP 4: Assignment Operators\033[0m\n")
        self.voice.speak("Finally, we have assignment operators. These are used to assign values to variables.")

        print("\033[32mThese operators assign values to variables.\n"
              "\nExamples:\n"
              "\n  * a = 5"
              "\n  * a += 2 (equivalent to a = a + 2)"
              "\n  * a *= 3 (equivalent to a = a * 3)\033[0m\n")
        self.voice.speak("For example: a equals 5, a plus equals 2, a times equals 3.")
        input()

        print("\033[33m SUMMARY \033[0m\n")
        self.voice.speak("Now let's summarize the lesson.")

        print("\033[34mOperators are symbols that perform operations on values.\n"
              "\n  * Arithmetic Operators: +, -, *, /"
              "\n  * Comparison Operators: ==, !=, >, <"
              "\n  * Logical Operators: and, or, not"
              "\n  * Assignment Operators: =, +=, -=\033[0m\n")
        self.voice.speak("Summary: Arithmetic operators include plus, minus, times, and divided by. Comparison operators include equals, not equals, greater than, and less than. Logical operators include and, or, not. Assignment operators include equals, plus equals, and times equals.")
        input()

        print("\033[31mHaha, My turn is over. Now it's your turn!!\033[0m\n")
        self.voice.speak("ok enougf, I can give you a chance . Now it's your turn!")

    def start_quiz3(self):
        self.voice.speak("Which of the following is a logical operator?")

        print(" \nWhich of the following is a logical operator?\n")
        print(" A) +")
        print(" B) and")
        print(" C) ==")
        print(" D) *")

        answer = input("\nEnter the correct answer (A/B/C/D): ").upper()

        if answer == "B":
            print("    \n\033[32m✅  Wow congratulations! Correct. Now let's move to the next lesson.\033[0m")
            self.voice.speak("Congratulations, that is correct! Now let's move to the next lesson.")
        else:
            print("    \n\033[31m❌ Incorrect answer! Try again.\033[0m")
            self.voice.speak("Incorrect answer! Try again.")
            self.start_quiz3()
