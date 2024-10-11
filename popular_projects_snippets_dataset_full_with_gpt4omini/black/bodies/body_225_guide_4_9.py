import asyncio # pragma: no cover
import logging # pragma: no cover

loop = asyncio.new_event_loop() # pragma: no cover
asyncio.set_event_loop(loop) # pragma: no cover
async def incomplete_task(): await asyncio.sleep(10) # pragma: no cover
for _ in range(1): loop.create_task(incomplete_task()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""Cancel all pending tasks on `loop`, wait for them, and close the loop."""
try:
    _l_(5192)

    # This part is borrowed from asyncio/runners.py in Python 3.7b2.
    to_cancel = [task for task in asyncio.all_tasks(loop) if not task.done()]
    _l_(5182)
    if not to_cancel:
        _l_(5184)

        exit()
        _l_(5183)

    for task in to_cancel:
        _l_(5186)

        task.cancel()
        _l_(5185)
    loop.run_until_complete(asyncio.gather(*to_cancel, return_exceptions=True))
    _l_(5187)
finally:
    _l_(5191)

    # `concurrent.futures.Future` objects cannot be cancelled once they
    # are already running. There might be some when the `shutdown()` happened.
    # Silence their logger's spew about the event loop being closed.
    cf_logger = logging.getLogger("concurrent.futures")
    _l_(5188)
    cf_logger.setLevel(logging.CRITICAL)
    _l_(5189)
    loop.close()
    _l_(5190)
