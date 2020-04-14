#! /usr/share/env python3

import sys
from string import ascii_letters
import argparse


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_letters, start=1)} 

def alphabet_position(text):
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)

def getalphabet(val):
    for key, value in LETTERS.items():
        if val == value:
            return key

def encode(message,shift,fileName):
    new = []
    print("INPUT          :",message)
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
    correction(list(message),new,fileName)


def correction(input,code,fileName):
    for i in range(len(input)):
        if input[i].isupper():
            code[i]=code[i].upper()
        elif input[i].islower():
            code[i]=code[i].lower()
    code =''.join(code)    
    print("AFTER ENCODING :",code)
    
    if fileName != 'False':
        file = open(fileName,'a')
        file.write(code+'\n')
        file.close()    
        print("\n Output is saved to "+fileName)            


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--text",help="text to encode/decode inside quotation i.e 'TEXT'",required=True)
    parser.add_argument("-e","--encode",help="encode the text",action="store_true",default=True)
    parser.add_argument("-s","--shift",help="position to shift",type=int,required=True)
    parser.add_argument("-o","--filename",help="save decode text to a file",default=False)

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    encode(args.text,args.shift,str(args.filename))


if __name__ == "__main__":
    Main()




