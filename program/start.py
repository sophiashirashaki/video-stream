@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **Thanks for adding me to the Group !**\n\n"
                "**Promote me as administrator of the Group, otherwise I will not be able to work properly.**\n\n"
                "**Once done type** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Channel", url=f"https://t.me/projectsupdates"),
                            InlineKeyboardButton("Support", url=f"https://t.me/AkoUpdate"),
                        ]
                    ]
                )
            )
