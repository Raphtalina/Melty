import discord
from discord.ext import commands
import os

import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lol(self, ctx, champ):
        url = "https://u.gg/lol/champions/{cha}/build".format(cha=champ.lower())
        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')

        response = requests.get('https://discordjs.guide/assets/img/2vsIPEP.3f295fd2.png')
        img = Image.open(BytesIO(response.content))

        championIcon = Image.open(BytesIO(requests.get(soup.find('img', class_='champion-image').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championPrimaryPerk1 = Image.open(BytesIO(requests.get(soup.find('div', class_='primary-perk keystones path-keystones').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championPrimaryPerk2 = Image.open(BytesIO(requests.get(soup.find('div', class_='primary-perk perks path-perk-1').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championPrimaryPerk3 = Image.open(BytesIO(requests.get(soup.find('div', class_='primary-perk perks path-perk-2').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championPrimaryPerk4 = Image.open(BytesIO(requests.get(soup.find('div', class_='primary-perk perks path-perk-3').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        try:
            championSecondaryPerk1 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-1').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        except:
            championSecondaryPerk2 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-2').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
            championSecondaryPerk3 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-3').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        try:
            championSecondaryPerk2 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-2').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        except:
            championSecondaryPerk1 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-1').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
            championSecondaryPerk3 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-3').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        try:
            championSecondaryPerk3 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-3').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        except:
            championSecondaryPerk1 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-1').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
            championSecondaryPerk2 = Image.open(BytesIO(requests.get(soup.find('div', class_='perks path-perk-2').find('div', class_='perk perk-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championSpells = soup.find('div', class_='grid-block summoner-spells').find('div', class_='grid-block-content').find_all('div', class_='image-wrapper')
        championShards = soup.find('div', class_='stat-shards-container').find_all('div', class_='shards')

        spells = []
        for spell in championSpells:
            spells.append(spell)

        shards = []
        for shard in championShards:
            shards.append(shard)

        championSpell1 = Image.open(BytesIO(requests.get(spells[0].find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championSpell2 = Image.open(BytesIO(requests.get(spells[1].find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championShard1 = Image.open(BytesIO(requests.get(shards[0].find('div', class_='shard shard-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championShard2 = Image.open(BytesIO(requests.get(shards[1].find('div', class_='shard shard-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)
        championShard3 = Image.open(BytesIO(requests.get(shards[2].find('div', class_='shard shard-active').find('img').get('src')).content)).resize((48, 48), Image.ANTIALIAS)

        championName = soup.find('span', class_='champion-name')
        championWinRate = soup.find('div', class_='value')
        championBanRate = soup.find('div', class_='ban-rate').find('div', class_='value')
        championPickRate = soup.find('div', class_='pick-rate').find('div', class_='value')

        ImageDraw.Draw(img).text((80, 31), championName.text + '        Kazanma: ' + championWinRate.text + '        Banlanma: ' + championBanRate.text + '        Seçilme: ' + championPickRate.text, (255, 255, 255), font=ImageFont.truetype("arial.ttf", 16))

        back_im = img.copy()
        back_im.paste(championIcon, (16, 16))
        back_im.paste(championPrimaryPerk1, (16, 80), championPrimaryPerk1)
        back_im.paste(championPrimaryPerk2, (80, 80), championPrimaryPerk2)
        back_im.paste(championPrimaryPerk3, (144, 80), championPrimaryPerk3)
        back_im.paste(championPrimaryPerk4, (208, 80), championPrimaryPerk4)
        try:
            back_im.paste(championSecondaryPerk1, (272, 80), championSecondaryPerk1)
        except:
            back_im.paste(championSecondaryPerk2, (336, 80), championSecondaryPerk2)
            back_im.paste(championSecondaryPerk3, (400, 80), championSecondaryPerk3)
        try:
            back_im.paste(championSecondaryPerk2, (336, 80), championSecondaryPerk2)
        except:
            back_im.paste(championSecondaryPerk1, (272, 80), championSecondaryPerk1)
            back_im.paste(championSecondaryPerk3, (400, 80), championSecondaryPerk3)
        try:
            back_im.paste(championSecondaryPerk3, (400, 80), championSecondaryPerk3)
        except:
            back_im.paste(championSecondaryPerk1, (272, 80), championSecondaryPerk1)
            back_im.paste(championSecondaryPerk2, (336, 80), championSecondaryPerk2)
        back_im.paste(championSpell1, (16, 144))
        back_im.paste(championSpell2, (80, 144))
        back_im.paste(championShard1, (464, 80), championShard1)
        back_im.paste(championShard2, (528, 80), championShard2)
        back_im.paste(championShard3, (592, 80), championShard3)
        back_im.save('infoimg2.png')
        await ctx.send(ctx.author.mention, file=discord.File('infoimg2.png', filename='infoimg2.png'))

bot.add_cog(Fun(bot))
bot.run(str(os.environ.get('BOT_TOKEN')))
