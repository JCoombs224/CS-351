# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\GCodes.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GCodesParser import GCodesParser
else:
    from GCodesParser import GCodesParser

import turtle
skk = turtle.Turtle()

# This class defines a complete generic visitor for a parse tree produced by GCodesParser.

class GCodesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GCodesParser#start.
    def visitStart(self, ctx:GCodesParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:GCodesParser.DrawlineExprContext):
        target_x = int(ctx.x_cord.text)
        target_y = int(ctx.y_cord.text)
        cur_pos = skk.pos() 
        #if target_x > cur_pos[0]:
            #skk.right(target_x - cur_pos[0])
        #else:
        #    skk.left(cur_pos[0] - target_x)

        #if target_y > cur_pos[0]:
        #    skk.forward(target_y - cur_pos[0])
        #else:
        #    skk.backward(cur_pos[0] - target_y)
        skk.setpos(target_x, target_y)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#returnHomeExpr.
    def visitReturnHomeExpr(self, ctx:GCodesParser.ReturnHomeExprContext):
        skk.home()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#heightExpr.
    def visitHeightExpr(self, ctx:GCodesParser.HeightExprContext):
        skk.width(float(ctx.z_cord.text))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:GCodesParser.PrintlineExprContext):
        return self.visitChildren(ctx)



del GCodesParser