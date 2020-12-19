"""
    File: parser.py
    Parser script for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Sat, 19/12/2020
"""
from lexer import *

# Parser object keeps track of the current token and check whether the code matches the grammar.
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # call this twice to initialize the current and peek.

    # program ::= {statement}
    def program(self):
        print("PROGRAM")
        
        # Parse all the statements in the program.
        while not self.checkToken(TokenType.EOF):
            self.statement()

    # statement ::= "PRINT" (expression | string) nl
    # One of the following statements...
    def statement(self):
        # Check the first token to see what kind of statement this is.
        
        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # Simple string.
                self.nextToken()
            else:
                # expected expression
                self.expression()

        # newline
        self.nl()
    
    def nl(self):
        print("NEWLINE")

        # Require at least one newline.
        self.match(TokenType.NEWLINE)
        # But we will allow extra newlines too, of course.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

    # Returns true whether the current token matches
    def checkToken(self, kind):
        return kind == self.curToken .kind
   
    # returns true whether the next token matches
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # try to match current token
    def match(self, kind):
        if not self.curToken.kind:
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    # advance the current token
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.
        


    def abort(self, message):
        sys.exit("Parser error. " + message)

#-------------------------------------------------------------------------------
