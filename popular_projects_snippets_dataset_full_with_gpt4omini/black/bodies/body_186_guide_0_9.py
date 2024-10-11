from pathlib import Path # pragma: no cover
import traceback # pragma: no cover
from enum import Enum # pragma: no cover

content = 'Sample content to reformat.' # pragma: no cover
fast = False # pragma: no cover
write_back = 'none' # pragma: no cover
mode = 'default' # pragma: no cover
class Changed(Enum): YES = 1; NO = 0 # pragma: no cover
changed = Changed.NO # pragma: no cover
class Report:  # pragma: no cover
    def done(self, path, changed):  # pragma: no cover
        print(f'Done processing {path}, changed: {changed}') # pragma: no cover
    def failed(self, path, message):  # pragma: no cover
        print(f'Failed processing {path}: {message}') # pragma: no cover
    verbose = True # pragma: no cover
report = Report() # pragma: no cover
path = Path('test.txt') # pragma: no cover
def format_stdin_to_stdout(content, fast, write_back, mode):  # pragma: no cover
    print(f'Formatting content: {content}, fast: {fast}, write_back: {write_back}, mode: {mode}') # pragma: no cover
    return True # pragma: no cover

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
_l_(6506)
try:
    _l_(6515)

    changed = Changed.NO
    _l_(6507)
    if format_stdin_to_stdout(
        content=content, fast=fast, write_back=write_back, mode=mode
    ):
        _l_(6509)

        changed = Changed.YES
        _l_(6508)
    report.done(path, changed)
    _l_(6510)
except Exception as exc:
    _l_(6514)

    if report.verbose:
        _l_(6512)

        traceback.print_exc()
        _l_(6511)
    report.failed(path, str(exc))
    _l_(6513)
