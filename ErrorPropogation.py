import math
import sys

def main():

    #prompt for mode
    looper = True
    mode = ""
    while(looper):
        print("Mode (1 for multiplication | 2 for division | 0 to quit)")
        mode = input()

        try:
            mode = int(mode)
        except:
            print("Invalid mode")
            continue
        
        if (mode > 2):
            print("Invalid mode")
            continue

        if (mode == 0):
            sys.exit()

        #we prob got valid
        looper = False

    #get numbers
    looper = True
    number_one = 0
    number_one_un = 0
    while(looper):
        print("Enter number 1, press enter, then enter its uncertainty")
        try:
            number_one = float(input())
            print("±")
            number_one_un = float(input())
        except:
            print("Invalid input")
            continue
        looper = False
        print(f'%f ± %f' % (number_one, number_one_un))

    #get numbers
    looper = True
    number_two = 0
    number_two_un = 0
    while(looper):
        print("Enter number 2, press enter, then enter its uncertainty")
        try:
            number_two = float(input())
            print("±")
            number_two_un = float(input())
        except:
            print("Invalid input")
            continue
        looper = False
        print(f'%f ± %f' % (number_two, number_two_un))

    if (mode == 1):
        w = number_one * number_two
        delta_w = w * math.sqrt((number_one_un/number_one)**2 + (number_two_un/number_two)**2)
        print(f"(%f ± %f)*(%f ± %f) = %f ± %f" % (number_one, number_one_un, number_two, number_two_un, w, delta_w))

    elif (mode == 2):
        w = number_one / number_two
        delta_w = w * math.sqrt((number_one_un/number_one)**2 + (number_two_un/number_two)**2)
        print(f"(%f ± %f)*(%f ± %f) = %f ± %f" % (number_one, number_one_un, number_two, number_two_un, w, delta_w))
    
while(True):
    main()        
