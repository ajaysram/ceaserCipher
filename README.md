# Ceaser cipher
## What is ceaser cipher ?
Ceaser cipher is one of the earliest known simple cipher. It is basically a substitution cipher named after [Julius Ceaser]("https://en.wikipedia.org/wiki/Julius_Caesar").
## What does it do ?
As said before it is a substitution cipher . The plain text is shifted by some shift value. 

```python

    input  : ABC
    shift  : 1
    output : BCD
``` 

## Where is it used ?
Almost every modern cryptography methods got evolved from this cipher.
And even exams contain questions based on ceaser cipher.Some **Capture the Flag** events host such questions for warm-up levels. 

## Prerequisites
* Python3

## How to use this script
* Download the file as zip or you can use git clone to get the script
* Run python3 ceaser.py
## Usage
```
usage: ceaser.py [-h] -t TEXT [-e] -s SHIFT [-o FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  text to encode/decode inside quotation i.e 'TEXT'
  -e, --encode          encode the text
  -s SHIFT, --shift SHIFT
                        position to shift
  -o FILENAME, --filename FILENAME
                        save decode text to a file

```