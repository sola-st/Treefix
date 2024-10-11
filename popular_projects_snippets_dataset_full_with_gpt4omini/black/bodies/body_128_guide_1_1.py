import sys # pragma: no cover

f = sys.stdout # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/files.py
from l3.Runtime import _l_
"""
    Wrap stream with colorama's wrap_stream so colors are shown on Windows.

    If `colorama` is unavailable, the original stream is returned unmodified.
    Otherwise, the `wrap_stream()` function determines whether the stream needs
    to be wrapped for a Windows environment and will accordingly either return
    an `AnsiToWin32` wrapper or the original stream.
    """
try:
    _l_(6782)

    from colorama.initialise import wrap_stream
    _l_(6778)
except ImportError:
    _l_(6780)

    aux = f
    _l_(6779)
    exit(aux)
else:
    aux = wrap_stream(f, convert=None, strip=False, autoreset=False, wrap=True)
    _l_(6781)
    # Set `strip=False` to avoid needing to modify test_express_diff_with_color.
    exit(aux)
