# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\turtle.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete listener for a parse tree produced by turtleParser.
class turtleListener(ParseTreeListener):

    # Enter a parse tree produced by turtleParser#start.
    def enterStart(self, ctx:turtleParser.StartContext):
        pass

    # Exit a parse tree produced by turtleParser#start.
    def exitStart(self, ctx:turtleParser.StartContext):
        pass


    # Enter a parse tree produced by turtleParser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by turtleParser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by turtleParser#printlineExpr.
    def enterPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        pass

    # Exit a parse tree produced by turtleParser#printlineExpr.
    def exitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        pass



del turtleParser