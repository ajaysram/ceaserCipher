#! /usr/share/env python3

import sys
from string import ascii_letters
import argparse

decodeFlag = False
decodeShift = 0

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_letters, start=1)} 

def alphabet_position(text):
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)

def getalphabet(val):
    for key, value in LETTERS.items():
        if val == value:
            return key

def encode(message,shift):
    new = []
    # print("INPUT          :",message)
    if int(shift) < 0 :
        shift = 26 + int(shift)    
    for letter in message:
        if letter.isalpha():
            pos = int(alphabet_position(letter))
            pos+=int(shift)
            if pos > 52:
                pos= pos%52
            new.append(getalphabet(str(pos)))
        else:
            new.append(letter)
    correction(list(message),new)


def correction(input,code):
    global decodeShift
    global decodeFlag
    for i in range(len(input)):
        if input[i].isupper():
            code[i]=code[i].upper()
        elif input[i].islower():
            code[i]=code[i].lower()
    code =''.join(code)
    input=''.join(input)
    if decodeFlag == True:
        print(decodeShift,'\t\t\t',code)
        decodeShift+=1
    else:
        print("BEFORE ENCODING :",input,"\nAFTER ENCODING  :",code)     
           

def decode(message):
    for i in range(27):
        encode(message,i)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--text",help="text to encode/decode inside quotation i.e 'TEXT'",required=True)
    parser.add_argument("-e","--encode",help="encode the text",action="store_true",default=True)
    parser.add_argument("-s","--shift",help="position to shift",type=int,default=0)
    parser.add_argument("-d","--decode",help="Bruteforce",action="store_true")

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if args.encode:
        encode(args.text,args.shift)
    
    if args.decode:  
        print("shift\t\t\toutput\t\t\t\n")    
        global decodeFlag
        decodeFlag = True  
        decode(args.text)
    
    if args.shift == False and decodeFlag == False:
        print("No shift is given,swtching to default value of 0")


if __name__ == "__main__":
    Main()