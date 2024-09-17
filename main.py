from pyrogram import Client, filters
from datetime import datetime, timezone, timedelta
from decouple import config

API_ID = config("API_ID")
API_HASH = config("API_HASH")

app = Client("auto_responder_bot", api_id=API_ID, api_hash=API_HASH)

start_hour = 14
end_hour = 2
end_minute = 00
timezone_offset = 3 

@app.on_message(filters.private)
async def auto_response(client, message):
    now = datetime.now(timezone.utc)
    local_time = now + timedelta(hours=timezone_offset)
    now_hour = local_time.hour
    now_minute = local_time.minute
    now_weekday = local_time.weekday() 
    if (now_hour > end_hour or (now_hour == end_hour and now_minute >= end_minute)) and now_hour < start_hour or now_weekday in [5, 6]:
        await message.reply("Извините, я сейчас недоступен. Пожалуйста, свяжитесь со мной с 14:00 до 02:00 по UTC+3 в будние дни.")

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
