import electrum
from aiohttp import web
from base import BaseDaemon


class LBCDaemon(BaseDaemon):
    name = "LBC"
    electrum = electrum
    DEFAULT_PORT = 5005


daemon = LBCDaemon()

app = web.Application()
daemon.configure_app(app)
daemon.start(app)
