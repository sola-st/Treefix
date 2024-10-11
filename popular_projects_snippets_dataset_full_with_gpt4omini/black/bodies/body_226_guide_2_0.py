import os # pragma: no cover
import sys # pragma: no cover
import asyncio # pragma: no cover
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, Executor # pragma: no cover

workers = 1 # pragma: no cover
sources = ['file1.py', 'file2.py'] # pragma: no cover
fast = False # pragma: no cover
write_back = True # pragma: no cover
mode = 'format' # pragma: no cover
report = None # pragma: no cover
executor = None # pragma: no cover
def maybe_install_uvloop(): pass # pragma: no cover
def schedule_formatting(sources, fast, write_back, mode, report, loop, executor): return asyncio.sleep(0) # pragma: no cover
def shutdown(loop): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""Reformat multiple files using a ProcessPoolExecutor."""
maybe_install_uvloop()
_l_(6011)

executor: Executor
_l_(6012)
if workers is None:
    _l_(6014)

    workers = os.cpu_count() or 1
    _l_(6013)
if sys.platform == "win32":
    _l_(6016)

    # Work around https://bugs.python.org/issue26903
    workers = min(workers, 60)
    _l_(6015)
try:
    _l_(6020)

    executor = ProcessPoolExecutor(max_workers=workers)
    _l_(6017)
except (ImportError, NotImplementedError, OSError):
    _l_(6019)

    # we arrive here if the underlying system does not support multi-processing
    # like in AWS Lambda or Termux, in which case we gracefully fallback to
    # a ThreadPoolExecutor with just a single worker (more workers would not do us
    # any good due to the Global Interpreter Lock)
    executor = ThreadPoolExecutor(max_workers=1)
    _l_(6018)

loop = asyncio.new_event_loop()
_l_(6021)
asyncio.set_event_loop(loop)
_l_(6022)
try:
    _l_(6031)

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
    _l_(6023)
finally:
    _l_(6030)

    try:
        _l_(6027)

        shutdown(loop)
        _l_(6024)
    finally:
        _l_(6026)

        asyncio.set_event_loop(None)
        _l_(6025)
    if executor is not None:
        _l_(6029)

        executor.shutdown()
        _l_(6028)
