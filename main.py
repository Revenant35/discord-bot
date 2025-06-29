import os
import random
import discord
import pytz
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv

from cunky_messages import get_cunky_message, get_cunky_message_for_user
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
    async def kill(ctx: Context):
        from kill_messages import get_kill_message, get_not_in_channel_message, get_no_user_message

        members = [member for member in ctx.message.mentions if not member.bot]

        if not members:
            await ctx.send(get_no_user_message())
            return

        for member in members:
            if member.voice:
                await member.move_to(None)
                msg = get_kill_message(member.display_name)
                await ctx.send(msg)
            else:
                msg = get_not_in_channel_message(member.display_name)
                await ctx.send(msg)

    @bot.command(name="cunky")
    async def cunky(ctx: Context):
        members = [member for member in ctx.message.mentions if not member.bot]
        if not members:
            await ctx.send(get_cunky_message())
        else:
            for member in members:
                await ctx.send(get_cunky_message_for_user(member.mention))

    @bot.command(name="krill")
    async def krill(ctx: Context):
        await ctx.send("Learn more about shrimp welfare: https://www.shrimpwelfareproject.org/")

    bot.run(token)


if __name__ == "__main__":
    main()
