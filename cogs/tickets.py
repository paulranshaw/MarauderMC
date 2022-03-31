import config
import datetime
import discord
from discord.ext import commands
import random
import requests

class Tickets(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def tickets(self, ctx):
        ticketEmbed = discord.Embed(title=config.ticketEmbedTitle, description=config.ticketEmbedDescription, colour=config.embedColour, timestamp=datetime.datetime.utcnow())
        ticket = await ctx.send(embed=ticketEmbed)
        return await ticket.add_reaction("📝")

    @commands.command()
    async def close(self, ctx):
        channel = ctx.channel.name  
        if (channel[:7]!="ticket-"):
            return                                    
        supportRole = ctx.guild.get_role(config.ticketsSupportRole)
        if supportRole not in ctx.author.roles:
                return
        messages = await ctx.channel.history(limit=None).flatten()
        log=""
        messages.reverse()
        for msg in (messages):
            if msg.content==None:
                log+=F"{msg.created_at}: EMBED (ID: {msg.id}) in #{msg.channel} ({msg.channel.id}) by {msg.author} ({msg.author.id})\n"
            else:
                log+=F"{msg.created_at}: {msg.content} (ID: {msg.id}) in #{msg.channel} ({msg.channel.id}) by {msg.author} ({msg.author.id})\n"
  
        API_ENDPOINT = "https://www.toptal.com/developers/hastebin/documents"
        r = requests.post(url = API_ENDPOINT, data = log.encode('utf-8')) 
        
        hkey = r.json()["key"]

        ticketsLog = discord.utils.get(ctx.author.guild.text_channels, id=config.ticketsLogChannel)
        logEmbed=discord.Embed(title="Ticket", description=F"Creator: <@{ctx.channel.topic}>\nLog: [Hastebin](https://hastebin.com/{hkey})\nSupport Staff: {ctx.author.mention}", colour=0xadd8e6, timestamp=datetime.datetime.utcnow())
        await ticketsLog.send(embed=logEmbed)
        
        await ctx.channel.delete()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        member = payload.member
        guild = member.guild
        member = payload.member
        if not guild:
            return
        if payload is not None:
            if payload.message_id == config.ticketsMessageID:
                channel = discord.utils.get(member.guild.text_channels, id=payload.channel_id)
                ticketsEmbed = await channel.fetch_message(payload.message_id)
                await ticketsEmbed.remove_reaction(payload.emoji, member)

                ticketID = random.randint(11111, 99999)
                
                if str(payload.emoji) == "📝":
                    name= "ticket-" + str(ticketID)
                    category = discord.utils.get(guild.categories, name=config.ticketsCategoryName)
                else:
                    return

                name.replace(" ", "-")

                everyoneRole = guild.get_role(config.ticketsServerID) 
                supportRole= guild.get_role(config.ticketsSupportRole) 

                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    guild.me: discord.PermissionOverwrite(read_messages=True,send_messages=True),
                    member: discord.PermissionOverwrite(read_messages=True,send_messages=True),
                    everyoneRole: discord.PermissionOverwrite(read_messages=False),
                    supportRole: discord.PermissionOverwrite(read_messages=True,send_messages=True)
                }

                ticketChannel = await guild.create_text_channel(name, category=category, overwrites=overwrites, topic=member.id)

                await ticketChannel.send(content=f"{member.mention} | <@&937233785987145768>")

                templateEmbed = discord.Embed(title=config.ticketsTitle, description=config.ticketsTemplate, colour=config.embedColour, timestamp=datetime.datetime.utcnow())
                templateEmbed = await ticketChannel.send(embed=templateEmbed)

def setup(bot):
    bot.add_cog(Tickets(bot))