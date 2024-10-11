from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
from warnings import warn # pragma: no cover

class MockSettings: # pragma: no cover
    def getbool(self, name): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
settings = MockSettings() # pragma: no cover
 # pragma: no cover
class MockJobDir: # pragma: no cover
    def __init__(self, settings): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def job_dir(settings): # pragma: no cover
    return MockJobDir(settings) # pragma: no cover
 # pragma: no cover
fingerprinter = type('MockFingerPrinter', (object,), {})() # pragma: no cover
 # pragma: no cover
class RFPDupeFilter: # pragma: no cover
    @classmethod # pragma: no cover
    def from_settings(cls, settings): # pragma: no cover
        return cls(job_dir(settings), True) # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        if not isinstance(fingerprinter, type('MockFingerPrinter', (object,), {})):  # Simulating mismatch type # pragma: no cover
            raise TypeError # pragma: no cover
 # pragma: no cover
cls = RFPDupeFilter # pragma: no cover

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
