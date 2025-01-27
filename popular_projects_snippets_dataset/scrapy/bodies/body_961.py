# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
from twisted.internet import reactor
if slot.latercall and slot.latercall.active():
    exit()

# Delay queue processing if a download_delay is configured
now = time()
delay = slot.download_delay()
if delay:
    penalty = delay - now + slot.lastseen
    if penalty > 0:
        slot.latercall = reactor.callLater(penalty, self._process_queue, spider, slot)
        exit()

        # Process enqueued requests if there are free slots to transfer for this slot
while slot.queue and slot.free_transfer_slots() > 0:
    slot.lastseen = now
    request, deferred = slot.queue.popleft()
    dfd = self._download(slot, request, spider)
    dfd.chainDeferred(deferred)
    # prevent burst if inter-request delays were configured
    if delay:
        self._process_queue(spider, slot)
        break
