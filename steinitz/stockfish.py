from untwisted.network import spawn
from untwisted.event import get_event
from untwisted.splits import Terminator
from re import compile, search, DOTALL

PATTERN_STR =  'bestmove (?P<move>[^\n ]+)'
PATTERN_RE  = compile(PATTERN_STR, DOTALL)
BESTMOVE    = get_event()

def install(expect):
    expect.add_map(Terminator.FOUND, spliter)

def spliter(expect, data):
    field = search(PATTERN_RE, data) 
    if field: spawn(expect, BESTMOVE, field.group('move'))

