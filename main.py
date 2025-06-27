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
        members = [member for member in ctx.message.mentions if not member.bot]

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
        members = [member for member in ctx.message.mentions if not member.bot]
        if not members:
            await generic_cunky(ctx)
        for member in members:
            await cunky_user(ctx, member)


    async def generic_cunky(ctx):
        messages = [
            "Cunky is great",
            "Cunky is the best",
            "Cunky is terrible",
            "Cunky is the worst",
            "Cunky is nutritious",
            "Cunky is the future",
            "Cunky loves you",
            "I'd share a beer with cunky",
            "Cunky is a lifestyle",
            "Cunky is a threat to national security",
            "Cunky is legally a gray area",
            "Cunky is why my therapist quit",
            "Cunky is sentient and watching",
            "Cunky is the noise in the walls",
            "Cunky is what happens when you microwave a god",
            "Cunky is both the question and the answer",
            "Cunky is love, cunky is pain",
            "Cunky is banned in 17 countries",
            "Cunky is what broke the simulation",
            "Cunky is made of 73% unknown matter",
            "Cunky is why we can't have nice things",
            "Cunky is whispering your name right now",
            "Cunky is inevitable",
            "Cunky is my emergency contact",
            "Cunky is the CEO of my nightmares",
            "Cunky is tax-deductible (somehow)",
            "Cunky is fueled by rage and Capri Sun",
            "Cunky is a war crime and a delicacy",
            "Cunky is a cryptid with an Instagram",
            "Cunky is what my last brain cell looks like",
            "Cunky is a poorly-disguised eldritch entity",
            "Cunky is the final boss of emotional damage",
            "Cunky is the reason your phone battery dies at 13%",
            "Cunky is probably illegal in space",
            "Cunky is the plot twist no one saw coming",
            "Cunky is proof that God has favorites, and it's not us",
            "Cunky is the result of a dare gone too far",
            "Cunky is a slippery slope and a slippery friend",
            "Cunky is the only thing keeping the fabric of reality together… barely",
        ]

        await ctx.send(random.choice(messages))

    async def cunky_user(ctx, user: discord.User):
        messages = [
            f"{user.mention} is infatuated with cunky",
            f"{user.mention} despises cunky",
            f"{user.mention} is a cunky enthusiast",
            f"{user.mention} is a cunky hater",
            f"{user.mention} is a cunky connoisseur",
            f"{user.mention} is a cunky critic",
            f"{user.mention} is a cunky lover",
            f"{user.mention} would die for cunky",
            f"{user.mention} thinks about cunky at 3AM, sweating",
            f"{user.mention} screams about cunky in their sleep",
            f"{user.mention} wrote a thesis on cunky",
            f"{user.mention} got banned from Discord for yelling about cunky",
            f"{user.mention} once punched someone for insulting cunky",
            f"{user.mention} wants to marry cunky",
            f"{user.mention} got a tattoo of cunky on their ass",
            f"{user.mention} lost everything gambling on cunky futures",
            f"{user.mention} is clinically obsessed with cunky",
            f"{user.mention} is in a toxic relationship with cunky",
            f"{user.mention} started a cult worshipping cunky",
            f"{user.mention} screams “CUNKY!” during inappropriate moments",
            f"{user.mention} blames cunky for all their problems",
            f"{user.mention} thinks cunky is their spirit animal",
            f"{user.mention} once saw cunky in a dream and never recovered",
            f"{user.mention} would fistfight God to defend cunky",
            f"{user.mention} has a Google alert for cunky news",
            f"{user.mention} prays to cunky before bed",
            f"{user.mention} has cunky on speed dial",
            f"{user.mention} tried to legally change their name to cunky",
            f"{user.mention} got doxxed for their controversial cunky opinions",
            f"{user.mention} got kicked out of therapy for bringing up cunky too much",
        ]
        await ctx.send(random.choice(messages))

    bot.run(token)


if __name__ == "__main__":
    main()
