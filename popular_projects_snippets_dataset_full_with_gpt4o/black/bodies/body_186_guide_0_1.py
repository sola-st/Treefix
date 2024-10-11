from pathlib import Path # pragma: no cover
import traceback # pragma: no cover

content = 'sample content' # pragma: no cover
fast = True # pragma: no cover
write_back = 'option' # pragma: no cover
mode = 'mode_value' # pragma: no cover
def format_stdin_to_stdout(content, fast, write_back, mode): # pragma: no cover
    # Mock function for format_stdin_to_stdout, returns True to execute uncovered path # pragma: no cover
    return True # pragma: no cover
class Changed: # pragma: no cover
    NO = 'no' # pragma: no cover
    YES = 'yes' # pragma: no cover
class MockReport: # pragma: no cover
    verbose = True # pragma: no cover
    def done(self, path, changed): # pragma: no cover
        print(f'Report done for {path} with change status {changed}') # pragma: no cover
    def failed(self, path, message): # pragma: no cover
        print(f'Report failed for {path} with message: {message}') # pragma: no cover
report = MockReport() # pragma: no cover

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
