# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\turtle.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete generic visitor for a parse tree produced by turtleParser.

import turtle
skk = turtle.Turtle()

class turtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        target_x = int(ctx.x_cord.text)
        target_y = int(ctx.y_cord.text)
        cur_pos = skk.pos() 
        if target_x > cur_pos[0]:
            skk.right(target_x - cur_pos[0])
        else:
            skk.left(cur_pos[0] - target_x)

        if target_y > cur_pos[0]:
            skk.forward(target_y - cur_pos[0])
        else:
            skk.backward(cur_pos[0] - target_y)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        print(f"Draw line to x={ctx.x_cord.text} y={ctx.y_cord.text}")
        return self.visitChildren(ctx)



del turtleParser