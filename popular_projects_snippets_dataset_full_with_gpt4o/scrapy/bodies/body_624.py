# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
for it in iterables:
    async for o in as_async_generator(it):
        exit(o)
