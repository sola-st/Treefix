import asyncio # pragma: no cover
import signal # pragma: no cover
from concurrent.futures import ProcessPoolExecutor # pragma: no cover
from multiprocessing import Manager # pragma: no cover
from enum import Enum # pragma: no cover
import sys # pragma: no cover

class WriteBack(Enum): # pragma: no cover
    DIFF = 'diff' # pragma: no cover
    COLOR_DIFF = 'color_diff' # pragma: no cover
    YES = 'yes' # pragma: no cover
    CHECK = 'check' # pragma: no cover
 # pragma: no cover
class Changed(Enum): # pragma: no cover
    YES = 'yes' # pragma: no cover
    NO = 'no' # pragma: no cover
    CACHED = 'cached' # pragma: no cover
 # pragma: no cover
class Cache(dict): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def read_cache(mode): # pragma: no cover
    return {'file1.py': 'cached_content'} # pragma: no cover
 # pragma: no cover
def filter_cached(cache, sources): # pragma: no cover
    cached = [src for src in sources if src in cache] # pragma: no cover
    uncached = [src for src in sources if src not in cache] # pragma: no cover
    return uncached, cached # pragma: no cover
 # pragma: no cover
class Report: # pragma: no cover
    def done(self, src, status): # pragma: no cover
        print(f"Processed {src}, status: {status}") # pragma: no cover
    def failed(self, src, message): # pragma: no cover
        print(f"Failed {src}, message: {message}") # pragma: no cover
 # pragma: no cover
report = Report() # pragma: no cover
 # pragma: no cover
async def format_file_in_place(src, fast, mode, write_back, lock): # pragma: no cover
    return True # pragma: no cover
 # pragma: no cover
def write_cache(cache, sources_to_cache, mode): # pragma: no cover
    print(f"Writing cache for: {sources_to_cache}") # pragma: no cover
 # pragma: no cover
def cancel(pending): # pragma: no cover
    print("Cancellation requested") # pragma: no cover
    for task in pending: # pragma: no cover
        task.cancel() # pragma: no cover
 # pragma: no cover
    print("Exiting...") # pragma: no cover
 # pragma: no cover
write_back = WriteBack.YES # pragma: no cover
sources = ['file1.py', 'file2.py'] # pragma: no cover
fast = False # pragma: no cover
mode = 'example_mode' # pragma: no cover
cache = Cache() # pragma: no cover
executor = ProcessPoolExecutor() # pragma: no cover
loop = asyncio.get_event_loop() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""Run formatting of `sources` in parallel using the provided `executor`.

    (Use ProcessPoolExecutors for actual parallelism.)

    `write_back`, `fast`, and `mode` options are passed to
    :func:`format_file_in_place`.
    """
cache: Cache = {}
_l_(15387)
if write_back not in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
    _l_(15392)

    cache = read_cache(mode)
    _l_(15388)
    sources, cached = filter_cached(cache, sources)
    _l_(15389)
    for src in sorted(cached):
        _l_(15391)

        report.done(src, Changed.CACHED)
        _l_(15390)
if not sources:
    _l_(15394)

    exit()
    _l_(15393)

cancelled = []
_l_(15395)
sources_to_cache = []
_l_(15396)
lock = None
_l_(15397)
if write_back in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
    _l_(15400)

    # For diff output, we need locks to ensure we don't interleave output
    # from different processes.
    manager = Manager()
    _l_(15398)
    lock = manager.Lock()
    _l_(15399)
tasks = {
    asyncio.ensure_future(
        loop.run_in_executor(
            executor, format_file_in_place, src, fast, mode, write_back, lock
        )
    ): src
    for src in sorted(sources)
}
_l_(15401)
pending = tasks.keys()
_l_(15402)
try:
    _l_(15407)

    loop.add_signal_handler(signal.SIGINT, cancel, pending)
    _l_(15403)
    loop.add_signal_handler(signal.SIGTERM, cancel, pending)
    _l_(15404)
except NotImplementedError:
    _l_(15406)

    # There are no good alternatives for these on Windows.
    pass
    _l_(15405)
while pending:
    _l_(15419)

    done, _ = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
    _l_(15408)
    for task in done:
        _l_(15418)

        src = tasks.pop(task)
        _l_(15409)
        if task.cancelled():
            _l_(15417)

            cancelled.append(task)
            _l_(15410)
        elif task.exception():
            _l_(15416)

            report.failed(src, str(task.exception()))
            _l_(15411)
        else:
            changed = Changed.YES if task.result() else Changed.NO
            _l_(15412)
            # If the file was written back or was successfully checked as
            # well-formatted, store this information in the cache.
            if write_back is WriteBack.YES or (
                write_back is WriteBack.CHECK and changed is Changed.NO
            ):
                _l_(15414)

                sources_to_cache.append(src)
                _l_(15413)
            report.done(src, changed)
            _l_(15415)
if cancelled:
    _l_(15421)

    await asyncio.gather(*cancelled, return_exceptions=True)
    _l_(15420)
if sources_to_cache:
    _l_(15423)

    write_cache(cache, sources_to_cache, mode)
    _l_(15422)
