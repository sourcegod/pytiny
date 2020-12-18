#!/usr/bin/python3
"""
    File: lexer.py
    Lexer for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Fri, 18/12/2020
"""

class Lexer(object):
    def __init__(self, input):
        self.source = input + '\n' # source code to lex as string.
        self.curChar = '' # current character in the string.
        self.curPos = -1 # current position in the string
        self.nextChar()

    # process the next character
    def nextChar(self):
        self.curPos += 1 
        if self.curPos >= len(self.source):
            self.curChar = '\0' # eEOF
        else:
            self.curChar = self.source[self.curPos]

    # returns the lookahead character
    def  peek(self):
        if self.curPos +1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

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

