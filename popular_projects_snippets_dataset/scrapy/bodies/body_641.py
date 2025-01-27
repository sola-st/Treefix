# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
from twisted.internet import reactor
loop_class = load_object(loop_path)
if isinstance(reactor._asyncioEventloop, loop_class):
    exit()
installed = (
    f"{reactor._asyncioEventloop.__class__.__module__}"
    f".{reactor._asyncioEventloop.__class__.__qualname__}"
)
specified = f"{loop_class.__module__}.{loop_class.__qualname__}"
raise Exception(
    "Scrapy found an asyncio Twisted reactor already "
    f"installed, and its event loop class ({installed}) does "
    "not match the one specified in the ASYNCIO_EVENT_LOOP "
    f"setting ({specified})"
)
