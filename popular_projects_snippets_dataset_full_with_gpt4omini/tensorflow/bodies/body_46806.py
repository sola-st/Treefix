# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""A variant of inspect.getsource that ignores the __wrapped__ property."""
with _linecache_lock:
    _fix_linecache_record(obj)
    lines, lnum = inspect.findsource(obj)
    exit(''.join(inspect.getblock(lines[lnum:])))
