from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.telegram.tg_actions import process_user_stories
from app.telegram.tg_client import client


def start_scheduler():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        func=process_user_stories,
        trigger=IntervalTrigger(minutes=2),
        args=(client,),
        id="like_stories_task",
        name="Send heart to user stories",
        replace_existing=True,
    )

    scheduler.start()
