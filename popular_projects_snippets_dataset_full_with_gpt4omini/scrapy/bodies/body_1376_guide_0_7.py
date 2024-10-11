from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
from scrapy.dupefilters import RFPDupeFilter # pragma: no cover

settings = type('MockSettings', (), {'getbool': lambda self, key: True})() # pragma: no cover
fingerprinter = type('MockFingerprinter', (), {})() # pragma: no cover
cls = RFPDupeFilter # pragma: no cover
job_dir = lambda settings: 'mock_job_directory' # pragma: no cover

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
