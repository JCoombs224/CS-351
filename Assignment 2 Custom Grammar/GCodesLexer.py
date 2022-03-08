# Generated from c:\Users\Jamison\Google Drive\Spring 2022 Semester\CS 351\Asssignments\Assignment 2 Custom Grammar\GCodes.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\5\6!\n\6\3\6\6\6$\n\6\r\6\16\6%\3\6\3")
        buf.write("\6\6\6*\n\6\r\6\16\6+\5\6.\n\6\3\7\6\7\61\n\7\r\7\16\7")
        buf.write("\62\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\3\5\2\13")
        buf.write("\f\17\17\"\"\2:\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\23")
        buf.write("\3\2\2\2\7\27\3\2\2\2\t\31\3\2\2\2\13 \3\2\2\2\r\60\3")
        buf.write("\2\2\2\17\20\7I\2\2\20\21\7\62\2\2\21\22\7\63\2\2\22\4")
        buf.write("\3\2\2\2\23\24\7I\2\2\24\25\7\64\2\2\25\26\7:\2\2\26\6")
        buf.write("\3\2\2\2\27\30\7\\\2\2\30\b\3\2\2\2\31\32\7r\2\2\32\33")
        buf.write("\7t\2\2\33\34\7k\2\2\34\35\7p\2\2\35\36\7v\2\2\36\n\3")
        buf.write("\2\2\2\37!\7/\2\2 \37\3\2\2\2 !\3\2\2\2!#\3\2\2\2\"$\4")
        buf.write("\62;\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&-\3\2")
        buf.write("\2\2\')\7\60\2\2(*\4\62;\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,.\3\2\2\2-\'\3\2\2\2-.\3\2\2\2.\f\3\2\2\2")
        buf.write("/\61\t\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62")
        buf.write("\63\3\2\2\2\63\64\3\2\2\2\64\65\b\7\2\2\65\16\3\2\2\2")
        buf.write("\b\2 %+-\62\3\b\2\2")
        return buf.getvalue()


class GCodesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUMBER = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'G28'", "'Z'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "WS" ]

    grammarFileName = "GCodes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


