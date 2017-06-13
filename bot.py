import discord, aiohttp, asyncio; from discord.ext.commands import Bot
bot = Bot('!!!', pm_help=False)

@bot.command(pass_context=True)
async def test(ctx):
    await bot.send_message(ctx.message.channel, "test message!")
@bot.command(pass_context=True)
async def write(ctx):
    open('file.txt').write('fuck you')
bot.run('TOKEN HERE')