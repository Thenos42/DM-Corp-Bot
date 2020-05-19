from discord import *
import os
from discord.ext import commands
import pickle
import time
from options import *

#v1.1.0

client = commands.Bot(command_prefix = '.', help_command = None)


def timeLog():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime('[%d/%m/%Y %H:%M:%S]', named_tuple)
    return time_string

@client.event
async def on_ready():
    print (client.user.name)
    print (client.user.id)
    await client.change_presence(status=botStatus, activity=botActivity)
    print ('status : ' +  str(botStatus))
    print ('activity : ' + str(botActivity))
    print ('version : ' + str(version))
    print ('\n====== Bot is ready ======\n')
    logsFile = open ('logs.txt', 'a')
    logsFile.write(timeLog() + ' ===== Bot started =====')
    logsFile.close()



# ---------------------------------------------------------------------------- #
#                               Commandes de base                              #
# ---------------------------------------------------------------------------- #

@client.command()
async def ping(ctx):
    await ctx.send(f'> ***Pong ! {round(client.latency *1000)}ms***')

@client.command()
async def help(ctx):
    await ctx.send ('```py\n" Commandes disponnibles : "```')
    await cxt.send ()



@client.command()
async def report(ctx, someone, *raisons):
    await ctx.channel.purge(limit=1)
    nameAuthor = str(ctx.author.id)
    await ctx.send ('> ' + someone + ' a été report par <@' + nameAuthor + '> pour la raison : *{}*'.format(' '.join(raisons)))


# ---------------------------------------------------------------------------- #
#                                Commandes admin                               #
# ---------------------------------------------------------------------------- #

@client.command()
@commands.has_role(rAdmin)
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_role(rModération)
async def mute(ctx):
    Member = Guild.get_member(arg0)
    await Member.edit(roles.append('Mute'))



# ---------------------------------------------------------------------------- #
#                                     DEBUG                                    #
# ---------------------------------------------------------------------------- #



@client.event
async def on_command_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send ('```diff\n- Erreur : Arguments manquants```')
    else:
        if isinstance (error, commands.CommandNotFound):
            await ctx.send ('```diff\n- Erreur : Commande inconnue```')
        else:
            if isinstance (error, commands.CheckFailure):
                await ctx.send ('```diff\n- Erreur : Vous n\'avez pas la permissions de faire ça```')
            else:
                pass



client.run('NzAxNTIwNTQxNDU4MzY2NDk1.XsQXqQ.bC6BDjISRZduNTo7EtNRzd0cD2M')
