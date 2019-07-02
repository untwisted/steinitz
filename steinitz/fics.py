from untwisted.network import spawn
from untwisted.event import get_event
from untwisted.splits import Terminator
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

class Fics:
    def __init__(self, con):
        self.con = con
        Terminator(con, b'\n\r')

        con.send_cmd = self.send_cmd
        con.add_map(Terminator.FOUND, self.tokenize)
    
    def send_cmd(self, cmd):
    
        cmd = cmd.encode('utf-8')
        self.con.dump(cmd)

    def tokenize(self, con, data):
        data = data.decode('utf-8')
        m = findall(GENERAL_REG, data)
        
        if m: spawn(con, *m)
        
        m = match(SESSION_REG, data)
        try:
            username = m.group('username')
        except:
            pass
        else:
            spawn(con, START_SESSION, username)
    
        m = match(TELL_REG, data) 
        try:
            nick = m.group('nick')
            msg  = m.group('msg')
            mode = m.group('mode')
        except:
            pass
        else:
            spawn(con, TELL, nick, mode, msg)
            spawn(con, '%s tells you:' % nick, mode, msg)
    
        m = match(SAY_REG, data)
        try:
            nick = m.group('nick')
            msg  = m.group('msg')
            mode = m.group('mode')
        except:
            pass
        else:
            spawn(con, SAY, nick, mode, msg)
            spawn(con, '%s says:' % nick, mode, msg)
    
        m = match(SHOUT_REG, data)
        try:
            nick = m.group('nick')
            mode = m.group('mode')
            msg  = m.group('msg')
        except:
            pass
        else:
            spawn(con, SHOUT, nick, mode, msg)
    

