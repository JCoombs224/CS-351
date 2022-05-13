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
        buf.write("\25\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\5\3\f\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3\23\n\3\3\3\2\2\4\2\4\2\2\2\25\2")
        buf.write("\b\3\2\2\2\4\22\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6\3")
        buf.write("\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\f\7\7\2\2\13\n\3\2\2")
        buf.write("\2\13\f\3\2\2\2\f\r\3\2\2\2\r\16\7\3\2\2\16\23\7\7\2\2")
        buf.write("\17\20\7\4\2\2\20\21\7\6\2\2\21\23\7\5\2\2\22\13\3\2\2")
        buf.write("\2\22\17\3\2\2\2\23\5\3\2\2\2\5\b\13\22")
        return buf.getvalue()


class battleDotsParser ( Parser ):

    grammarFileName = "battleDots.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'vs'", "'duration'", "'->'" ]

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
            if token in [battleDotsParser.T__0, battleDotsParser.T__1, battleDotsParser.NAME]:
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
            self.time = None # Token
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


    class VsExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a battleDotsParser.ExprContext
            super().__init__(parser)
            self.name1 = None # Token
            self.name2 = None # Token
            self.copyFrom(ctx)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(battleDotsParser.NAME)
            else:
                return self.getToken(battleDotsParser.NAME, i)

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
        self._la = 0 # Token type
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [battleDotsParser.T__0, battleDotsParser.NAME]:
                localctx = battleDotsParser.VsExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==battleDotsParser.NAME:
                    self.state = 8
                    localctx.name1 = self.match(battleDotsParser.NAME)


                self.state = 11
                self.match(battleDotsParser.T__0)
                self.state = 12
                localctx.name2 = self.match(battleDotsParser.NAME)
                pass
            elif token in [battleDotsParser.T__1]:
                localctx = battleDotsParser.DurationExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(battleDotsParser.T__1)
                self.state = 14
                localctx.time = self.match(battleDotsParser.INT)
                self.state = 15
                self.match(battleDotsParser.T__2)
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





