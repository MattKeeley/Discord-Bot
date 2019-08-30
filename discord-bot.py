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
            await message.channel.send('The doccumentation for this bot is located at https://github.com/MattKeeley/Discord-Bot !')
        if message.content.startswith('!ctemp'):
            await message.channel.send('The temp channel was cleared!  {0.author.mention}'.format(message))
            await message.channel.clone(name="temp")
            await message.channel.delete()

client = MyClient()
client.run()
