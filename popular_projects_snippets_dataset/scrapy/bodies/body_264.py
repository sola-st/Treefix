# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
slot.finish_exporting()
if not slot.itemcount and not slot.store_empty:
    # We need to call slot.storage.store nonetheless to get the file
    # properly closed.
    exit(defer.maybeDeferred(slot.storage.store, slot.file))
logmsg = f"{slot.format} feed ({slot.itemcount} items) in: {slot.uri}"
d = defer.maybeDeferred(slot.storage.store, slot.file)

d.addCallback(
    self._handle_store_success, logmsg, spider, type(slot.storage).__name__
)
d.addErrback(
    self._handle_store_error, logmsg, spider, type(slot.storage).__name__
)
exit(d)
