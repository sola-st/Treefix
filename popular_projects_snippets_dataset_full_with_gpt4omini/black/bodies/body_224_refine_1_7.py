import asyncio # pragma: no cover
import sys # pragma: no cover

def err(message): sys.stderr.write(message + '\n') # pragma: no cover

import asyncio # pragma: no cover
import sys # pragma: no cover

def err(message): sys.stderr.write(message + '\n') # pragma: no cover
async def main(): # pragma: no cover
    tasks = [asyncio.create_task(asyncio.sleep(1))] # pragma: no cover
    err("Aborted!") # pragma: no cover
    for task in tasks: # pragma: no cover
        task.cancel() # pragma: no cover
asyncio.run(main()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/concurrency.py
from l3.Runtime import _l_
"""asyncio signal handler that cancels all `tasks` and reports to stderr."""
err("Aborted!")
_l_(8769)
for task in tasks:
    _l_(8771)

    task.cancel()
    _l_(8770)
