# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
"""Installs the :mod:`~twisted.internet.reactor` with the specified
    import path. Also installs the asyncio event loop with the specified import
    path if the asyncio reactor is enabled"""
reactor_class = load_object(reactor_path)
if reactor_class is asyncioreactor.AsyncioSelectorReactor:
    with suppress(error.ReactorAlreadyInstalledError):
        event_loop = set_asyncio_event_loop(event_loop_path)
        asyncioreactor.install(eventloop=event_loop)
else:
    *module, _ = reactor_path.split(".")
    installer_path = module + ["install"]
    installer = load_object(".".join(installer_path))
    with suppress(error.ReactorAlreadyInstalledError):
        installer()
