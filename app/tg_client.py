from telethon import TelegramClient
from telethon.types import ReactionEmoji
from app.config import settings
from telethon.tl.types import User
from telethon.tl.functions.stories import SendReactionRequest, GetPeerStoriesRequest


client = TelegramClient(settings.SESSION_NAME, settings.API_ID, settings.API_HASH)

async def main():

    dialogs = await client.get_dialogs()
    user_dialogs = [dialog for dialog in dialogs if type(dialog.entity) == User]

    for dialog in user_dialogs:

        user_id = dialog.entity.id

        try:
            user_stories = await client(GetPeerStoriesRequest(peer=user_id))

            if not user_stories.stories.stories:
                print('У пользователя нет историй в данный момент')
            else:
                for story in user_stories.stories.stories:
                    await client(SendReactionRequest(peer=user_id,
                                                     story_id=story.id,
                                                     reaction=ReactionEmoji(
                                                         emoticon='❤️'
                                                     )))
                    print(f"Отправлена реакция ❤️ на сторис {story.id} пользователя {user_id}")

        except:
            print('Не получилось достать истории')





with client:
    client.loop.run_until_complete(main())
