from untwisted.event import Event
from untwisted.splits import Terminator
from re import findall, match, compile

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

class START_SESSION(Event):
    pass

class TELL(Event):
    pass

class SAY(Event):
    pass

class SHOUT(Event):
    pass

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
        
        if m: con.drive(*m)
        
        m = match(SESSION_REG, data)
        try:
            username = m.group('username')
        except:
            pass
        else:
            con.drive(START_SESSION, username)
    
        m = match(TELL_REG, data) 
        try:
            nick = m.group('nick')
            msg  = m.group('msg')
            mode = m.group('mode')
        except:
            pass
        else:
            con.drive(TELL, nick, mode, msg)
            con.drive('%s tells you:' % nick, mode, msg)
    
        m = match(SAY_REG, data)
        try:
            nick = m.group('nick')
            msg  = m.group('msg')
            mode = m.group('mode')
        except:
            pass
        else:
            con.drive(SAY, nick, mode, msg)
            con.drive('%s says:' % nick, mode, msg)
    
        m = match(SHOUT_REG, data)
        try:
            nick = m.group('nick')
            mode = m.group('mode')
            msg  = m.group('msg')
        except:
            pass
        else:
            con.drive(SHOUT, nick, mode, msg)
    

