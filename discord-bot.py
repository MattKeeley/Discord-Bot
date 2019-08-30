import discord
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!help'):
            await message.channel.send('The doccumentation for this bot is located at XXX !')
        if message.content.startswith('!clone'):
            await message.channel.send('The temp text channel was created!  {0.author.mention}'.format(message))
            await message.channel.clone()
client = MyClient()
client.run()
