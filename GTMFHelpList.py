import discord

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

        if message.content.startswith('|help'):
            await message.channel.send('This is the help list {0.author.mention} \n musichelp - Shows the music commands \n giveaway <time> <prize> - makes a giveaway \n kick - kicks a user. \n ban - bans a user from the guild.'.format(message))

client = MyClient()
client.run('NzU3MTI1MTkzMDUwMDk1NzI3.X2b1yA.NoHXVzfQRbwjZZiiVXPBrNW2ngM')
