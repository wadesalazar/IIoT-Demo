from aiohttp import web
from aiohttp import WSMsgType

async def index(request):
    return web.FileResponse('.\\index.html')

async def health(request):
    return web.Response(text = "Device time" + os.popen('date').read())

async def getwifiname(request):
    return web.Response(body = {names : "Wifi SSID 1,Wifi SSID 2,Wifi SSID 3"})



