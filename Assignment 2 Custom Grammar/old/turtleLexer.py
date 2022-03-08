# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\turtle.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write(",\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\6\4\32\n\4\r")
        buf.write("\4\16\4\33\3\4\3\4\6\4 \n\4\r\4\16\4!\5\4$\n\4\3\5\6\5")
        buf.write("\'\n\5\r\5\16\5(\3\5\3\5\2\2\6\3\3\5\4\7\5\t\6\3\2\3\5")
        buf.write("\2\13\f\17\17\"\"\2/\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\3\13\3\2\2\2\5\22\3\2\2\2\7\31\3\2\2\2")
        buf.write("\t&\3\2\2\2\13\f\7v\2\2\f\r\7w\2\2\r\16\7t\2\2\16\17\7")
        buf.write("v\2\2\17\20\7n\2\2\20\21\7g\2\2\21\4\3\2\2\2\22\23\7r")
        buf.write("\2\2\23\24\7t\2\2\24\25\7k\2\2\25\26\7p\2\2\26\27\7v\2")
        buf.write("\2\27\6\3\2\2\2\30\32\4\62;\2\31\30\3\2\2\2\32\33\3\2")
        buf.write("\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34#\3\2\2\2\35\37\7\60")
        buf.write("\2\2\36 \4\62;\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!")
        buf.write("\"\3\2\2\2\"$\3\2\2\2#\35\3\2\2\2#$\3\2\2\2$\b\3\2\2\2")
        buf.write("%\'\t\2\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)")
        buf.write("*\3\2\2\2*+\b\5\2\2+\n\3\2\2\2\7\2\33!#(\3\b\2\2")
        return buf.getvalue()


class turtleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'turtle'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "WS" ]

    grammarFileName = "turtle.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


