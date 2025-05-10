from sound import Voice  

class Lesson8:
    def __init__(self):
        self.speaker = Voice()

    def start_lesson8(self):
        self.speaker.speak("Welcome to the lesson on file handling in Programming, for example, i will teach you how to handling file in python, so you can get idea about it's concepts, to applly another languages also.")
        
        print("\n\033[1mFILE HANDLING IN PYTHON\033[0m\n")  
        input("Press ENTER when you're ready to continue...")  

        
        print("Files are used to store data permanently, even after the program stops running.")
        self.speaker.speak("Files help us store data permanently, unlike variables that vanish when the program ends.") 
        input()

        print("\n\033[33mSTEP 1: Opening and Reading a File\033[0m\n")
        self.speaker.speak("Let's start with reading a file.")

        print("\033[32mPython provides the built-in open() function to work with files.\n\033[0m")
        input("Press ENTER to see an example...") 

      
        print("\nPython:")
        print("  with open('example.txt', 'r') as file:")
        print("      content = file.read()")
        print("      print(content)\n")

        self.speaker.speak("This opens a file named 'example.txt' in read mode and prints its contents.")
        input()

    
        print("\n\033[33mSTEP 2: Writing to a File\033[0m\n")
        self.speaker.speak("Now, let's learn how to write to a file.")

        print("\033[32mThe 'w' mode overwrites an existing file or creates a new one if it doesn’t exist.\n\033[0m")
        input()

        
        print("\nPython:")
        print("  with open('example.txt', 'w') as file:")
        print("      file.write('Hello, world!')\n")

        self.speaker.speak("This writes 'Hello, world!' to the file.")
        input()

       
        print("\n\033[33mSTEP 3: Appending to a File\033[0m\n")
        self.speaker.speak("What if we want to add data to a file instead of overwriting it?")

        print("\033[32mThe 'a' mode allows us to append data to an existing file.\n\033[0m")
        input()

        
        print("\nPython:")
        print("  with open('example.txt', 'a') as file:")
        print("      file.write('\\nNew line added!')\n")

        self.speaker.speak("This adds a new line to the file without erasing existing data.")
        input()

      
        print("\n\033[33mSUMMARY\033[0m\n")
        self.speaker.speak("Let's summarize what we learned.")

        print("\033[34mQuick Recap:\n"
              "  - 'r' mode is used to read files.\n"
              "  - 'w' mode is used to write (and overwrite) files.\n"
              "  - 'a' mode is used to append data to files.\033[0m\n")

        input("Press ENTER to continue...")

        print("\033[31mThat's it! Now, let's test your knowledge!\033[0m\n")
        self.speaker.speak("ok now i am going to ask a question from you ")

    def start_quiz8(self):
        
        
        self.speaker.speak("Which mode should you use to add new content to a file without deleting existing data?")
        
        print("\nWhich mode should you use to add new content to a file without deleting existing data?\n")
        print(" A) 'r'")
        print(" B) 'w'")  
        print(" C) 'a'") 
        print(" D) 'x'") 

        answer = input("\nEnter the correct answer (A/B/C/D): ").strip().upper()

       
        while answer not in ["A", "B", "C", "D"]:
            print("\n⚠️ Invalid choice. Please enter A, B, C, or D.")
            answer = input("\nEnter the correct answer (A/B/C/D): ").strip().upper()

        if answer == "C":
            print("\n✅ Great job! 'a' mode appends data to a file.")
            self.speaker.speak("Correct! You got it right!, so finnaly I think you getter better idea about basic programming concepts, so I think I touch you at my best, and good luck for your programming carrier, see you")
        else:
            print("\n❌ Incorrect! Try again.")
            self.speaker.speak("I think,  it is not the correct answer right. Give it another shot.")
            self.start_quiz8()  
