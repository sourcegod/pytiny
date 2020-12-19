#!/usr/bin/python3
"""
    File: pytiny.py
    Main script for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Fri, 18/12/2020
"""

from lexer import *
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
    parse = Parser(lex)

    parse.program() # starts the parser

    print("Parsing completed.")


main()
