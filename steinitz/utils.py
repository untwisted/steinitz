import re

def make(x1, flip):
    if not flip:
        return 9 - (x1 + 1)
    else:
        return x1 + 1

def over(flip):
    alphabet = 'abcdefgh'
    if flip:
        return list(reversed(alphabet))
    else:
        return alphabet

def algebraic(cx, cy, flip):
    alphabet = over(flip)
    x1, y1 = cx
    x2, y2 = cy
  
    coordx = '%s%s' % (alphabet[y1], make(x1, flip))
    coordy = '%s%s' % (alphabet[y2], make(x2, flip))

    return '%s%s\n\r' % (coordx, coordy) 

def setup(x, y, color):
    """ This function determines the color of a square. 
        based on the (x, y) coordinate and color tuple.. 
    """
    # I couldnt think of a cool name.
    odd = lambda x: x % 2

    # Just for cleaness.
    xcolor, ycolor = color

    if odd(x) == odd(y): 
        return xcolor
     
    return ycolor

def side(coord, flip):
    x, y = coord

    if flip:
       return (8-(x+1), 8-(y + 1))
    else:
       return coord

def fenstring(state):
    content = '/'.join(state[:8])
    def beta(obj):
        return str(len(obj.group(0)))

    content = re.sub('-+', beta, content)
    flag=''

    if int(state[10]):
        flag = flag + 'K'
    if int(state[11]):
        flag = flag + 'Q'
    if int(state[12]):
        flag = flag + 'k'
    if int(state[13]):
        flag = flag + 'q'

    content = 'position fen %s %s %s' % (content, state[8].lower(), flag)
    print('flag', flag)
    return content

def init():
    from os.path import exists
    
    if not exists(dir):
        pass    

def rsc(*args):
    from os.path import join, dirname
    return join(dirname(__file__), *args)


def stockfish(state, depth=20, path='stockfish'):
    from subprocess import Popen, PIPE
    from re import compile, search, DOTALL

    PATTERN_STR =  'bestmove (?P<move>[^\n ]+)'
    PATTERN_RE  = compile(PATTERN_STR, DOTALL)
    
    pipe        = Popen([path], stdin=PIPE, stdout=PIPE)
    fen         = fenstring(state)
    print(fen)
    pipe.stdin.write('isready\n')
    pipe.stdin.write('%s\n' % fen)
    pipe.stdin.write('go depth %s\n'  % depth)
    import time
    time.sleep(5)
    pipe.stdin.close()

    data  = pipe.stdout.read()
    field = search(PATTERN_RE, data) 
    move  = field.group('move')
    return move







