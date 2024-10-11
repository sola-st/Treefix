from typing import Any, List # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockLinkExtractor: # pragma: no cover
    def _extract_links(self, *args: Any, **kwargs: Any) -> List[str]: # pragma: no cover
        return ['http://example.com', 'http://example.org'] # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    link_extractor = MockLinkExtractor() # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
aux = self.link_extractor._extract_links(*args, **kwargs)
_l_(17976)
exit(aux)
