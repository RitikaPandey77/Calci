#from line 27 to 68...there is definition of 1, 2, 3....9, 0, and '.'
#77-198 there is definition of addition multiplications...etc and their equations including % etc
#202 - 346 this is the button section of above operators...
#from 349  scientific calculator section
#
from math import *
from tkinter import *
k = 0;
fileName = "calculator.txt"
WRITE = 'w'
READ = 'r'
APPEND = 'a'
file = open(fileName, mode = WRITE)
file.close()

file = open(fileName, mode = APPEND)
data = ("Hey! Welcome to the History of your calculation." + "\n" + "-" * 50)
file.write(data)
file.close()

error = "Syntax Error"

a = Tk(className = "calculator")
# this is for input display
display = Entry(a, bd = 5, bg = 'lightgray', fg = 'black', justify = "right", relief = "solid")
display.grid(ipadx = 40, ipady = 15, columnspan = 10)
#must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky


###############################################
#I am gonna make text record
file = open(fileName, mode = APPEND)
# function for digits
def one():
    display.insert(END, 1)


def two():
    display.insert(END, 2)


def three():
    display.insert(END, 3)


def four():
    display.insert(END, 4)


def five():
    display.insert(END, 5)


def six():
    display.insert(END, 6)


def seven():
    display.insert(END, 7)


def eight():
    display.insert(END, 8)


def nine():
    display.insert(END, 9)


def zero():
    display.insert(END, 0)


def dec():
    display.insert(END, ".")


#################################
# for operators application

# for addition

try:
    def add():
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " + ")


    # for subtraction
    def sub():
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " - ")


    # for multiplication
    def mul():
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " * ")


    # for division
    def div():
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " / ")

    #for per oparator
    def per() :
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " % ")



    # for sign and unsign
    def sign():
        #there is bug
        display.insert(END, "-")
except ValueError:
    display.insert(error)

######################################
# definitions of equation

