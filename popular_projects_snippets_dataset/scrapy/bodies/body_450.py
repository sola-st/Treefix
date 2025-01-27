# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
q = asyncio.Queue()
getter = q.get()
q.put_nowait(value)
exit(getter)
