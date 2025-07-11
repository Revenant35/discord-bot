from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import TextChannel
from scheduled_message import ScheduledMessage


class MessageScheduler:
    def __init__(self, scheduler: AsyncIOScheduler = AsyncIOScheduler()):
        self.channel = None
        self.scheduler = scheduler
        self.jobs_scheduled = False

    def schedule_messages(self, channel: TextChannel, messages: list[ScheduledMessage]):
        if self.jobs_scheduled:
            return

        self.channel = channel
        for message in messages:
            self.scheduler.add_job(self.send_message, message.time, args=[message.message])
        
        self.jobs_scheduled = True

    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()

    def shutdown(self):
        if self.scheduler.running:
            self.scheduler.shutdown()

    async def send_message(self, message: str):
        if self.channel:
            await self.channel.send(message)

