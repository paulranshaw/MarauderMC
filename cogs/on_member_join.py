import config
import datetime
import discord
from discord.ext import commands  

class On_Member_Join(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcomeChannel = discord.utils.get(member.guild.text_channels, id=config.welcomeChannel)
        welcomeEmbed = discord.Embed(description=f'(!) Welcome, {member.mention} to the MarauderMC | Prisons!\n\n:pushpin: **INFORMATION**\n:video_game: | play.maraudermc.com\n:credit_card: | https://shop.maraudermc.com\n\n(( For more information please read <#937233793310425119>.))', colour=config.embedColour, timestamp=datetime.datetime.utcnow())
        welcomeEmbed.set_image(url='https://media.discordapp.net/attachments/937233793310425119/937350553455984700/MarauderMC_Header.png?width=1200&height=400')
        await welcomeChannel.send(embed=welcomeEmbed)

def setup(bot):
    bot.add_cog(On_Member_Join(bot))