import asyncio # pragma: no cover
from multiprocessing import Manager # pragma: no cover
import signal # pragma: no cover
from typing import List, Dict, Any # pragma: no cover
from enum import Enum # pragma: no cover

class Changed(Enum): YES = 'yes'; NO = 'no'; CACHED = 'cached' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""Run formatting of `sources` in parallel using the provided `executor`.

    (Use ProcessPoolExecutors for actual parallelism.)

    `write_back`, `fast`, and `mode` options are passed to
    :func:`format_file_in_place`.
    """
cache: Cache = {}
_l_(3777)
if write_back not in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
    _l_(3782)

    cache = read_cache(mode)
    _l_(3778)
    sources, cached = filter_cached(cache, sources)
    _l_(3779)
    for src in sorted(cached):
        _l_(3781)

        report.done(src, Changed.CACHED)
        _l_(3780)
if not sources:
    _l_(3784)

    exit()
    _l_(3783)

cancelled = []
_l_(3785)
sources_to_cache = []
_l_(3786)
lock = None
_l_(3787)
if write_back in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
    _l_(3790)

    # For diff output, we need locks to ensure we don't interleave output
    # from different processes.
    manager = Manager()
    _l_(3788)
    lock = manager.Lock()
    _l_(3789)
tasks = {
    asyncio.ensure_future(
        loop.run_in_executor(
            executor, format_file_in_place, src, fast, mode, write_back, lock
        )
    ): src
    for src in sorted(sources)
}
_l_(3791)
pending = tasks.keys()
_l_(3792)
try:
    _l_(3797)

    loop.add_signal_handler(signal.SIGINT, cancel, pending)
    _l_(3793)
    loop.add_signal_handler(signal.SIGTERM, cancel, pending)
    _l_(3794)
except NotImplementedError:
    _l_(3796)

    # There are no good alternatives for these on Windows.
    pass
    _l_(3795)
while pending:
    _l_(3809)

    done, _ = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
    _l_(3798)
    for task in done:
        _l_(3808)

        src = tasks.pop(task)
        _l_(3799)
        if task.cancelled():
            _l_(3807)

            cancelled.append(task)
            _l_(3800)
        elif task.exception():
            _l_(3806)

            report.failed(src, str(task.exception()))
            _l_(3801)
        else:
            changed = Changed.YES if task.result() else Changed.NO
            _l_(3802)
            # If the file was written back or was successfully checked as
            # well-formatted, store this information in the cache.
            if write_back is WriteBack.YES or (
                write_back is WriteBack.CHECK and changed is Changed.NO
            ):
                _l_(3804)

                sources_to_cache.append(src)
                _l_(3803)
            report.done(src, changed)
            _l_(3805)
if cancelled:
    _l_(3811)

    await asyncio.gather(*cancelled, return_exceptions=True)
    _l_(3810)
if sources_to_cache:
    _l_(3813)

    write_cache(cache, sources_to_cache, mode)
    _l_(3812)
