#!/usr/bin/env python3.6
import sys
import os
import click
import time

if sys.platform == 'win32':
    R = T = B = G = W = U = F = N = str()
    
else:
    R = '\033[1;31m'; T = '\033[1;33m'; B = '\033[1;34m'; G = '\033[1;32m'; W = '\033[1;37m'; U = '\033[1;4m'; F = '\033[1;7m'; N = '\033[0m'
    
# Box
some = str()


# English To Morse 
string_to_mors = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', ',': '--..--', '1': '.----', '.': '.-.-.-', '2': '..---', '?': '..--..', '3': '...--', ';': '-.-.-.', '4': '....-', ':': '---...', '5': '.....', "'": '.----.', '6': '-....', '-': '-....-', '7': '--...', '/': '-..-.', '8': '---..', '(': '-.--.-', '9': '----.', ')': '-.--.-', '_': '..--.-', ' ': ' ',    }

# Morse To English 
morse_to_string = { m:o for o, m in string_to_mors.items()}
            
# Encode To Mores Code 
def encode(*args, **kwargs):
    global some
    text = args[0]

    for tap in text.split():
        for string in tap:
            try:some += ' ' + string_to_mors[string]
            except: return None
                
        if tap[-1] == string:
            some += '  '

    return some

# Decode To English Language  
def decode(*args, **kwargs):
    global some
    morses = args[0]

    for morse in morses.split():
        try:some += morse_to_string[morse] + ' '
        except:return None

    return some

# Run audio
def go_play(text):
    try:
        from playsound import playsound
    except ImportError or Exception:
        print(f"{R}[!]{N} Error: Import playsound Model")
        return

    for Play in text.split():
            try:
                playsound(f'./ogg/{morse_to_string[Play]}.mp3')
            except Exception as e:
                print(f"{R}[!]{N} Error: play encode {morse_to_string[Play]}")
                continue
    

@click.command()
@click.option('-t', '--text',   type=str,   default=None,  help='English Language to Morse code')
@click.option('-m', '--morse',  type=str,   default=None,  help='Morse code to English Language.')
@click.option('-p', '--play',   type=bool, default=False, is_flag=True, help='Play the sound Morse code.')
@click.option('-s', '--nostyle',  type=bool,  default=False, is_flag=True, help='Canceling styles.')
def main(text, morse, play, nostyle):
    if not nostyle:
        print(f"""\t\t{T}{'#'*16}{T}\n\t\t{T}#{N} Morse Coding {T}#{N}\n\t\t{T}{'#'*16}{N}""")

    if text:
        en = encode(text.lower(), play)
        if en and not nostyle:
            print(f"{G}[+]{N} Text  : {text.lower()[0:30]}{ 'etc...' if len(text) > 30 else ''}\n{G}[+]{N} Play  : {True if play else False} \n{G}[+]{N} Encode: {en}")
        elif en:
            print(en)

        else:
            print(f"{R}[!]{N} Error For encoding")
            sys.exit(0)

        if play:
            print(f"{T}[*]{N} playsound Now")
            go_play(some)
                      
    elif morse:
        de = decode(morse)
        if de and not nostyle:
            print(f"{G}[+]{N} Morse : {morse[0:30]}{ ' etc...' if len(morse) > 30 else ''}\n{G}[+]{N} Play  : {True if play else False} \n{G}[+]{N} Decode: {de}")
        elif de:
            print(de)
        else:
            print(f"{R}[!]{N} Error For decoding")
            sys.exit(0)

        if play:
            print(f"{T}[*]{N} playsound Now")
            go_play(morse)

    else:
        print(f"\n{R}[!]{N} Error: Please Use {sys.argv[0]} --help")
    
    
if __name__ == "__main__":
    main()