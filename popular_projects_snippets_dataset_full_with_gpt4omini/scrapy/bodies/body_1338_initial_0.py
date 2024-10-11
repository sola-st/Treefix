from collections import defaultdict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
self.stats.inc_value('downloader/response_count', spider=spider)
_l_(8943)
self.stats.inc_value(f'downloader/response_status_count/{response.status}', spider=spider)
_l_(8944)
reslen = len(response.body) + get_header_size(response.headers) + get_status_size(response.status) + 4
_l_(8945)
# response.body + b"\r\n"+ response.header + b"\r\n" + response.status
self.stats.inc_value('downloader/response_bytes', reslen, spider=spider)
_l_(8946)
aux = response
_l_(8947)
exit(aux)
