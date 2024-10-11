import warnings # pragma: no cover

obj = type('MockObject', (object,), {})() # pragma: no cover
oldattr = 'old_attribute' # pragma: no cover
version = '2.0' # pragma: no cover
newattr = 'new_attribute' # pragma: no cover
ScrapyDeprecationWarning = type('ScrapyDeprecationWarning', (Warning,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
cname = obj.__class__.__name__
_l_(19828)
warnings.warn(
    f"{cname}.{oldattr} attribute is deprecated and will be no longer supported "
    f"in Scrapy {version}, use {cname}.{newattr} attribute instead",
    ScrapyDeprecationWarning,
    stacklevel=3)
_l_(19829)
