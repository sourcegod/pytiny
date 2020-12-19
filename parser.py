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
        pass

    # Returns true whether the current token matches
    def checkToken(self, kind):
        return kind == self.curToken .kind
   
   # returns true whether the next token matches
   def checkPeek(self, kind):
       return kind == self.peekToken.kind

   # try to match current token
   def match(self, kind):
       pass


   # advance the current token
   def nextToken(self):
       pass

   def abort(self, message):
       sys.exit("Parser error. " + message)

#-------------------------------------------------------------------------------
