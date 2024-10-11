output_format = 'json' # pragma: no cover
valid_output_formats = ['xml', 'csv', 'json'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
from l3.Runtime import _l_
if output_format not in valid_output_formats:
    _l_(9213)

    raise UsageError(
        f"Unrecognized output format '{output_format}'. "
        f"Set a supported one ({tuple(valid_output_formats)}) "
        "after a colon at the end of the output URI (i.e. -o/-O "
        "<URI>:<FORMAT>) or as a file extension."
    )
    _l_(9212)
