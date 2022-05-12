# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 4 Final\battleDots.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\22\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\20\n\3\3\3\2\2\4\2\4\2\2\2\22\2\b\3\2\2\2\4\17")
        buf.write("\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2")
        buf.write("\2\t\3\3\2\2\2\n\13\7\3\2\2\13\20\7\7\2\2\f\20\7\4\2\2")
        buf.write("\r\16\7\5\2\2\16\20\7\6\2\2\17\n\3\2\2\2\17\f\3\2\2\2")
        buf.write("\17\r\3\2\2\2\20\5\3\2\2\2\4\b\17")
        return buf.getvalue()


class battleDotsParser ( Parser ):

    grammarFileName = "battleDots.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PLAYER'", "'vs'", "'duration'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "NAME", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INT=4
    NAME=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(battleDotsParser.ExprContext,0)


        def getRuleIndex(self):
            return battleDotsParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = battleDotsParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [battleDotsParser.T__0, battleDotsParser.T__1, battleDotsParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [battleDotsParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return battleDotsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DurationExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a battleDotsParser.ExprContext
            super().__init__(parser)
            self.seconds = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(battleDotsParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurationExpression" ):
                listener.enterDurationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurationExpression" ):
                listener.exitDurationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDurationExpression" ):
                return visitor.visitDurationExpression(self)
            else:
                return visitor.visitChildren(self)


    class PlayerExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a battleDotsParser.ExprContext
            super().__init__(parser)
            self.player_name = None # Token
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(battleDotsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerExpression" ):
                listener.enterPlayerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerExpression" ):
                listener.exitPlayerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayerExpression" ):
                return visitor.visitPlayerExpression(self)
            else:
                return visitor.visitChildren(self)


    class VsExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a battleDotsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVsExpression" ):
                listener.enterVsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVsExpression" ):
                listener.exitVsExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVsExpression" ):
                return visitor.visitVsExpression(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = battleDotsParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [battleDotsParser.T__0]:
                localctx = battleDotsParser.PlayerExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(battleDotsParser.T__0)
                self.state = 9
                localctx.player_name = self.match(battleDotsParser.NAME)
                pass
            elif token in [battleDotsParser.T__1]:
                localctx = battleDotsParser.VsExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.match(battleDotsParser.T__1)
                pass
            elif token in [battleDotsParser.T__2]:
                localctx = battleDotsParser.DurationExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 11
                self.match(battleDotsParser.T__2)
                self.state = 12
                localctx.seconds = self.match(battleDotsParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





