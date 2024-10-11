from typing import Any, Dict, List # pragma: no cover

class MockLinkExtractor:# pragma: no cover
    def _extract_links(self, *args: Any, **kwargs: Dict[str, Any]) -> List[str]:# pragma: no cover
        return ['http://example.com', 'http://test.com'] # pragma: no cover
self = type('MockObject', (object,), {'link_extractor': MockLinkExtractor()})() # pragma: no cover
args = ('arg1', 'arg2') # pragma: no cover
kwargs = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
aux = self.link_extractor._extract_links(*args, **kwargs)
_l_(7547)
exit(aux)
