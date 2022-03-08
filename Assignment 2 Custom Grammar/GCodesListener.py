# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\GCodes.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GCodesParser import GCodesParser
else:
    from GCodesParser import GCodesParser

# This class defines a complete listener for a parse tree produced by GCodesParser.
class GCodesListener(ParseTreeListener):

    # Enter a parse tree produced by GCodesParser#start.
    def enterStart(self, ctx:GCodesParser.StartContext):
        pass

    # Exit a parse tree produced by GCodesParser#start.
    def exitStart(self, ctx:GCodesParser.StartContext):
        pass


    # Enter a parse tree produced by GCodesParser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:GCodesParser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:GCodesParser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#returnHomeExpr.
    def enterReturnHomeExpr(self, ctx:GCodesParser.ReturnHomeExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#returnHomeExpr.
    def exitReturnHomeExpr(self, ctx:GCodesParser.ReturnHomeExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#heightExpr.
    def enterHeightExpr(self, ctx:GCodesParser.HeightExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#heightExpr.
    def exitHeightExpr(self, ctx:GCodesParser.HeightExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#printlineExpr.
    def enterPrintlineExpr(self, ctx:GCodesParser.PrintlineExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#printlineExpr.
    def exitPrintlineExpr(self, ctx:GCodesParser.PrintlineExprContext):
        pass



del GCodesParser