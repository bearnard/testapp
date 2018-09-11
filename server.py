#!/usr/bin/env python

import os

import prometheus_client
from aiohttp import web
from prometheus_client import Counter


counter = Counter('testapp_requests', 'Number of requests to /')


async def handle(request):
    counter.inc()
    text = "Hello, Openshift Container Platform helped me get here! version: {}".format(
        os.environ["TESTAPP_VERSION"])
    print('received request, replying with "{}".'.format(text))
    return web.Response(text=text)


async def metrics_handle(request):
    resp = web.Response(body=prometheus_client.generate_latest())
    resp.content_type = prometheus_client.CONTENT_TYPE_LATEST    
    return resp


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/metrics', metrics_handle)

web.run_app(app, port=5858)
