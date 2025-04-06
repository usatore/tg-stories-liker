from datetime import datetime, timedelta, timezone

from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.stories import (GetPeerStoriesRequest,
                                           SendReactionRequest)
from telethon.tl.types import ReactionEmoji

from app.tg_users.dao import TGUsersDAO


async def process_user_stories(client: TelegramClient):

    contacts = await client(GetContactsRequest(hash=0))

    for contact in contacts.users:

        contact_id = contact.id

        contact_stories = await client(GetPeerStoriesRequest(peer=contact_id))

        if contact_stories.stories.stories:

            tg_user = await TGUsersDAO.get_tg_user_by_tg_id(tg_id=contact_id)

            if tg_user is None:
                tg_user = await TGUsersDAO.add_tg_user(
                    tg_id=contact_id, tg_nickname=contact.username
                )
                print(f"Пользователь с ID {contact_id} добавлен в базу данных.")

            last_like_time = tg_user.last_like_time

            if not last_like_time is None:
                time_diff = datetime.now(tz=timezone.utc) - last_like_time
                if time_diff < timedelta(days=2):
                    continue

            for story in contact_stories.stories.stories:
                await client(
                    SendReactionRequest(
                        peer=contact_id,
                        story_id=story.id,
                        reaction=ReactionEmoji(emoticon="❤️"),
                    )
                )
                print(
                    f"Отправлена реакция ❤️ на сторис {story.id} пользователя {contact_id}"
                )

            await TGUsersDAO.update_last_like_time(tg_id=contact_id)
