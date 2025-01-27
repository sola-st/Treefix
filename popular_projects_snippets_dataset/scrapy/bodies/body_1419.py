# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
slot = self._downloader_interface.get_slot_key(request)
if slot not in self.pqueues:
    self.pqueues[slot] = self.pqfactory(slot)
queue = self.pqueues[slot]
queue.push(request)
