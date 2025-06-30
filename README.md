# Telegram Conversation Bot

A simple Telegram bot that lets users message you and receive replies.

## Features
- Users can message the bot.
- Owner receives messages and can reply directly.
- Replies are forwarded back to users.
- Works with Render free plan using a dummy port listener.

## Setup

### Environment Variables

Copy `.env.example` to `.env` and fill in your credentials.

### Docker Usage

```bash
docker build -t telegram-reply-bot .
docker run --env-file .env telegram-reply-bot
```

### Deployment on Render (Free Tier)

1. Use a Web Service (NOT a background worker).
2. Make sure the service builds from Docker.
3. Add the environment variables from `.env`.
4. This bot includes a dummy HTTP server to keep Render from shutting it down.

## License

MIT © Sahil
