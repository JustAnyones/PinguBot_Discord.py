import aiohttp

async def sendGetRequest(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as response:
                return await response.text()
    except Exception:
        raise
