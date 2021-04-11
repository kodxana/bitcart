import electrum
from aiohttp import web
from base import BaseDaemon


class LBRYDaemon(BaseDaemon):
    name = "LBC"
    electrum = electrum
    DEFAULT_PORT = 5005


daemon = LBRYDaemon()

app = web.Application()
daemon.configure_app(app)
daemon.start(app)
