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
    input = "+-123 9.8654  \"This is a string\" # This a comment!\n */"
    lex = Lexer(input)
    token = lex.getToken()
    
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lex.getToken()

main()
