from itemadapter import ItemAdapter # pragma: no cover
from scrapy import Request # pragma: no cover

item = {'image_urls': ['http://example.com/image1.jpg', 'http://example.com/image2.jpg']} # Example item # pragma: no cover
self = type('Mock', (object,), {'images_urls_field': 'image_urls'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
from l3.Runtime import _l_
urls = ItemAdapter(item).get(self.images_urls_field, [])
_l_(20668)
aux = [Request(u) for u in urls]
_l_(20669)
exit(aux)
