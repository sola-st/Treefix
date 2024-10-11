import tempfile # pragma: no cover
import zipfile # pragma: no cover
import pytest # pragma: no cover
import pandas as pd # pragma: no cover

tm = type('Mock', (object,), {'ensure_clean': lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix)}) # pragma: no cover
suffix = '.zip' # pragma: no cover
archive = zipfile.ZipFile # pragma: no cover
pytest = type('pytest', (object,), {'raises': pytest.raises}) # pragma: no cover
pd = pd # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import os # pragma: no cover
import zipfile # pragma: no cover

suffix = '.zip' # pragma: no cover
class MockArchive(zipfile.ZipFile): # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass # pragma: no cover
archive = MockArchive # pragma: no cover
tm.ensure_clean = lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix, delete=False) # pragma: no cover
class CustomPytest: # pragma: no cover
    @staticmethod # pragma: no cover
    def raises(expected_exception, match=None): # pragma: no cover
        class RaisesContext: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_type: # pragma: no cover
                    raise AssertionError(f"DID NOT RAISE {expected_exception}") # pragma: no cover
                if not issubclass(exc_type, expected_exception): # pragma: no cover
                    return False # pragma: no cover
                if match and not re.search(match, str(exc_val)): # pragma: no cover
                    raise AssertionError(f"Exception did not match: {match}") # pragma: no cover
                return True # pragma: no cover
        return RaisesContext() # pragma: no cover
pytest = CustomPytest() # pragma: no cover

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
