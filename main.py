import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from the Discord Developer Portal.
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Create a bot instance with a command prefix (!)
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command: Hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your friendly Discord bot!')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Info
@bot.command()
async def info(ctx):
    await ctx.send('I am a Discord bot created with Python and discord.py!')

# Command: Server Info
@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    info = f'Server Name: {server.name}\nMember Count: {server.member_count}'
    await ctx.send(info)

# Command: User Info
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    info = f'Username: {member.name}\nDiscriminator: {member.discriminator}\nID: {member.id}'
    await ctx.send(info)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar_url)

# Command: Roll
@bot.command()
async def roll(ctx, num: int = 100):
    import random
    result = random.randint(1, num)
    await ctx.send(f'You rolled a {result} (1-{num})')

# Command: Coin Flip
@bot.command()
async def coinflip(ctx):
    import random
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(result)

@bot.command()
async def play(ctx, *, song: str):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        await ctx.send("You need to be in a voice channel to use this command.")
        return

    try:
        voice_client = await voice_channel.connect()
    except discord.errors.ClientException:
        voice_client = ctx.voice_client

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{song}", download=False)
        url = info['entries'][0]['url']

    voice_client.play(discord.FFmpegPCMAudio(url))
    await ctx.send(f'Now playing: {info["title"]}')

@bot.command()
async def stop(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client and voice_client.is_playing():
            voice_client.stop()

@bot.command()
async def leave(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()


# Command: Ban
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server. Reason: {reason}')

# Command: Kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server. Reason: {reason}')

# Command: Mute
@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, time=None, *, reason=None):
    # Implement mute functionality (e.g., assigning a "Muted" role to the user for the specified time)
    # Make sure to handle invalid time inputs and assign appropriate roles.
    await ctx.send(f'{member.mention} has been muted for {time}. Reason: {reason}')

# Command: Unmute
@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    # Implement unmute functionality (e.g., removing the "Muted" role from the user)
    # Make sure to handle cases where the user was not muted.
    await ctx.send(f'{member.mention} has been unmuted.')

# Command: Warn
@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    # Implement warn functionality (e.g., issuing a warning to the user)
    # You can use a database or a file to store warning information.
    await ctx.send(f'{member.mention} has been warned. Reason: {reason}')

# Command: Clear
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages have been deleted.')

# Command: Remind Me
@bot.command()
async def remindme(ctx, time, *, reminder):
    # Implement the reminder functionality using asyncio and datetime modules
    # to schedule and trigger reminders.
    await ctx.send(f'Okay, I will remind you to "{reminder}" at {time}.')

bot.run(BOT_TOKEN)