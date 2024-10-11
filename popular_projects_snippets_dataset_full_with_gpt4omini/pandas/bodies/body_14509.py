# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
"""Tests if RuntimeError is hit when calling lzma without
    having the module available.
    """
code = textwrap.dedent(
    """
        import sys
        import pytest
        sys.modules['lzma'] = None
        import pandas as pd
        df = pd.DataFrame()
        with pytest.raises(RuntimeError, match='lzma module'):
            df.to_csv('foo.csv', compression='xz')
        """
)
subprocess.check_output([sys.executable, "-c", code], stderr=subprocess.PIPE)
