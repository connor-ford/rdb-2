import interactions
from config import TOKEN

client = interactions.Client(TOKEN)

@client.command()
async def ping(ctx: interactions.CommandContext):
    """Ping Pong!"""
    await ctx.send(f"Pong! ({(int) (ctx.client.latency)}ms)")

client.start()
