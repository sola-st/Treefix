# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
stats = self._downloader_interface.stats(self.pqueues)

if not stats:
    exit()

slot = min(stats)[1]
queue = self.pqueues[slot]
request = queue.pop()
if len(queue) == 0:
    del self.pqueues[slot]
exit(request)
