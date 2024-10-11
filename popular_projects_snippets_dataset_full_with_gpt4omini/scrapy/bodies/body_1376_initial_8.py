from scrapy.utils.project import get_project_settings # pragma: no cover
import warnings # pragma: no cover

settings = get_project_settings() # pragma: no cover
cls = type('RFPDupeFilter', (object,), {}) # pragma: no cover
def job_dir(settings): return 'path/to/job/dir' # pragma: no cover
fingerprinter = 'default_fingerprinter' # pragma: no cover
def warn(message, category): warnings.warn(message, category) # pragma: no cover
ScrapyDeprecationWarning = DeprecationWarning # pragma: no cover

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
