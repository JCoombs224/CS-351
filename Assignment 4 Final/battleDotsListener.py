# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 4 Final\battleDots.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .battleDotsParser import battleDotsParser
else:
    from battleDotsParser import battleDotsParser

# This class defines a complete listener for a parse tree produced by battleDotsParser.
class battleDotsListener(ParseTreeListener):

    # Enter a parse tree produced by battleDotsParser#start.
    def enterStart(self, ctx:battleDotsParser.StartContext):
        pass

    # Exit a parse tree produced by battleDotsParser#start.
    def exitStart(self, ctx:battleDotsParser.StartContext):
        pass


    # Enter a parse tree produced by battleDotsParser#playerExpression.
    def enterPlayerExpression(self, ctx:battleDotsParser.PlayerExpressionContext):
        pass

    # Exit a parse tree produced by battleDotsParser#playerExpression.
    def exitPlayerExpression(self, ctx:battleDotsParser.PlayerExpressionContext):
        pass


    # Enter a parse tree produced by battleDotsParser#vsExpression.
    def enterVsExpression(self, ctx:battleDotsParser.VsExpressionContext):
        pass

    # Exit a parse tree produced by battleDotsParser#vsExpression.
    def exitVsExpression(self, ctx:battleDotsParser.VsExpressionContext):
        pass


    # Enter a parse tree produced by battleDotsParser#durationExpression.
    def enterDurationExpression(self, ctx:battleDotsParser.DurationExpressionContext):
        pass

    # Exit a parse tree produced by battleDotsParser#durationExpression.
    def exitDurationExpression(self, ctx:battleDotsParser.DurationExpressionContext):
        pass



del battleDotsParser