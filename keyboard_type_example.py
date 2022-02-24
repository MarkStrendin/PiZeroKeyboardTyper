#!/usr/bin/env python3
import time
RELEASE_CHAR = chr(0)*8

def write_key(key):
        with open('/dev/hidg0', 'rb+') as fd:
                fd.write(key.encode())
                fd.write(RELEASE_CHAR.encode())

def translate_letter(letter):
        if letter == "a": return chr(0)*2+chr(4)+chr(0)*5
        if letter == "b": return chr(0)*2+chr(5)+chr(0)*5
        if letter == "c": return chr(0)*2+chr(6)+chr(0)*5
        if letter == "d": return chr(0)*2+chr(7)+chr(0)*5
        if letter == "e": return chr(0)*2+chr(8)+chr(0)*5
        if letter == "f": return chr(0)*2+chr(9)+chr(0)*5
        if letter == "g": return chr(0)*2+chr(10)+chr(0)*5
        if letter == "h": return chr(0)*2+chr(11)+chr(0)*5
        if letter == "i": return chr(0)*2+chr(12)+chr(0)*5
        if letter == "j": return chr(0)*2+chr(13)+chr(0)*5
        if letter == "k": return chr(0)*2+chr(14)+chr(0)*5
        if letter == "l": return chr(0)*2+chr(15)+chr(0)*5
        if letter == "m": return chr(0)*2+chr(16)+chr(0)*5
        if letter == "n": return chr(0)*2+chr(17)+chr(0)*5
        if letter == "o": return chr(0)*2+chr(18)+chr(0)*5
        if letter == "p": return chr(0)*2+chr(19)+chr(0)*5
        if letter == "q": return chr(0)*2+chr(20)+chr(0)*5
        if letter == "r": return chr(0)*2+chr(21)+chr(0)*5
        if letter == "s": return chr(0)*2+chr(22)+chr(0)*5
        if letter == "t": return chr(0)*2+chr(23)+chr(0)*5
        if letter == "u": return chr(0)*2+chr(24)+chr(0)*5
        if letter == "v": return chr(0)*2+chr(25)+chr(0)*5
        if letter == "w": return chr(0)*2+chr(26)+chr(0)*5
        if letter == "x": return chr(0)*2+chr(27)+chr(0)*5
        if letter == "y": return chr(0)*2+chr(28)+chr(0)*5
        if letter == "z": return chr(0)*2+chr(29)+chr(0)*5
        if letter == "A": return chr(32)+chr(0)*2+chr(4)+chr(0)*5
        if letter == "B": return chr(32)+chr(0)*2+chr(5)+chr(0)*5
        if letter == "C": return chr(32)+chr(0)*2+chr(6)+chr(0)*5
        if letter == "D": return chr(32)+chr(0)*2+chr(7)+chr(0)*5
        if letter == "E": return chr(32)+chr(0)*2+chr(8)+chr(0)*5
        if letter == "F": return chr(32)+chr(0)*2+chr(9)+chr(0)*5
        if letter == "G": return chr(32)+chr(0)*2+chr(10)+chr(0)*5
        if letter == "H": return chr(32)+chr(0)*2+chr(11)+chr(0)*5
        if letter == "I": return chr(32)+chr(0)*2+chr(12)+chr(0)*5
        if letter == "J": return chr(32)+chr(0)*2+chr(13)+chr(0)*5
        if letter == "K": return chr(32)+chr(0)*2+chr(14)+chr(0)*5
        if letter == "L": return chr(32)+chr(0)*2+chr(15)+chr(0)*5
        if letter == "M": return chr(32)+chr(0)*2+chr(16)+chr(0)*5
        if letter == "N": return chr(32)+chr(0)*2+chr(17)+chr(0)*5
        if letter == "O": return chr(32)+chr(0)*2+chr(18)+chr(0)*5
        if letter == "P": return chr(32)+chr(0)*2+chr(19)+chr(0)*5
        if letter == "Q": return chr(32)+chr(0)*2+chr(20)+chr(0)*5
        if letter == "R": return chr(32)+chr(0)*2+chr(21)+chr(0)*5
        if letter == "S": return chr(32)+chr(0)*2+chr(22)+chr(0)*5
        if letter == "T": return chr(32)+chr(0)*2+chr(23)+chr(0)*5
        if letter == "U": return chr(32)+chr(0)*2+chr(24)+chr(0)*5
        if letter == "V": return chr(32)+chr(0)*2+chr(25)+chr(0)*5
        if letter == "W": return chr(32)+chr(0)*2+chr(26)+chr(0)*5
        if letter == "X": return chr(32)+chr(0)*2+chr(27)+chr(0)*5
        if letter == "Y": return chr(32)+chr(0)*2+chr(28)+chr(0)*5
        if letter == "Z": return chr(32)+chr(0)*2+chr(29)+chr(0)*5
        if letter == " ": return chr(0)*2+chr(44)+chr(0)*5
        if letter == ".": return chr(0)*2+chr(55)+chr(0)*5
        if letter == ",": return chr(0)*2+chr(54)+chr(0)*5
        if letter == "/": return chr(0)*2+chr(56)+chr(0)*5
        if letter == ";": return chr(0)*2+chr(51)+chr(0)*5
        if letter == "'": return chr(0)*2+chr(52)+chr(0)*5
        if letter == " ": return chr(0)*2+chr(44)+chr(0)*5
        if letter == "[": return chr(0)*2+chr(47)+chr(0)*5
        if letter == "]": return chr(0)*2+chr(48)+chr(0)*5
        if letter == "\\": return chr(0)*2+chr(49)+chr(0)*5
        if letter == "`": return chr(0)*2+chr(53)+chr(0)*5
        if letter == "-": return chr(0)*2+chr(45)+chr(0)*5
        if letter == "=": return chr(0)*2+chr(46)+chr(0)*5
        if letter == "1": return chr(0)*2+chr(30)+chr(0)*5
        if letter == "2": return chr(0)*2+chr(31)+chr(0)*5
        if letter == "3": return chr(0)*2+chr(32)+chr(0)*5
        if letter == "4": return chr(0)*2+chr(33)+chr(0)*5
        if letter == "5": return chr(0)*2+chr(34)+chr(0)*5
        if letter == "6": return chr(0)*2+chr(35)+chr(0)*5
        if letter == "7": return chr(0)*2+chr(36)+chr(0)*5
        if letter == "8": return chr(0)*2+chr(37)+chr(0)*5
        if letter == "9": return chr(0)*2+chr(38)+chr(0)*5
        if letter == "0": return chr(0)*2+chr(39)+chr(0)*5
        if letter == ".": return chr(0)*2+chr(55)+chr(0)*5
        if letter == ",": return chr(0)*2+chr(54)+chr(0)*5
        if letter == "/": return chr(0)*2+chr(56)+chr(0)*5
        if letter == ";": return chr(0)*2+chr(51)+chr(0)*5
        if letter == "'": return chr(0)*2+chr(52)+chr(0)*5
        if letter == "\"": return chr(32)+chr(0)*2+chr(52)+chr(0)*5
        if letter == "{": return chr(32)+chr(0)*2+chr(47)+chr(0)*5
        if letter == "}": return chr(32)+chr(0)*2+chr(48)+chr(0)*5
        if letter == "|": return chr(32)+chr(0)*2+chr(49)+chr(0)*5
        if letter == "~": return chr(32)+chr(0)*2+chr(53)+chr(0)*5
        if letter == "_": return chr(32)+chr(0)*2+chr(45)+chr(0)*5
        if letter == "+": return chr(32)+chr(0)*2+chr(46)+chr(0)*5
        if letter == "!": return chr(32)+chr(0)*2+chr(30)+chr(0)*5
        if letter == "@": return chr(32)+chr(0)*2+chr(31)+chr(0)*5
        if letter == "#": return chr(32)+chr(0)*2+chr(32)+chr(0)*5
        if letter == "$": return chr(32)+chr(0)*2+chr(33)+chr(0)*5
        if letter == "%": return chr(32)+chr(0)*2+chr(34)+chr(0)*5
        if letter == "^": return chr(32)+chr(0)*2+chr(35)+chr(0)*5
        if letter == "&": return chr(32)+chr(0)*2+chr(36)+chr(0)*5
        if letter == "*": return chr(32)+chr(0)*2+chr(37)+chr(0)*5
        if letter == "(": return chr(32)+chr(0)*2+chr(38)+chr(0)*5
        if letter == ")": return chr(32)+chr(0)*2+chr(39)+chr(0)*5
        if letter == ">": return chr(32)+chr(0)*2+chr(55)+chr(0)*5
        if letter == "<": return chr(32)+chr(0)*2+chr(54)+chr(0)*5
        if letter == "?": return chr(32)+chr(0)*2+chr(56)+chr(0)*5
        if letter == ":": return chr(32)+chr(0)*2+chr(51)+chr(0)*5

        print("Letter not found: " + letter)
        return None

def send_keystroke(key):
        data = translate_letter(key)
        if data != None:
                write_key(data)

def send_phrase(phrase):
        for character in phrase:
                send_keystroke(character)
                time.sleep(0.05)

def send_enter():
        write_key(chr(0)*2+chr(40)+chr(0)*5)

def send_tab():
        write_key(chr(0)*2+chr(43)+chr(0)*5)

def send_phrase_with_enter(phrase):
        send_phrase(phrase)
        send_enter()

def send_phrase_with_tab(phrase):
        send_phrase(phrase)
        send_tab()

print("waiting 5 seconds...")
print("Focus the window on a text box or text editor now.")
time.sleep(5)

send_phrase_with_enter("The quick brown fox jumps over the lazy dog.")

quit()
