# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\GCodes.g4 by ANTLR 4.8
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
        buf.write("\26\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\24\n\3\3\3\2\2\4\2\4\2\2\2\27")
        buf.write("\2\b\3\2\2\2\4\23\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6")
        buf.write("\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13\f\7\7")
        buf.write("\2\2\f\24\7\7\2\2\r\24\7\4\2\2\16\17\7\5\2\2\17\24\7\7")
        buf.write("\2\2\20\21\7\6\2\2\21\22\7\7\2\2\22\24\7\7\2\2\23\n\3")
        buf.write("\2\2\2\23\r\3\2\2\2\23\16\3\2\2\2\23\20\3\2\2\2\24\5\3")
        buf.write("\2\2\2\4\b\23")
        return buf.getvalue()


class GCodesParser ( Parser ):

    grammarFileName = "GCodes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'G28'", "'Z'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
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
            return self.getTypedRuleContext(GCodesParser.ExprContext,0)


        def getRuleIndex(self):
            return GCodesParser.RULE_start

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

        localctx = GCodesParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GCodesParser.T__0, GCodesParser.T__1, GCodesParser.T__2, GCodesParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [GCodesParser.EOF]:
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
            return GCodesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeightExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.z_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(GCodesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeightExpr" ):
                listener.enterHeightExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeightExpr" ):
                listener.exitHeightExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeightExpr" ):
                return visitor.visitHeightExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrintlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GCodesParser.NUMBER)
            else:
                return self.getToken(GCodesParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlineExpr" ):
                listener.enterPrintlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlineExpr" ):
                listener.exitPrintlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlineExpr" ):
                return visitor.visitPrintlineExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReturnHomeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnHomeExpr" ):
                listener.enterReturnHomeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnHomeExpr" ):
                listener.exitReturnHomeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnHomeExpr" ):
                return visitor.visitReturnHomeExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GCodesParser.NUMBER)
            else:
                return self.getToken(GCodesParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawlineExpr" ):
                listener.enterDrawlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawlineExpr" ):
                listener.exitDrawlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawlineExpr" ):
                return visitor.visitDrawlineExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = GCodesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GCodesParser.T__0]:
                localctx = GCodesParser.DrawlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(GCodesParser.T__0)
                self.state = 9
                localctx.x_cord = self.match(GCodesParser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(GCodesParser.NUMBER)
                pass
            elif token in [GCodesParser.T__1]:
                localctx = GCodesParser.ReturnHomeExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(GCodesParser.T__1)
                pass
            elif token in [GCodesParser.T__2]:
                localctx = GCodesParser.HeightExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(GCodesParser.T__2)
                self.state = 13
                localctx.z_cord = self.match(GCodesParser.NUMBER)
                pass
            elif token in [GCodesParser.T__3]:
                localctx = GCodesParser.PrintlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 14
                self.match(GCodesParser.T__3)
                self.state = 15
                localctx.x_cord = self.match(GCodesParser.NUMBER)
                self.state = 16
                localctx.y_cord = self.match(GCodesParser.NUMBER)
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





