# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 4 Final\battleDots.g4 by ANTLR 4.8
from antlr4 import *
import shutil

import os
here = os.path.dirname(os.path.abspath(__file__))
playerLib = os.path.join(here, 'player_library')
activePlayers = os.path.join(here, 'players')

global duration
duration = 0

if __name__ is not None and "." in __name__:
    from .battleDotsParser import battleDotsParser
else:
    from battleDotsParser import battleDotsParser

# This class defines a complete generic visitor for a parse tree produced by battleDotsParser.

class battleDotsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by battleDotsParser#start.
    def visitStart(self, ctx:battleDotsParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battleDotsParser#vsExpression.
    def visitVsExpression(self, ctx:battleDotsParser.VsExpressionContext):
        if ctx.name1 != None:
            player1 = ctx.name1.text
            libPlayer1 = os.path.join(playerLib, player1)
            newPlayer1 = os.path.join(activePlayers, player1)
            shutil.copytree(libPlayer1, newPlayer1)


        player2 = ctx.name2.text
        libPlayer2 = os.path.join(playerLib, player2)
        newPlayer2 = os.path.join(activePlayers, player2)            
        shutil.copytree(libPlayer2, newPlayer2)
        

        return self.visitChildren(ctx)


    # Visit a parse tree produced by battleDotsParser#durationExpression.
    def visitDurationExpression(self, ctx:battleDotsParser.DurationExpressionContext):
        global duration
        duration = int(ctx.time.text)
        print(duration)
        return duration



del battleDotsParser