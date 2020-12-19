#!/usr/bin/python3
"""
    File: pytiny.py
    Main script for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Fri, 18/12/2020
"""

from lexer import *
from emitter import *
from parser import *
import sys

def main():
    print("Pytiny Compiler")
    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
    
    # input = "IF+-123 foo*THEN/"
    # Initialize the lexer
    lex = Lexer(input)
    emit = Emitter("out.c")
    parse = Parser(lex, emit)

    parse.program() # starts the parser
    emit.writeFile() # write the output to file
    print("Compiling completed.")


main()
