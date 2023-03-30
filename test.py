from pornhub_api import PornhubApi
import asyncio
import random
import aiohttp
from pornhub_api.backends.aiohttp import AioHttpBackend
from discord_webhook import DiscordWebhook

async def execute():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        backend = AioHttpBackend()
        backend._session = session
        api = PornhubApi(backend=backend)
        video = await api.video.get_by_id("ph560b93077ddae")


asyncio.run(execute())

api = PornhubApi()

tags = random.sample(api.video.tags("f").tags, 5)
category = random.choice(api.video.categories().categories)
result = api.search.search_videos(ordering="mostviewed", tags=tags, category=category)

print(result.size())
for vid in result:
    print(vid.title, vid.url)
    break
    
webhook = DiscordWebhook(url='!!!!!!!!! ENTER YOUR URL HERE !!!!!!!!!!!')

message = f"New Video: {vid.title}\n{vid.url}"
webhook.set_content(content=message)
response = webhook.execute()
