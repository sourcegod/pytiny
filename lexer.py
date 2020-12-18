#!/usr/bin/python3
"""
    Lexer for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Fri, 18/12/2020
"""

class Lexer(object):
    def __init__(self, input):
        pass

    # process the next character
    def nextChar(self):
        pass

    # returns the lookahead character
    def  peek(self):
        pass

    # Invalid token found, print error message and exit
    def abort(self, message):
        pass

    # skip whitespace except newlines, which we will use to indicate the end of a statement
    def skipWhitespace(self):
        pass

    # Skip comment in the code
    def skipComment(self):
        pass

    # Returns the next token
    def getToken(self):
        pass

