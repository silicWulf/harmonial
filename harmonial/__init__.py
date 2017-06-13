import random
from .Function import Function
from .Command import Command
#from .LoginInfo import LoginInfo

def build(filename, prefix, commands):
    open(filename, 'w').close()
    f = open(filename, 'a')
    sss = """import discord, aiohttp, asyncio; from discord.ext.commands import Bot
bot = Bot('""" + prefix + """', pm_help=False)

"""
    f.write(sss)
    for command in commands:
        f.write(command._command_code)
    f.write("bot.run('TOKEN HERE')")
    f.close()

def special(special_type, params=None):
    if type(special_type) == str:
        if special_type == 'randomNumber':
            if type(params) == tuple:
                return random.choice(range(params[0], params[1]))
            else:
                raise ValueError("'params' must be a tuple when using the 'randomNumber' function")

        elif special_type == 'contentsOf':
            if type(params) != str:
                raise ValueError("'params' must be a string when using the 'contentsOf' function")
            else:
                try:
                    return open(params, 'r').read()
                except FileNotFoundError:
                    raise FileNotFoundError("file not found at '" + params + "'")

    else: return ''