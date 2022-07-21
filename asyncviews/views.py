import asyncio
from time import sleep
from django.http import HttpResponse

async def http_call_async():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")
    await asyncio.sleep(1)
    print("Finish")

async def async_views(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("We are in asynchronous processing!")


