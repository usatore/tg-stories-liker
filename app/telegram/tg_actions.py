from datetime import datetime, timedelta, timezone

from telethon import TelegramClient
from telethon.tl.functions.stories import (GetPeerStoriesRequest,
                                           SendReactionRequest)
from telethon.tl.types import ReactionEmoji, User

from app.tg_users.dao import TGUsersDAO


async def process_user_stories(client: TelegramClient):
    dialogs = await client.get_dialogs()
    user_dialogs = [dialog for dialog in dialogs if isinstance(dialog.entity, User)]

    for dialog in user_dialogs:

        user_id = dialog.entity.id
        user_nickname = dialog.entity.username

        user_stories = await client(GetPeerStoriesRequest(peer=user_id))

        if user_stories.stories.stories:
            tg_user = await TGUsersDAO.get_tg_user_by_tg_id(tg_id=user_id)
            if tg_user is None:
                tg_user = await TGUsersDAO.add_tg_user(
                    tg_id=user_id, tg_nickname=user_nickname
                )
                print(f"Пользователь с ID {user_id} добавлен в базу данных.")

            last_like_time = tg_user.last_like_time

            if not last_like_time is None:
                time_diff = datetime.now(tz=timezone.utc) - last_like_time
                if time_diff < timedelta(days=2):
                    print(f"Слишком рано для лайка пользователя {user_id}")
                    continue

            for story in user_stories.stories.stories:
                await client(
                    SendReactionRequest(
                        peer=user_id,
                        story_id=story.id,
                        reaction=ReactionEmoji(emoticon="❤️"),
                    )
                )
                print(
                    f"Отправлена реакция ❤️ на сторис {story.id} пользователя {user_id}"
                )

            await TGUsersDAO.update_last_like_time(tg_id=user_id)
