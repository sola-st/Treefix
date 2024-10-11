from pathlib import Path # pragma: no cover
import traceback # pragma: no cover

Path = Path # pragma: no cover
class Changed: # pragma: no cover
    NO = 'no' # pragma: no cover
    YES = 'yes' # pragma: no cover
def format_stdin_to_stdout(content, fast, write_back, mode): # pragma: no cover
    return True  # Mock implementation for testing # pragma: no cover
content = 'Some content to format' # pragma: no cover
fast = True # pragma: no cover
write_back = 'diff' # pragma: no cover
mode = {} # pragma: no cover
report = type('Mock', (object,), { # pragma: no cover
    'done': lambda self, path, changed: print(f'Done: {path}, {changed}'), # pragma: no cover
    'verbose': True, # pragma: no cover
    'failed': lambda self, path, exc: print(f'Failed: {path}, {exc}') # pragma: no cover
})() # pragma: no cover
traceback = type('Mock', (object,), { # pragma: no cover
    'print_exc': lambda: print('Traceback (most recent call last): ...') # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""
    Reformat and print out `content` without spawning child processes.
    Similar to `reformat_one`, but for string content.

    `fast`, `write_back`, and `mode` options are passed to
    :func:`format_file_in_place` or :func:`format_stdin_to_stdout`.
    """
path = Path("<string>")
_l_(18300)
try:
    _l_(18309)

    changed = Changed.NO
    _l_(18301)
    if format_stdin_to_stdout(
        content=content, fast=fast, write_back=write_back, mode=mode
    ):
        _l_(18303)

        changed = Changed.YES
        _l_(18302)
    report.done(path, changed)
    _l_(18304)
except Exception as exc:
    _l_(18308)

    if report.verbose:
        _l_(18306)

        traceback.print_exc()
        _l_(18305)
    report.failed(path, str(exc))
    _l_(18307)
