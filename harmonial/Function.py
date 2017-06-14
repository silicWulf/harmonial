class Function:
    def __init__(self, function_type, params=None):
        self.function_type = function_type
        self.params = params
        self._function_code = ''

        #if self.params == '$argument':


        if self.function_type == 'say':
            self.params = '"' + self.params + '"'
            self._function_code = """    await bot.send_message(ctx.message.channel, """ + self.params + """)
"""
        elif self.function_type == 'writeFile':
            p = self.params.split('|||')
            if len(p) < 2:
                raise Exception("not enough arguments in 'params'")
            else:
                self._function_code = """    open('""" + p[0] + """').write('""" + p[1] + """')
"""