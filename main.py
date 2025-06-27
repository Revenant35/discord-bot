import os
import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv
import pytz

def main():
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    channel_id = int(os.getenv("CHANNEL_ID"))

    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!", intents=intents)

    scheduler = AsyncIOScheduler()


    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")

        if not scheduler.get_jobs():
            scheduler.add_job(send_youtube_video,
                              CronTrigger(day_of_week='fri', hour=15, minute=0, timezone=pytz.timezone('US/Central')))
            scheduler.start()
            print("Scheduler started.")


    async def send_youtube_video():
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send("https://youtu.be/2WSqXrvm8i0?si=6saOxuUm408Dfwsi")
        else:
            print("Channel not found.")


    bot.run(token)

if __name__ == "__main__":
    main()
