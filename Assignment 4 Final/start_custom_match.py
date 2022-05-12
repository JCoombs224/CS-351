from antlr4 import *
from subprocess import call, TimeoutExpired

from battleDotsLexer import battleDotsLexer
from battleDotsParser import battleDotsParser
from battleDotsVisitor import battleDotsVisitor

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'playerconfig')
activePlayers = os.path.join(here, 'players')
os.chdir(here)

def main():
    lexer = battleDotsLexer( FileStream(filename))
    token_stream = CommonTokenStream(lexer)
    parser = battleDotsParser(token_stream)
    visitor = battleDotsVisitor()

    os.system('rmdir /S /Q "{}"'.format(activePlayers)) #remove active players
    
    while True: 
        tree = parser.start()
        if tree.expr() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)


    from battleDotsVisitor import duration

    print(f"Duration: {duration}")
    
    if duration > 0:
        try:
            call('py run_me.py', timeout = duration)
        except TimeoutExpired as e:
            print('Time limit exceeded, terminating..')
    else:
        os.system('py run_me.py')



if __name__ == '__main__':
    main()
