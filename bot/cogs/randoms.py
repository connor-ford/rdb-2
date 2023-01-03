import interactions
import random


class RandomsCog(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(name="coinflip", description="Flips a coin.")
    async def coinflip(self, ctx: interactions.CommandContext):
        await ctx.send(f"It's {'Head' if random.randint(0, 1) == 1 else 'Tail'}s.")

    @interactions.extension_command(
        name="diceroll",
        description="Rolls n dice with n sides.",
    )
    @interactions.option("The amount of dice to roll (default is 1, range is 1-100).")
    @interactions.option(
        "The amount of sides each dice should have (default is 6, range is 2-100)."
    )
    async def rolldice(
        self, ctx: interactions.CommandContext, amount: int = 1, sides: int = 6
    ):
        if not (1 <= amount <= 100):
            await ctx.send("Amount of dice must be between 1-100.")
            return
        if not (2 <= sides <= 100):
            await ctx.send("Amount of sides must be between 2-100.")
            return
        await ctx.send(
            f"Rolled {amount} {sides}-sided dice: ```"
            + "\n".join([str(random.randint(1, sides)) for _ in range(0, amount)])
            + "```"
        )


def setup(client):
    RandomsCog(client)
