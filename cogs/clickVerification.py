import config
import datetime
import discord
from discord.ext import commands

class clickVerification(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        member = payload.member
        if payload.member.bot:
            return
        if payload is not None:        
            if payload.message_id == config.clickVerificationMessageID:
                if str(payload.emoji) == "✅":
                    return await member.add_roles(discord.utils.get(member.guild.roles, id=config.clickVerificationAutoRole))
                else:
                    return
            
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def clickVerification(self, ctx):
        await ctx.message.delete()
        clickVerificationEmbed = await ctx.send(embed=discord.Embed(title=config.clickVerificationTitle, description=config.clickVerificationDescription, colour=config.embedColour, timestamp=datetime.datetime.utcnow()))
        return await clickVerificationEmbed.add_reaction('✅')

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(clickVerification(bot))