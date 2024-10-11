# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
key = self._get_slot_key(request, spider)
if key not in self.slots:
    conc = self.ip_concurrency if self.ip_concurrency else self.domain_concurrency
    conc, delay = _get_concurrency_delay(conc, spider, self.settings)
    self.slots[key] = Slot(conc, delay, self.randomize_delay)

exit((key, self.slots[key]))
