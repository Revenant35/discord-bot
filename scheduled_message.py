from apscheduler.triggers.cron import CronTrigger


class ScheduledMessage:
    def __init__(self, message: str, time: CronTrigger):
        self.message = message
        self.time = time
