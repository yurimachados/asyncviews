import asyncio
import time
import httpx
from django.http import HttpResponse
#import requests 

async def http_call_async():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(f'async call {num}')
    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.httpbin.org')
        print(r)

def http_call_sync():
    for num in range(1,6):
        time.sleep(1)
        print(f'sync call {num}')
    r = httpx.get('https://www.httpbin.org')
    print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")