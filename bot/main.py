import os
import threading
from pyrogram import Client, filters
from pyrogram.types import Message
from http.server import BaseHTTPRequestHandler, HTTPServer

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
OWNER_ID = int(os.getenv("OWNER_ID"))

app = Client("conversation_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Dummy HTTP server to keep Render happy
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("", port), DummyHandler)
    print(f"Dummy server running on port {port}")
    server.serve_forever()

# Start dummy server in a background thread
threading.Thread(target=run_dummy_server, daemon=True).start()

# Telegram bot handlers
@app.on_message(filters.private & ~filters.user(OWNER_ID))
async def forward_to_owner(client, message: Message):
    await message.forward(OWNER_ID)
    await message.reply_text("✅ Your message has been received.")

@app.on_message(filters.private & filters.user(OWNER_ID) & filters.reply)
async def reply_to_user(client, message: Message):
    if message.reply_to_message.forward_from:
        user_id = message.reply_to_message.forward_from.id
        await app.send_message(user_id, message.text)
        await message.reply_text("✉️ Reply sent.")
    else:
        await message.reply_text("⚠️ Can't detect original user.")

app.run()
