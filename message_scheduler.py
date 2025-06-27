from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import TextChannel
from scheduled_message import ScheduledMessage


class MessageScheduler:
    def __init__(self, channel: TextChannel, messages: list[ScheduledMessage], scheduler: AsyncIOScheduler = AsyncIOScheduler()):
        self.channel = channel
        self.messages = messages
        self.scheduler = scheduler

        for message in self.messages:
            self.scheduler.add_job(self.send_message, message.time, args=[message.message])

    def start(self):
        self.scheduler.start()

    async def send_message(self, message: str):
        await self.channel.send(message)

