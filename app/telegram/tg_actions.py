from telethon.tl.types import ReactionEmoji
from telethon.tl.functions.stories import SendReactionRequest, GetPeerStoriesRequest
from telethon.tl.types import User
from telethon import TelegramClient


async def process_user_stories(client: TelegramClient):
    dialogs = await client.get_dialogs()
    user_dialogs = [dialog for dialog in dialogs if isinstance(dialog.entity, User)]

    for dialog in user_dialogs:
        user_id = dialog.entity.id

        try:
            user_stories = await client(GetPeerStoriesRequest(peer=user_id))

            if not user_stories.stories.stories:
                print(f'У пользователя {user_id} нет историй в данный момент')
            else:
                for story in user_stories.stories.stories:
                    await client(SendReactionRequest(peer=user_id,
                                                     story_id=story.id,
                                                     reaction=ReactionEmoji(
                                                         emoticon='❤️'
                                                     )))
                    print(f"Отправлена реакция ❤️ на сторис {story.id} пользователя {user_id}")

        except Exception as e:
            print(f'Не получилось достать истории пользователя {user_id}: {e}')
