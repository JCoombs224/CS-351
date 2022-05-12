# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 4 Final\battleDots.g4 by ANTLR 4.8
import shutil
from antlr4 import *

import os
here = os.path.dirname(os.path.abspath(__file__))
playerLib = os.path.join(here, 'player_library')
activePlayers = os.path.join(here, 'players')

global duration

if __name__ is not None and "." in __name__:
    from .battleDotsParser import battleDotsParser
else:
    from battleDotsParser import battleDotsParser

# This class defines a complete generic visitor for a parse tree produced by battleDotsParser.

def copy_dir(src, dst, *, follow_sym=True):
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        if os.path.isdir(src):
            shutil.copyfile(src, dst, follow_symlinks=follow_sym)
            shutil.copystat(src, dst, follow_symlinks=follow_sym)
        return dst

class battleDotsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by battleDotsParser#start.
    def visitStart(self, ctx:battleDotsParser.StartContext):
        global duration
        duration = 0
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battleDotsParser#playerExpression.
    def visitPlayerExpression(self, ctx:battleDotsParser.PlayerExpressionContext):
        print(ctx.player_name.text)
        print(here)
        libPlayer = os.path.join(playerLib, ctx.player_name.text)
        newPlayer = os.path.join(activePlayers, ctx.player_name.text)

        print(libPlayer)
        shutil.copytree(libPlayer, newPlayer)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battleDotsParser#vsExpression.
    def visitVsExpression(self, ctx:battleDotsParser.VsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battleDotsParser#durationExpression.
    def visitDurationExpression(self, ctx:battleDotsParser.DurationExpressionContext):
        global duration
        duration = int(ctx.seconds.text)
        return ctx.seconds.text




del battleDotsParser