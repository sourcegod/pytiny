"""
    File: emitter.py
    Emitter script for pytiny compiler.
    Inspired from Teeny Tiny Compiler
    Author: Coolbrother
    Date: Sat, 19/12/2020
"""

# Emitter object keeps track of the generated code and outputs it.
class Emitter(object):
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.header = ""
        self.code = ""

    def headerLine(self, code):
        self.header += code  + '\n'

    def emit(self, code):
        self.code += code 

    def emitLine(self, code):
        self.code +=code + '\n'

    def writeFile(self):
        with open(self.fullPath, 'w') as outputFile:
            outputFile.write(self.header + self.code)

#-------------------------------------------------------------------------------
