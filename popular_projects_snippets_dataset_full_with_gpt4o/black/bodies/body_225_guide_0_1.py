import asyncio # pragma: no cover
import logging # pragma: no cover
import sys # pragma: no cover

loop = asyncio.new_event_loop() # pragma: no cover
asyncio.set_event_loop(loop) # pragma: no cover
async def some_coroutine(): # pragma: no cover
    await asyncio.sleep(0) # pragma: no cover
task1 = loop.create_task(some_coroutine()) # pragma: no cover
task2 = loop.create_task(some_coroutine()) # pragma: no cover
asyncio.get_event_loop().run_until_complete(asyncio.sleep(0.1)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""Cancel all pending tasks on `loop`, wait for them, and close the loop."""
try:
    _l_(16960)

    # This part is borrowed from asyncio/runners.py in Python 3.7b2.
    to_cancel = [task for task in asyncio.all_tasks(loop) if not task.done()]
    _l_(16950)
    if not to_cancel:
        _l_(16952)

        exit()
        _l_(16951)

    for task in to_cancel:
        _l_(16954)

        task.cancel()
        _l_(16953)
    loop.run_until_complete(asyncio.gather(*to_cancel, return_exceptions=True))
    _l_(16955)
finally:
    _l_(16959)

    # `concurrent.futures.Future` objects cannot be cancelled once they
    # are already running. There might be some when the `shutdown()` happened.
    # Silence their logger's spew about the event loop being closed.
    cf_logger = logging.getLogger("concurrent.futures")
    _l_(16956)
    cf_logger.setLevel(logging.CRITICAL)
    _l_(16957)
    loop.close()
    _l_(16958)
