# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
from l3.Runtime import _l_
"""send notification mail with some additional useful info"""
stats = self.crawler.stats
_l_(9759)
s = f"Memory usage at engine startup : {stats.get_value('memusage/startup')/1024/1024}M\r\n"
_l_(9760)
s += f"Maximum memory usage          : {stats.get_value('memusage/max')/1024/1024}M\r\n"
_l_(9761)
s += f"Current memory usage          : {self.get_virtual_size()/1024/1024}M\r\n"
_l_(9762)

s += "ENGINE STATUS ------------------------------------------------------- \r\n"
_l_(9763)
s += "\r\n"
_l_(9764)
s += pformat(get_engine_status(self.crawler.engine))
_l_(9765)
s += "\r\n"
_l_(9766)
self.mail.send(rcpts, subject, s)
_l_(9767)
