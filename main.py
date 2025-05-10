from lesson1 import Lesson1
from lesson2 import Lesson2
from lesson3 import Lesson3
from lesson4 import Lesson4
from lesson5 import Lesson5
from lesson6 import Lesson6
from lesson7 import Lesson7
from lesson8 import Lesson8
from sound import Voice

def main():

    voice = Voice()

    print("                         \nStarting lesson 1\n")
    
    lesson1 = Lesson1()
    lesson1.start_lesson1()
    lesson1.start_quiz1()
      

    print("                        \nStarting lesson 2\n")
    
    lesson2 = Lesson2()
    lesson2.start_lesson2()
    lesson2.start_quiz2()

    print("                        \nStarting lesson 3\n")

    lesson3 = Lesson3()
    lesson3.start_lesson3()
    lesson3.start_quiz3()

    print("                        \nStarting lesson 4\n")

    lesson4 = Lesson4()
    lesson4.start_lesson4()
    lesson4.start_quiz4() 

    print("                        \nStarting lesson 5\n")

    lesson5 = Lesson5()
    lesson5.start_lesson5()
    lesson5.start_quiz5() 

    print("                        \nStarting lesson 6\n")

    lesson6 = Lesson6()
    lesson6.start_lesson6()
    lesson6.start_quiz6() 

    print("                        \nStarting lesson 7\n")

    lesson7 = Lesson7()
    lesson7.start_lesson7()
    lesson7.start_quiz7()

    print("                        \nStarting lesson 8\n")

    lesson8 = Lesson8()
    lesson8.start_lesson8()
    lesson8.start_quiz8()



if __name__ == "__main__":
    main()