#!/usr/bin/python3
"""
    File: pytiny.py
    Main script for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Fri, 18/12/2020
"""


from lexer import *

def main():
    input = "let foobar = 123"
    lex = Lexer(input)
    
    while lex.peek() != '\0':
        print(lex.curChar)
        lex.nextChar()

main()
