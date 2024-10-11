from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.utils.job import job_dir # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
import warnings # pragma: no cover

settings = get_project_settings() # pragma: no cover
cls = type('MockClass', (object,), {'__init__': lambda self, job_dir, debug, fingerprinter=None: None, 'from_settings': classmethod(lambda cls, settings: cls(job_dir(settings), debug))}) # pragma: no cover
fingerprinter = type('MockFingerprinter', (object,), {})() # pragma: no cover
warn = warnings.warn # pragma: no cover
job_dir = lambda settings: '/some/job/dir' # pragma: no cover

import warnings # pragma: no cover
from scrapy.utils.job import job_dir # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover

class MockSettings: # pragma: no cover
    def getbool(self, key): # pragma: no cover
        if key == 'DUPEFILTER_DEBUG': # pragma: no cover
            return True # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
    def __getitem__(self, item): # pragma: no cover
        if item == 'JOBDIR': # pragma: no cover
            return '/some/job/dir' # pragma: no cover
        raise KeyError # pragma: no cover
 # pragma: no cover
settings = MockSettings() # pragma: no cover
 # pragma: no cover
class MockCls: # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        self.job_dir = job_dir # pragma: no cover
        self.debug = debug # pragma: no cover
        self.fingerprinter = fingerprinter # pragma: no cover
 # pragma: no cover
    @classmethod # pragma: no cover
    def from_settings(cls, settings): # pragma: no cover
        job_directory = job_dir(settings) # pragma: no cover
        debug_mode = settings.getbool('DUPEFILTER_DEBUG') # pragma: no cover
        return cls(job_directory, debug_mode) # pragma: no cover
 # pragma: no cover
fingerprinter = lambda: None # pragma: no cover
warn = warnings.warn # pragma: no cover
ScrapyDeprecationWarning = ScrapyDeprecationWarning # pragma: no cover

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
