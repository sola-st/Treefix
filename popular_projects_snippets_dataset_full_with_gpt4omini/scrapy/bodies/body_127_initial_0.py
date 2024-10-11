from scrapy.http import Request # pragma: no cover
from itemadapter import ItemAdapter # pragma: no cover

class MockSelf: images_urls_field = 'image_urls' # pragma: no cover
item = {'image_urls': ['http://example.com/image1.jpg', 'http://example.com/image2.jpg']} # pragma: no cover
ItemAdapter = ItemAdapter # pragma: no cover
Request = Request # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
from l3.Runtime import _l_
urls = ItemAdapter(item).get(self.images_urls_field, [])
_l_(9182)
aux = [Request(u) for u in urls]
_l_(9183)
exit(aux)
