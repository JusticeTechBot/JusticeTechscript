import time
from telethon import TelegramClient, events

# Your Telegram API credentials from https://my.telegram.org/apps
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
PHONE_NUMBER = "YOUR_PHONE_NUMBER"

# Target bot username
BOT_USERNAME = "goldeagle_bot"

# Initialize Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

async def main():
    # Start the client
    await client.start(phone=PHONE_NUMBER)

    print("Bot started! Listening for commands...")

    # Interact with the bot
    @client.on(events.NewMessage(from_users=BOT_USERNAME))
    async def handler(event):
        print(f"Message received: {event.raw_text}")

        # Example: Automatically reply with "Hello"
        if "specific trigger" in event.raw_text.lower():
            await client.send_message(BOT_USERNAME, "Hello!")

    # Send a start command
    await client.send_message(BOT_USERNAME, "/start")
    
    # Keep the client running
    await client.run_until_disconnected()

# Run the client
if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())