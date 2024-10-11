import aiofiles # pragma: no cover
import aiohttp # pragma: no cover
import asyncio # pragma: no cover

SRC_URL = 'https://example.com/file.txt' # pragma: no cover
DEST_FILE = 'local_file.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
from l3.Runtime import _l_
try:
    import aiofiles
    _l_(2810)

except ImportError:
    pass
try:
    import aiohttp
    _l_(2812)

except ImportError:
    pass
try:
    import asyncio
    _l_(2814)

except ImportError:
    pass

async def async_http_download(src_url, dest_file, chunk_size=65536):
    _l_(2820)

    async with aiofiles.open(dest_file, 'wb') as fd:
        _l_(2819)

        async with aiohttp.ClientSession() as session:
            _l_(2818)

            async with session.get(src_url) as resp:
                _l_(2817)

                async for chunk in resp.content.iter_chunked(chunk_size):
                    _l_(2816)

                    await fd.write(chunk)
                    _l_(2815)

SRC_URL = "/path/to/url"
_l_(2821)
DEST_FILE = "/path/to/file/on/local/machine"
_l_(2822)

asyncio.run(async_http_download(SRC_URL, DEST_FILE))
_l_(2823)

