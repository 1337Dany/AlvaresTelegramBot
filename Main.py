import asyncio
from uvicorn import Config, Server

from utils.bot_service import bs
from app.handlers import router  # , state_router


async def main() -> None:
    await asyncio.gather(
        run_bot(),
        # run_server()
    )


async def run_bot() -> None:
    try:
        bs.dispatcher.include_router(router)
        # dp.include_router(state_router)
        await bs.dispatcher.start_polling(bs.bot)
    except KeyboardInterrupt:
        await bs.bot.close()


# establishing server controller
async def run_server() -> None:
    config = Config(app="controllers.controller:app", host="0.0.0.0", port=17001, reload=False)
    server = Server(config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
