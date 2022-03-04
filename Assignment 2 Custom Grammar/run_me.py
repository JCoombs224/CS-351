import turtle
import time
from antlr4 import *

from turtleLexer import turtleLexer
from turtleParser import turtleParser
from turtleVisitor import turtleVisitor

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'turtle_tester')

def main():
    print("helloo world")
    lexer = turtleLexer( FileStream(filename))
    token_stream = CommonTokenStream(lexer)
    parser = turtleParser(token_stream)
    visitor = turtleVisitor()

    while True: 
        tree = parser.start()
        if tree.expr() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)

    time.sleep(2)


if __name__ == '__main__':
    main()
