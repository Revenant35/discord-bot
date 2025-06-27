import os
import random
import discord
import pytz
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from dotenv import load_dotenv
from message_scheduler import MessageScheduler
from scheduled_message import ScheduledMessage


def main():
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    channel_id = int(os.getenv("CHANNEL_ID"))

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.voice_states = True
    intents.guilds = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")
        channel = bot.get_channel(channel_id)
        if not channel:
            print("Could not find a channel with that ID")
        else:
            messages = [
                ScheduledMessage(
                    "https://youtu.be/2WSqXrvm8i0?si=6saOxuUm408Dfwsi",
                    CronTrigger(day_of_week='fri', hour=15, minute=0, timezone=pytz.timezone('US/Central'))
                )
            ]
            message_scheduler = MessageScheduler(channel, messages)
            message_scheduler.start()

    @bot.command(name="kill")
    async def kill(ctx):
        members = [member for member in ctx.guild.members if not member.bot]

        if not members:
            await ctx.send("Please mention a user to disconnect.")
            return

        for member in members:
            if member.voice:
                await member.move_to(None)
                await ctx.send(f"{member.display_name} has perished.")
            else:
                await ctx.send(f"{member.display_name} is not in a voice channel.")

    @bot.command(name="cunky")
    async def cunky(ctx):
        members = [member for member in ctx.guild.members if not member.bot]
        random_member = "Everyone"
        if members:
            random_member = random.choice(members).mention

        messages = [
            "Cunky is good",
            "Cunky is great",
            "Cunky is the best",
            "Cunky is bad",
            "Cunky is terrible",
            "Cunky is the worst",
            "Cunky is nutritious",
            "Cunky is the future",
            "Cunky loves you",
            "I'd share a beer with cunky",
            f"{random_member} is infatuated with cunky",
            f"{random_member} despises cunky",
        ]

        await ctx.send(random.choice(messages))

    bot.run(token)


if __name__ == "__main__":
    main()
