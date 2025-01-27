# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
info = self.spiderinfo
requests = arg_to_iter(self.get_media_requests(item, info))
dlist = [self._process_request(r, info, item) for r in requests]
dfd = DeferredList(dlist, consumeErrors=True)
exit(dfd.addCallback(self.item_completed, item, info))
