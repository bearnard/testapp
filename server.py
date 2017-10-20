#!/usr/bin/env python

import os

from aiohttp import web


async def handle(request):
    text = "Hello, IS helped me get here! version: {}".format(
        os.environ["TESTAPP_VERSION"])
    print('received request, replying with "{}".'.format(text))
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)

web.run_app(app, port=5858)
