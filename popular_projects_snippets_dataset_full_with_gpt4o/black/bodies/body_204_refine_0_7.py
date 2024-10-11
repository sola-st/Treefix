from typing import Any, Dict # pragma: no cover

_format_str_once = lambda dst, mode: f'formatted_{dst}_{mode}' # pragma: no cover
dst = 'initial_code' # pragma: no cover
mode = 'DEFAULT' # pragma: no cover
dump_to_file = lambda mode_str, diff_src, diff_dst: f'dump_log_{mode_str}_{diff_src}_{diff_dst}' # pragma: no cover
diff = lambda before, after, before_desc, after_desc: f'diff_{before_desc}_vs_{after_desc}' # pragma: no cover
src = 'original_source_code' # pragma: no cover

from typing import Any, Dict # pragma: no cover

_format_str_once = lambda dst, mode: dst # pragma: no cover
dst = 'sample_code' # pragma: no cover
mode = 'DEFAULT' # pragma: no cover
dump_to_file = lambda mode_str, diff_src, diff_dst: 'log.txt' # pragma: no cover
diff = lambda before, after, before_desc, after_desc: 'no_diff' # pragma: no cover
src = 'sample_source_code' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Raise AssertionError if `dst` reformats differently the second time."""
# We shouldn't call format_str() here, because that formats the string
# twice and may hide a bug where we bounce back and forth between two
# versions.
newdst = _format_str_once(dst, mode=mode)
_l_(16833)
if dst != newdst:
    _l_(16836)

    log = dump_to_file(
        str(mode),
        diff(src, dst, "source", "first pass"),
        diff(dst, newdst, "first pass", "second pass"),
    )
    _l_(16834)
    raise AssertionError(
        "INTERNAL ERROR: Black produced different code on the second pass of the"
        " formatter.  Please report a bug on https://github.com/psf/black/issues."
        f"  This diff might be helpful: {log}"
    ) from None
    _l_(16835)
