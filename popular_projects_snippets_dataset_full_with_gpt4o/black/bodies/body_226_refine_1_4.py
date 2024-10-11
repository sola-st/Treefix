from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # pragma: no cover
import asyncio # pragma: no cover
import os # pragma: no cover
import sys # pragma: no cover

def maybe_install_uvloop(): pass # pragma: no cover
Executor = object # pragma: no cover
workers = None # pragma: no cover
sources = [] # pragma: no cover
fast = False # pragma: no cover
write_back = 'replace' # pragma: no cover
mode = 'auto' # pragma: no cover
report = None # pragma: no cover
def schedule_formatting(sources, fast, write_back, mode, report, loop, executor): pass # pragma: no cover
def shutdown(loop): pass # pragma: no cover

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # pragma: no cover
import asyncio # pragma: no cover
import os # pragma: no cover
import sys # pragma: no cover

def maybe_install_uvloop(): pass # pragma: no cover
Executor = object # pragma: no cover
workers = None # pragma: no cover
sources = ['file1.py', 'file2.py'] # pragma: no cover
fast = False # pragma: no cover
write_back = 'replace' # pragma: no cover
mode = 'auto' # pragma: no cover
report = None # pragma: no cover
async def dummy_coroutine(): pass # pragma: no cover
async def schedule_formatting(sources, fast, write_back, mode, report, loop, executor): await dummy_coroutine() # pragma: no cover
def shutdown(loop): loop.close() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""Reformat multiple files using a ProcessPoolExecutor."""
maybe_install_uvloop()
_l_(17808)

executor: Executor
_l_(17809)
if workers is None:
    _l_(17811)

    workers = os.cpu_count() or 1
    _l_(17810)
if sys.platform == "win32":
    _l_(17813)

    # Work around https://bugs.python.org/issue26903
    workers = min(workers, 60)
    _l_(17812)
try:
    _l_(17817)

    executor = ProcessPoolExecutor(max_workers=workers)
    _l_(17814)
except (ImportError, NotImplementedError, OSError):
    _l_(17816)

    # we arrive here if the underlying system does not support multi-processing
    # like in AWS Lambda or Termux, in which case we gracefully fallback to
    # a ThreadPoolExecutor with just a single worker (more workers would not do us
    # any good due to the Global Interpreter Lock)
    executor = ThreadPoolExecutor(max_workers=1)
    _l_(17815)

loop = asyncio.new_event_loop()
_l_(17818)
asyncio.set_event_loop(loop)
_l_(17819)
try:
    _l_(17828)

    loop.run_until_complete(
        schedule_formatting(
            sources=sources,
            fast=fast,
            write_back=write_back,
            mode=mode,
            report=report,
            loop=loop,
            executor=executor,
        )
    )
    _l_(17820)
finally:
    _l_(17827)

    try:
        _l_(17824)

        shutdown(loop)
        _l_(17821)
    finally:
        _l_(17823)

        asyncio.set_event_loop(None)
        _l_(17822)
    if executor is not None:
        _l_(17826)

        executor.shutdown()
        _l_(17825)
