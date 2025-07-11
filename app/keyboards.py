from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#it is a reply keyboard with one button for canceling operation of context search
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Cancel")],
],
    resize_keyboard=True,
    input_field_placeholder="Write context....."
)

# inline keyboard shows under message after /start command, shows info about bot and how to use it
start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Do you need help?",
                          url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",)],
    [InlineKeyboardButton(text="Visit website", url="http://alvaresonline.duckdns.org:17000/")],
    [InlineKeyboardButton(text="About", callback_data="about")],
])

# inline keyboard for choosing what type of message to search
message_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Text message", callback_data="text")],
        [InlineKeyboardButton(text="Image message", callback_data="image")],
        [InlineKeyboardButton(text="Audio message", callback_data="audio")],
        [InlineKeyboardButton(text="Document", callback_data="document")],
        [InlineKeyboardButton(text="Video message", callback_data="video")],
    ]
)