try:
    def eq():
        s = display.get()
        try :
            file = open(fileName, mode = APPEND)
            file.write("\n" + s)
            file.close()
        except UnicodeEncodeError :
            pass
        if (len(s) == 0):
            display.insert(END, "")
        elif (len(s) == 1): #if user gives only single value and press = then this will fix.
            display.delete(0, END)
            display.insert(END, s)
        else :
            s = display.get()
            s = s.split()
            if (s[1] == "+"):  # for addition
                try:
                    s = float(s[0]) + float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
            elif (s[1] == "-"):  # for division
                try:
                    s = float(s[0]) - float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
            elif (s[1] == "*"):  # for multiplication
                try:
                    s = float(s[0]) * float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == "/"):  # for division
                try:
                    s = float(s[0]) / float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ZeroDivisionError:
                    display.delete(0, END)
                    display.insert(0, "Cannot devide by zero")
            elif (s[1] == '%'):   #for percentage
                try:
                    if (len(s) == 0):
                        display.insert(END, "")
                    else:
                        s = float(s[0]) / 100
                        display.delete(0, END)
                        display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)

            ################################################scientific calc###################
            elif (s[1] == '!') : #for factorial
                try:
                    s = str(factorial(int(s[0])))
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, "Give a positive integer!")

            elif (s[0] == '√') : #for underRoot
                try:
                    s = pow((float(s[1])), 1/2) #there is a problem of incoding
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, "Imaginary Number!")

            elif (s[0] == 'sin(') : #for sin
                try:
                    a = (int(s[1])) * pi / 180
                    s = sin(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'cos(') : #for cos
                try:
                    a = (int(s[1])) * pi / 180
                    s = cos(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'tan(') : #for cos
                try:
                    a = (int(s[1])) * pi / 180
                    s = tan(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'ln(') : #for ln
                try:
                    a = (float(s[1]))
                    s = log(a) #here base is e
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'log(') : #for log
                try:
                    a = (float(s[1]))
                    s = log(a, 10) #here base is e
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == '1/'):   #for inverse
                try:
                    a = float(s[1])
                    s = 1/ a;
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)




            elif (s[0] == 'e^(') : #for exponential
                try:
                    a = (float(s[1]))
                    s = exp(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)


            elif (s[1] == '^2') : #for exponential
                try:
                    a = (float(s[0]))
                    s = pow(a, 2)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == '^') : #for x raised to the power n..
                try:
                    a = (float(s[2]))
                    s = pow(float(s[0]),a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == '^') : #for x raised to the power n..
                try:
                    a = (float(s[2]))
                    s = pow(float(s[0]),a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

           # elif (s[0] == 'pi'):   #for percentage
            #    try:
             #       s = pi
              #      display.delete(0, END)
               #     display.insert(0, str(s))
                #except IndexError:
                 #   display.delete(0, END)
                  #  display.insert(0, error)

            try:
                file = open(fileName, mode=APPEND)
                n = " = " + str(s) + '\n' + ('-' * 50)
                file.write(n)
                file.close()
            except UnicodeEncodeError:
                pass
except ValueError :
    display.delete(0, END)
    display.insert(0, error)
except IndexError:
    display.delete(0, END)
    display.insert(0, error)



##########################################
# button for digits
onE = Button(a, text = '1', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = one, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
onE.grid(row = 8, column = 0)

twO = Button(a, text = '2', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = two, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
twO.grid(row = 8, column = 1)

threE = Button(a, text = '3', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
               , command = three, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
threE.grid(row = 8, column = 2)

fouR = Button(a, text = '4', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = four, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
fouR.grid(row = 7, column = 0)

fivE = Button(a, text = '5', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = five, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
fivE.grid(row = 7, column = 1)

siX = Button(a, text = '6', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = six, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
siX.grid(row = 7, column = 2)

seveN = Button(a, text = '7' , activebackground = 'LawnGreen'
               , activeforeground = 'yellow',  bd = 15, bg = 'GoldenRod'
               , command = seven, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
seveN.grid(row = 6, column = 0)

eighT = Button(a, text = '8', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
               , command = eight, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
eighT.grid(row = 6, column = 1)

ninE = Button(a, text = '9', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = nine, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
ninE.grid(row = 6, column = 2)

zerO = Button(a,  text = '0', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = zero, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
zerO.grid(row = 9, column = 1)

deC = Button(a, text = '.', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = dec, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
deC.grid(row = 9, column = 0)

# this button for assigning the positive and negative value....
sigN = Button(a, text = '±', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = sign, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
sigN.grid(row = 9, column = 2)

##########################################
# button for operators
# for % operator
peR = Button(a, text = '%', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = per, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
peR.grid(row = 5, column = 2)
# button for +
plus = Button(a, text = '+', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = add, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
plus.grid(row = 8, column = 3)

# button for -
minus = Button(a, text = '-', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd =  15, bg = 'GoldenRod'
               , command = sub, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
minus.grid(row = 7, column = 3)

# button for *
multiply = Button(a, text = '*', activebackground = 'LawnGreen'
                  , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                  , command = mul, fg = 'Indigo', justify = 'center', relief = 'groove'
                  , state = "normal")
multiply.grid(row = 6, column = 3)

# button for /
divide = Button(a, text = '/', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = div, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
divide.grid(row = 5, column = 3)





# button for = 
equal = Button(a, text = ' = ', activebackground = 'green'
               , activeforeground = 'yellow', bd = 15, bg = 'red'
               , command = eq, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
equal.grid(row = 9, column = 3)


# clear the screen
def clear():
    display.delete(0, END)


reset = Button(a, text = 'C', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
               , command = clear, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
reset.grid(row = 5, column = 0)


# delete a value
def deleT():
    display.delete((display.index(1000)) - 1)
    #print (display.index(1000))


deletE = Button(a, text = '←', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = deleT, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
deletE.grid(row = 5, column = 1)

#now I am going to make this calc as scientific calclulator..
#############################
try:
    def braces():
        s = display.get()
        s = s.split()
        if (len(s) == 2) :
            display.insert(END, " )")
        else :
            display.insert(END, "")



    # for factorial
    def fact():
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " !")


    # for underRoot
    def underRoot():
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "√ ")
        else :
            display.insert(END, "")


    # def of sin
    def sine():
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "sin( ")
        else :
            display.insert(END, "")

    #for cos
    def cosine() :
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "cos( ")
        else :
            display.insert(END, "")

    def tangent(): #for tan
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "tan( ")
        else:
            display.insert(END, "")

    def loge(): #for log
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "log( ")
        else:
            display.insert(END, "")

    def lne(): #for ln
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "ln( ")
        else:
            display.insert(END, "")


    def inverse(): #for inverse
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            display.delete(0, END)
            display.insert(END, ("1/ %s" %s))

    def expo(): #for exponent
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "e^( ")
        else:
            display.insert(END, "")

    def sq(): #for square
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            display.insert(END, " ^2 ")
    def power(): #for power
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            display.insert(END, (" ^ "))

    def mod(): #for mod
        s = display.get()
        s = s.split()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            v = abs(float(s[0]))
            display.delete(0, END)
            display.insert(END, str(v))#incase of mode we use simple

    def pii(): #for pi
        s = display.get()
        if (len(s) == 0):
            display.insert(END, " 3.141592 ") #slution for symble
        else:
            display.insert(END, "")

    def ee(): #for e
        s = display.get()
        if (len(s) == 0):
            display.insert(END, " 2.71828 ")
        else:
            display.insert(END, "")


except ValueError:
    display.insert(error)



#########################################
#######################################

#for braces...#underconstruction
braceS = Button(a, text = '(  )', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = braces, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
braceS.grid(row = 5, column = 4)


#button for factorial
facT = Button(a, text = 'n!', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = fact, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
facT.grid(row = 5, column = 5)


#button for underRoot
undeR = Button(a, text = '√', activebackground = 'LawnGreen' # alt + 251
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = underRoot, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
undeR.grid(row = 5, column = 6)


##############################
#for sin
sinE = Button(a, text = 'sin', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = sine, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
sinE.grid(row = 6, column = 4)

#for cos
cosinE = Button(a, text = 'cos', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = cosine, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
cosinE.grid(row = 6, column = 5)

#for tan
taN = Button(a, text = 'tan', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = tangent, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
taN.grid(row = 6, column = 6)

#for log
loG = Button(a, text = 'log', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = loge, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
loG.grid(row = 7, column = 4)

#for ln
lN = Button(a, text = 'ln', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = lne, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
lN.grid(row = 7, column = 5)

#for inverse
inveR = Button(a, text = '1/x', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = inverse, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
inveR.grid(row = 7, column = 6)

#for exponent
exP = Button(a, text = 'eⁿ', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = expo, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
exP.grid(row = 8, column = 4)

#for square
#In this just click the button and it will give the square of target number
sQ = Button(a, text = 'x²', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = sq, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
sQ.grid(row = 8, column = 5)

#it's just give the x^n we can say...power
poweR = Button(a, text = 'xⁿ', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = power, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
poweR.grid(row = 8, column = 6)

#for mod
moD = Button(a, text = '|x|', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = mod, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
moD.grid(row = 9, column = 4)

#some constants
#for pi
pI = Button(a, text = 'π', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = pii, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
pI.grid(row = 9, column = 5)

#for expo
expO = Button(a, text = 'e', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = ee, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
expO.grid(row = 9, column = 6)
##########################################
a.mainloop()

file = open(fileName, mode = APPEND)
file.write(("\n" + "Thanks buddy\n" + "-"*50))
file.close()


