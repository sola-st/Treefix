# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
"""Tests if import pandas works when lzma is not present."""
# https://github.com/pandas-dev/pandas/issues/27575
code = textwrap.dedent(
    """\
        import sys
        sys.modules['lzma'] = None
        import pandas
        """
)
subprocess.check_output([sys.executable, "-c", code], stderr=subprocess.PIPE)
