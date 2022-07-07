#Program randomly selects a student from a list of student names
#Designed to allow student to be selected up to two times per classmethod

import time, random

studentnamesglobal = ['John', 'Alice', 'Tim', 'Timothy', 'Julian', 'Roger', 'Jim', 'Pete', 'Peter'] #Global list of students



#GREETING AND INSTRUCTIONS

def greeting():
    print('RANDOM STUDENT PICKER\nStudents can be selected up to 2 times per day!\nType \'q\' to quit.\nGood Luck Everyone!\n\n')





def loadingscreen():                       #Loading screen function.

    print('Randomly selecting a student')  #Loading text
    time.sleep(1)
    print('Please Wait...')
    time.sleep(1)
    for i in range(6):                     #Builds a loading bar
        print('. ', end = ' ')
        time.sleep(.5)





def studentpicker():
    students = studentnamesglobal * 2 #Creates a local list with doubled student names

    greeting()  #prints greeting

    while True: #main loop for studentpicker function.
        print('Press \'ENTER\' to select a student')
        answer = input()
        if answer == 'q':
            print('Goodbye')
            break
        else:
            loadingscreen() #shows loading screen


            #selects a student randomly
            selection = random.choice(students)
            print('\n' + selection.upper() + '!!!')

            students.remove(selection) #removes student name from list

            #Tells student if they can still be selected again
            if selection in students:
                print(selection + ', you may still be selected one more time today')
            else:
                print('You will not be called on again today, ' + selection)
        continue

studentpicker()
