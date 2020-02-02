import discord
import os

class Bot(discord.Client):
    async def on_ready(self):
        print('{0.user} olarak giriş yapıldı!'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('.dev'):
            if 'Kurucu' in [role.name for role in message.author.roles]:
                member = message.mentions[0]
                await member.add_roles(discord.utils.get(message.guild.roles, name='Geliştirici'))
                await message.channel.send('**{member}** artık geliştirici!'.format(member=member.name))
            else:
                await message.channel.send('Üzgünüm, bu komutu kullanmak için yetkin yok. :pensive:')

        if message.content.startswith('.undev'):
            if 'Kurucu' in [role.name for role in message.author.roles]:
                member = message.mentions[0]
                await member.remove_roles(discord.utils.get(message.guild.roles, name='Geliştirici'))
                await message.channel.send('**{member}** geliştiricilikten çıkarıldı!'.format(member=member.name))
            else:
                await message.channel.send('Üzgünüm, bu komutu kullanmak için yetkin yok. :pensive:')

if __name__ == '__main__':
    bot = Bot()
    bot.run(str(os.environ.get('BOT_TOKEN')))
