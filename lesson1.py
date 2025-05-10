
from sound import Voice

class Lesson1:
 
  def __init__(self):
     self.voice = Voice()

  def start_lesson1(self):
    
    self.voice.speak("Lets Starting lesson one.")
    self.voice.speak("wait a minute, now i'm going to introduce about our first lesson, so our first lesson is about variables in programmnig")
    self.voice.speak("""In programming, a **variable** is like a container where you store information. The container has a **name** (the variable name), and inside it is a **value** (like a number or text). You can change the value inside the variable whenever needed.
                 so Why Are Variables Important?

            number one    Storing Information   : Variables hold data that your program can use.
            number two    Changing Information  : The value of a variable can change as the program runs.
            number three  Making Programs Flexible  : Variables allow programs to work with dynamic values instead of fixed ones.

            Think of a variable as a box with a label, and you can put different things in it at different times!
                ok please hit enter to continue our lesson in detailed
        """)
    
    self.voice.speak("yah, let's go through the lesson about variables")   
    print("THE FIRST LESSON IS ABOUT VARIABLES IN PROGRAMMING\n")
    input("press ENTER button to continue \n")

    print("WHAT DO YOU THINK ABOUT THE VARIABLE IS ?? ")
    self.voice.speak("WHAT DO YOU THINK ABOUT THE VARIABLE IS ??" )
    input("")
    print("A variable (vary + able) is a container that can store or hold data types")
    self.voice.speak("A variable (vary + able) is a container that can store or hold data types")
    input("")

    print("\033[31Why do we need Variables??\033[0m\n")
    self.voice.speak("so Why do we need variables")

    print("\033[32mThese variables help us store and manage data in programming \n"
          
            "\n  * No need writing vlaues repeately"
            "\n  * Dynamic Data Handling"
            "\n  * Simplifies Complec Calculatioms"
            "\n  * Flexible and more......\033[0m\n")
    
    self.voice.speak("  because These variables help us store and manage data in programming \n"
          
            "\n   No need writing vlaues repeately"
            "\n   Dynamic Data Handling"
            "\n   Simplifies Complec Calculatioms"
            "\n   Flexible and more")
    input()
    print("\033[31mNow I'm Going To Teach How To Declare A Variable Step By Step\033[0m\n")
    self.voice.speak("don't worry, I know your question, Now I'm Going To Teach How To Declare A Variable Step By Step, follow these steps correctly ")
    input()

    print("\033[33m STEP 1 : Choose a Variable Name\033[0m\n")
    print("\033[32mSelect a name that is meaningful and represents the data it will hold.\n"
            "\nThe name should follow these rules:\n"

            "\n  * Start with a letter (a-z, A-Z) or an underscore (_)."
            "\n  * Can contain letters, digits (0-9), or underscores."
            "\n  * Cannot contain special characters like @ or blank spaces "
            "\n  * Cannot be a keyword like (e.g., if, while, class, etc.)\033[0m\n")
    input()  
    print("\033[32mExamples of valid variable names:\n"

            "\n  * age"
            "\n  * name"
            "\n  * total_amount"
            "\n  * _score\033[0m\n")
    self.voice.speak("Those are examples for valid variable names")

    input()
    print("\033[32mExamples of invalid variable names:\n"

            "\n  * 2age"
            "\n  * if"
            "\n  * my@name"
            "\n  * max score\033[0m\n")
    self.voice.speak("and these are the incorrect variable names in programming ")

    print("\033[33m STEP 2 : Assign a Value to the Variable\033[0m\n")
    self.voice.speak("Next step is assign a value to the variable")

    print("\033[32mUse the = operator to assign a value to the variable."
            "\nThe value can be of any data type (e.g., integer, string, float, etc.).\n"
            "\033[0m\n")
    
    input()  
    print("\033[32mExamples of valid variable declarations:\n"

            "\n  * age = 25"
            "\n  * name = \"Alise\""
            "\n  * score = 9.5\n"

            "\nYou also can reassign different valuse for same variable\n"

            "\nExample:-\n"
            "\n  * age = 25"
            "\n  * age = 30"
            "\033[0m\n")
    self.voice.speak("These are valid variable declarations")
    input()

    print("\033[33m SUMMARY \033[0m\n")

    print("\033[34mExamples of valid variable names:\n"

            "\n  * Variable names cannot start with a number."
            "\n  * Variable names cannot be reserved keywords."
            "\n  * Variable names cannot be reserved keywords."
            "\n  * cannot use built in functions names"
            "\n  * Spaces are not allowed.\033[0m\n")
    
    input()
    print("\033[31m Haha, My turn is over. Now it's your turn!! \033[0m\n")
    self.voice.speak("haa haa, My turn is over. Now it's your turn")


  def start_quiz1(self):
    print(" \nWhat is the correct way to declare a variable \n")
    print(" A) 2name = \"john\"")
    print(" B) user name  = \"Alice\"")
    print(" C) age = 5")
    print(" D) @score = 98")
    
        
    answer = input("\nEnter the correct answer (A/B/C/D): ").upper()

    if answer == "C":
        print("\n✅  Wow congratulations Correct now lets move to next lesson ") 
        self.voice.speak("Wow you are really awesome, and lets move to next lesson")            
    else:
        print("\n❌ It is not the correct answer mate")
        self.voice.speak("your answer is incorrect, but Don't worry, you are a beginner, you can try it again")
        self.start_quiz1()

