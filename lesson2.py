from sound import Voice

class Lesson2:

    def __init__(self):
        self.voice = Voice()

    def start_lesson2(self):
        self.voice.speak("Starting lesson two.")
        self.voice.speak("In this lesson, we will be learning about data types in programming.")

        self.voice.speak("In programming, data types specify what kind of value a variable can hold. This helps the program understand how to handle the data. "
                          "Each data type has different rules for the kind of value it stores.")
        print("THE SECOND LESSON IS ABOUT DATA TYPES IN PROGRAMMING\n")
        input("Press ENTER button to continue \n")

        print("WHAT DO YOU THINK ABOUT DATA TYPES?")
        self.voice.speak("What do you think about data types?")
        input("")

        print("In programming, data types specify what kind of value a variable can hold. This helps the program understand how to handle the data.\n"
              "Each data type has different rules for the kind of value it stores.\n")
        self.voice.speak("Let's go through the most common data types.")

        print("\033[33m THE MOST COMMON DATA TYPES \033[0m\n")

        print("\033[32m1. Integer (int):\n"
              "   - Used to store whole numbers, both positive and negative (e.g., 5, -3, 100).\n"
              "   - Example: age = 25\n")
        self.voice.speak("The first data type is Integer, used for storing whole numbers. Example: age equals 25.")
        input()

        print("\033[32m2. Float (float):\n"
              "   - Used to store decimal numbers (e.g., 3.14, -0.99, 100.5).\n"
              "   - Example: price = 19.99\n")
        self.voice.speak("The second data type is Float, used for storing decimal numbers. Example: price equals 19.99.")
        input()

        print("\033[32m3. Character (char):\n"
              "   - Stores a single character, like a letter or a symbol (e.g., 'A', 'b', '@').\n"
              "   - Example: grade = 'A'\n")
        self.voice.speak("The third data type is Character, used for storing a single character. Example: grade equals 'A'.")
        input()

        print("\033[32m4. String (str):\n"
              "   - Used to store text (e.g., 'Hello', 'Python').\n"
              "   - Example: name = 'Alice'\n")
        self.voice.speak("The fourth data type is String, used for storing text. Example: name equals 'Alice'.")
        input()

        print("\033[32m5. Boolean (bool):\n"
              "   - Used to store values of True or False, which are helpful for making decisions.\n"
              "   - Example: is_active = True\n")
        self.voice.speak("The fifth data type is Boolean, used for storing True or False values. Example: is_active equals True.")
        input()

        print("\033[33m HOW TO USE DATA TYPES WITH VARIABLES \033[0m\n")
        self.voice.speak("Next, let's look at how to use data types with variables.")

        print("\033[34mExamples:\n"
              "   * age = 25          # int\n"
              "   * price = 19.99     # float\n"
              "   * grade = 'A'       # char\n"
              "   * name = 'Alice'    # string\n"
              "   * is_active = True  # bool\n")
        input()

        print("\033[33m SUMMARY \033[0m\n")
        self.voice.speak("Now, let's review the key points from this lesson.")

        print("\033[34mKey Points:\n"
              "\n   * Every variable has a data type that defines the type of data it holds.\n"
              "   * Choosing the right data type is important for the program to function correctly.\n"
              "   * The most common data types are int, float, char, string, and bool.\n"
              "   * Data types help the program understand how to store and manipulate data.\n")
        input()
        
        print("\033[31m Okay, it’s your turn to answer the question!!!\033[0m\n")
        self.voice.speak("Okay, it’s your turn to answer the question!")

    def start_quiz2(self):
        self.voice.speak("What is the correct data type for the value 'True'?")
        
        print("\nWhat is the correct data type for the value 'True'? \n")
        print(" A) int")
        print(" B) string")
        print(" C) float")
        print(" D) bool")
        
        answer = input("\nEnter the correct answer (A/B/C/D): ").upper()

        if answer == "D":
            print("\n✅ Correct, now let's move to the next lesson.")
            self.voice.speak("Correct, now let's move to the next lesson.")
        else:
            print("\n❌ Incorrect answer! Try again.")
            self.voice.speak("Incorrect answer! Try again.")
            self.start_quiz2()
