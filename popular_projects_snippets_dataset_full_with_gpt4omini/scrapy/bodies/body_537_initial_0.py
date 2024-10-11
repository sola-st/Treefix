import warnings # pragma: no cover
class Mock: # pragma: no cover
    pass # pragma: no cover
class ScrapyDeprecationWarning(Warning): # pragma: no cover
    pass # pragma: no cover

obj = type('MockObject', (Mock,), {'oldattr': 'old_attribute', 'newattr': 'new_attribute'})() # pragma: no cover
oldattr = 'oldattr' # pragma: no cover
version = '2.5.0' # pragma: no cover
newattr = 'newattr' # pragma: no cover
warnings = type('MockWarnings', (object,), {'warn': lambda self, message, category, stacklevel: print(f'Warning: {message}')})() # pragma: no cover
ScrapyDeprecationWarning = ScrapyDeprecationWarning # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
cname = obj.__class__.__name__
_l_(8857)
warnings.warn(
    f"{cname}.{oldattr} attribute is deprecated and will be no longer supported "
    f"in Scrapy {version}, use {cname}.{newattr} attribute instead",
    ScrapyDeprecationWarning,
    stacklevel=3)
_l_(8858)
