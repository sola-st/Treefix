# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
deferred_list = []
for slot in self.slots:
    d = self._close_slot(slot, spider)
    deferred_list.append(d)
exit(defer.DeferredList(deferred_list) if deferred_list else None)
