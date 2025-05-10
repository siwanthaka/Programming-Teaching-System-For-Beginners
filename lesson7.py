from sound import Voice  

class Lesson7:  
    def __init__(self):
        self.voice = Voice()  

    def start_lesson7(self):
        self.voice.speak("Alright, let's begin Lesson Seven.")
        self.voice.speak("Today, we are diving into arrays and lists in programming.")

        print("\n\033[1mTHE SEVENTH LESSON: ARRAYS / LISTS IN PROGRAMMING\033[0m\n")
        input("Press ENTER when you're ready to continue...")

        print("Before we begin, what do you think arrays or lists are?")
        self.voice.speak("What do you think arrays or lists are?")
        input("") 

        print("\nArrays or Lists allow us to store multiple values in a single variable.")
        self.voice.speak("Arrays and lists help us store multiple values in a single variable.")
        input("Press ENTER to proceed...")

        print("\n\033[31mWhy do we even need Arrays or Lists?\033[0m\n")
        self.voice.speak("Why do we need arrays or lists?")

        print("\033[32mSome key benefits of using arrays and lists:\n"
              "  - Store multiple values without needing tons of separate variables\n"
              "  - Make our code cleaner and less repetitive\n"
              "  - Easier to loop through values instead of handling them one by one\n"
              "  - Keep data structured and organized\033[0m\n")
        self.voice.speak("They make our code more efficient, readable, and structured.")
        input()

        print("\n\033[31mLet's explore how arrays and lists work in different programming languages, step by step.\033[0m")
        self.voice.speak("Now, let's learn about arrays and lists in different languages.")
        input()

        print("\n\033[33mSTEP 1: Defining an Array / List\033[0m\n")
        self.voice.speak("First, let's learn how to define an array or a list.")

        print("\033[32mDifferent languages have slightly different ways to define them.\033[0m\n")
        self.voice.speak("For example, in Python, we use square brackets to define a list.")
        input("Press ENTER to see an example...")

        print("\nPython:")
        print("  my_list = [1, 2, 3, 4, 5]\n")
        self.voice.speak("Here is a Python list.")

        input("\nPress ENTER to continue...")

  
        print("\n\033[33mSTEP 2: Accessing Elements\033[0m\n")
        self.voice.speak("Now, let's see how to access elements.")

        print("\033[32mWe use an index (starting at 0) to get values from a list.\n\033[0m")
        input("Press ENTER to see an example...")

        print("\nPython:")
        print("  print(my_list[0])  # Output: 1\n")
        input("Press ENTER to continue...")

        
        print("\n\033[33mSTEP 3: Modifying Elements\033[0m\n")
        self.voice.speak("Let's see how to change values inside a list.")

        print("\033[32mWe can update values by assigning a new one to a specific index.\n\033[0m")
        input("Press ENTER for an example...")

        print("\nPython:")
        print("  my_list[0] = 10  # Changes first element to 10\n")
        input("Press ENTER to continue...")

        
        print("\n\033[33mSTEP 4: Iterating Over an Array / List\033[0m\n")
        self.voice.speak("Now, let's loop through a list.")

        print("\033[32mLoops allow us to process multiple elements efficiently.\n\033[0m")
        input("Press ENTER to see an example...")

        print("\nPython:")
        print("  for item in my_list:")
        print("      print(item)\n")
        input("Press ENTER to continue...")

       
        print("\n\033[33mSUMMARY\033[0m\n")
        self.voice.speak("Let's wrap up everything we've learned.")

        print("\033[34mQuick Recap:\n"
              "  - Arrays / Lists store multiple values in a single variable.\n"
              "  - We access elements using an index (starting at 0).\n"
              "  - We can modify values by assigning new ones.\n"
              "  - Loops make it easy to iterate over elements.\033[0m\n")

        self.voice.speak("Arrays and lists help us store, access, modify, and loop through values efficiently.")
        input("Press ENTER to continue...")

        print("\033[31mHaha, my turn is over. Now it's your turn to test your knowledge!\033[0m\n")
        self.voice.speak("like another lesson here is a question for you ")

    def start_quiz7(self):
        self.voice.speak("Here's a quick question for you.")

        print("\nWhich index does an array or list start from in most programming languages?\n")
        print(" A) 1")
        print(" B) 0")
        print(" C) -1")
        print(" D) 2")

        answer = input("\nEnter the correct answer (A/B/C/D): ").strip().upper()

        if answer == "B":
            print("\n✅ Wow! Congratulations, that's correct! Now let's move on.")
            self.voice.speak("Correct! Great job!")
        else:
            print("\n\033[32m❌ Oops! That's incorrect. Try again.\033[0m")
            self.voice.speak("Oops! That was incorrect. Give it another shot.")
            self.start_quiz7()

