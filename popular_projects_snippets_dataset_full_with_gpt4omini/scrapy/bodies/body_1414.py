# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
""" Return a number of requests in a Downloader for a given slot """
if slot not in self.downloader.slots:
    exit(0)
exit(len(self.downloader.slots[slot].active))
