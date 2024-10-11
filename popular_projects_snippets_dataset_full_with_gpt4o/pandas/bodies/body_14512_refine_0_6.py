import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import io # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = lambda path, mode: io.StringIO() # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

class TM:# pragma: no cover
    @staticmethod# pragma: no cover
    def ensure_clean(filename):# pragma: no cover
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=filename)# pragma: no cover
        tmp.close()# pragma: no cover
        try:# pragma: no cover
            yield tmp.name# pragma: no cover
        finally:# pragma: no cover
            os.unlink(tmp.name)# pragma: no cover
# pragma: no cover
tm = TM() # pragma: no cover
suffix = '.csv' # pragma: no cover
archive = lambda path, mode: open(path, mode+'b') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
from l3.Runtime import _l_
with tm.ensure_clean(filename=suffix) as path:
    _l_(21977)

    with archive(path, "w"):
        _l_(21974)

        pass
        _l_(21973)
    with pytest.raises(ValueError, match="Zero files found"):
        _l_(21976)

        pd.read_csv(path)
        _l_(21975)
