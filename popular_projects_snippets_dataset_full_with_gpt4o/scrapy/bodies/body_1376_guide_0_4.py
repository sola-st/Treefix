import warnings # pragma: no cover
from scrapy.settings import Settings # pragma: no cover
from scrapy.utils.log import get_scrapy_root_handler # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover

settings = Settings() # pragma: no cover
settings.set('DUPEFILTER_DEBUG', True) # pragma: no cover
def job_dir(settings): return '/some/directory/path' # pragma: no cover
fingerprinter = type('Fingerprinter', (object,), {})() # pragma: no cover
class MockRFPDupeFilter: # pragma: no cover
    @classmethod # pragma: no cover
    def from_settings(cls, settings): # pragma: no cover
        return cls(job_dir(settings), settings.getbool('DUPEFILTER_DEBUG')) # pragma: no cover
debug = settings.getbool('DUPEFILTER_DEBUG') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
from l3.Runtime import _l_
debug = settings.getbool('DUPEFILTER_DEBUG')
_l_(16095)
try:
    _l_(16102)

    aux = cls(job_dir(settings), debug, fingerprinter=fingerprinter)
    _l_(16096)
    exit(aux)
except TypeError:
    _l_(16101)

    warn(
        "RFPDupeFilter subclasses must either modify their '__init__' "
        "method to support a 'fingerprinter' parameter or reimplement "
        "the 'from_settings' class method.",
        ScrapyDeprecationWarning,
    )
    _l_(16097)
    result = cls(job_dir(settings), debug)
    _l_(16098)
    result.fingerprinter = fingerprinter
    _l_(16099)
    aux = result
    _l_(16100)
    exit(aux)
