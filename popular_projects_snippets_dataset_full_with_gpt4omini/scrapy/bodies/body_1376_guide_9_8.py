from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
import warnings # pragma: no cover

class MockSettings: # pragma: no cover
    def getbool(self, key): return False # pragma: no cover
# Return False to provoke a TypeError # pragma: no cover
 # pragma: no cover
class MockCls: # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        if fingerprinter is None: # pragma: no cover
            raise TypeError('fingerprinter required') # pragma: no cover
 # pragma: no cover
def job_dir(settings): return 'mock_job_dir' # pragma: no cover
settings = MockSettings() # pragma: no cover
fingerprinter = None # pragma: no cover
# This will trigger the TypeError # pragma: no cover
cls = MockCls # pragma: no cover
warn = warnings.warn # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
from l3.Runtime import _l_
debug = settings.getbool('DUPEFILTER_DEBUG')
_l_(4743)
try:
    _l_(4750)

    aux = cls(job_dir(settings), debug, fingerprinter=fingerprinter)
    _l_(4744)
    exit(aux)
except TypeError:
    _l_(4749)

    warn(
        "RFPDupeFilter subclasses must either modify their '__init__' "
        "method to support a 'fingerprinter' parameter or reimplement "
        "the 'from_settings' class method.",
        ScrapyDeprecationWarning,
    )
    _l_(4745)
    result = cls(job_dir(settings), debug)
    _l_(4746)
    result.fingerprinter = fingerprinter
    _l_(4747)
    aux = result
    _l_(4748)
    exit(aux)
