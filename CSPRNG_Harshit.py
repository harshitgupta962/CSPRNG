'''Author: Harshit gupta
   Date: 5/24/2016
   Version: 1.0 '''


import random
import sys
import os

def Value():
        try:
                number= eval(input ("Enter the number of random numbers you want to generate: "))
        except NameError:
                print("Invalid input. Integer is required")
                return 0
        else:
                if isinstance(number, int) is False or number<0:
                        print(" please enter positive integer only")
                        l=Value()
                        return (l)
                        print(l)
        return (number)
def Random(number, length, s, m, filename):
        calc=0
        
        print ("The list of random numbers generated is as follows")
        f=open(filename,"w")
        for v in range (number):                                            # number of random numbers required
                for t in range (2048):                                        # loop for bit to integer conversion
                        irand=random.randrange(0, length)                   # selecting random bits from the file
                        h=s[irand]
                        y=int (h)
                        calc=calc+(y*(2**t))
                m.append (calc)
                print ()
                print (m[v])
                f.write(str(m[v])+"\n")
        
kh=0

def increment():
        global kh
        kh=kh+1
        return kh
def main():
        
    
    filename = input("Enter the full path of the audio or image file you want to generate random numbers from: ")
    filename1 = input("Enter the full path of the output file to output random numbers into: ")
    op=increment()
    try:
        f1= open (filename , "rb")
        f2= open(filename1, "w")
        op=0
    except IOError as err:
        print("I/O error : {0}".format(err))
        print("Invalid path or file name")
        
        

    if op>=1 and op<4:
             main()
    elif op>=4:
              os._exit(0)
            
    else:
                number= Value()
                while True:
                        if number==0 :
                                number=Value()
                                if number!=0:
                                        break
                        else:
                                break
                data=f1.read()                                                      # read the file data 
                l=str(data)                                                         # to find the eof
                a= ' '.join(format(ord(x), 'b') for x in l)                         # generation of bits
                z=a.replace(" ", "")                                                # remove white spaces
                s=list()
                m=list()                                                            # declare list for random numbers
                s=z
                length =len(data)
                if number>5000:
                        print("please choose a smaller number")                     # this can be updated according to the need 
                        number=Value()
                        if number!=0:
                                Random(number, length, s, m)
                else:
                        Random(number, length, s, m, filename1)
main()
    
#D:/Users/HACK/Desktop/WINDOWS.jpg
