from untwisted.network import get_event, spawn
from untwisted.utils.shrug import FOUND
from re import *

GENERAL_STR = '[^ ]+' 
GENERAL_REG = compile(GENERAL_STR)
SESSION_STR = '\*\*\*\* Starting FICS session as (?P<username>.+) \*\*\*\*'
SESSION_REG = compile(SESSION_STR)
TELL_STR    = '(?P<nick>[a-zA-Z]+)(?P<mode>.*) tells you:(?P<msg>.+)'
TELL_REG    = compile(TELL_STR)
SAY_STR     = '(?P<nick>[a-zA-Z]+)(?P<mode>.*) says:(?P<msg>.+)'
SAY_REG     = compile(SAY_STR)
SHOUT_STR   = '(?P<nick>[a-zA-Z]+)(?P<mode>.*) shouts:(?P<msg>.+)'
SHOUT_REG   = compile(SHOUT_STR)

START_SESSION = get_event()
TELL          = get_event()
SAY           = get_event()
SHOUT         = get_event()

def install(spin):
    spin.link(FOUND, spliter)

def spliter(spin, data):
    m = findall(GENERAL_REG, data)
    
    if m: spawn(spin, *m)
    
    m = match(SESSION_REG, data)
    try:
        username = m.group('username')
    except:
        pass
    else:
        spawn(spin, START_SESSION, username)

    m = match(TELL_REG, data) 
    try:
        nick = m.group('nick')
        msg  = m.group('msg')
        mode = m.group('mode')
    except:
        pass
    else:
        spawn(spin, TELL, nick, mode, msg)
        spawn(spin, '%s tells you:' % nick, mode, msg)

    m = match(SAY_REG, data)
    try:
        nick = m.group('nick')
        msg  = m.group('msg')
        mode = m.group('mode')
    except:
        pass
    else:
        spawn(spin, SAY, nick, mode, msg)
        spawn(spin, '%s says:' % nick, mode, msg)

    m = match(SHOUT_REG, data)
    try:
        nick = m.group('nick')
        mode = m.group('mode')
        msg  = m.group('msg')
    except:
        pass
    else:
        spawn(spin, SHOUT, nick, mode, msg)













