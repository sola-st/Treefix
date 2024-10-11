# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
self._slot_gc_loop.stop()
for slot in self.slots.values():
    slot.close()
