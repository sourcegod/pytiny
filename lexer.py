#!/usr/bin/python3
"""
    File: lexer.py
    Lexer for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Fri, 18/12/2020
"""
import enum
import sys

# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3

    # keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    # operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

#-------------------------------------------------------------------------------

# Token contains the original text and the type of token
class Token(object):
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText # the token's actual text
        self.kind = tokenKind # the token type

#-------------------------------------------------------------------------------

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
        sys.exit("Lexing error. " + message)

    # skip whitespace except newlines, which we will use to indicate the end of a statement
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    # Skip comment in the code
    def skipComment(self):
        pass

    # Returns the next token
    def getToken(self):
        tok = None
        self.skipWhitespace()
        # check the first character of this token
        if (self.curChar == '+'): 
            tok = Token(self.curChar, TokenType.PLUS) # plus token
        elif (self.curChar == '-'): 
            tok = Token(self.curChar, TokenType.MINUS) # minus token
        elif (self.curChar == '*'): 
            tok = Token(self.curChar, TokenType.ASTERISK) # Asterisk token
        elif (self.curChar == '/'): 
            tok = Token(self.curChar, TokenType.SLASH) # Slash token
        elif (self.curChar == '='): 
            # check whether this token is = or ==
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                tok = Token(lastChar + self.curChar, TokenType.EQEQ) 
            else:
                tok = Token(self.curChar, TokenType.EQ) 
        elif (self.curChar == '>'): 
            # check whether this token is > or >=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                tok = Token(lastChar + self.curChar, TokenType.GTEQ) 
            else:
                tok = Token(self.curChar, TokenType.GT) 
        elif (self.curChar == '<'): 
            # check whether this token is < or <=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                tok = Token(lastChar + self.curChar, TokenType.LTEQ) 
            else:
                tok = Token(self.curChar, TokenType.LT) 
        elif (self.curChar == '!'): 
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                tok = Token(lastChar + self.curChar, TokenType.NOTEQ) 
            else:
                self.abort("Expected !=, got !" + self.peek())

        elif (self.curChar == '\n'): 
            tok = Token(self.curChar, TokenType.NEWLINE) # newline token 
        elif (self.curChar == '\0'): 
            tok = Token(self.curChar, TokenType.EOF) # EOF token
        else:
            # Unknown token
            self.abort("Unknown token: " + self.curChar)
        
        self.nextChar()
        return tok

#-------------------------------------------------------------------------------
