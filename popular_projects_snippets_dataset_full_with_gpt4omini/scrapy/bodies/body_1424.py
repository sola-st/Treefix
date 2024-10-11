# Extracted from ./data/repos/scrapy/scrapy/crawler.py
if isinstance(spidercls, Spider):
    raise ValueError('The spidercls argument must be a class, not an object')

if isinstance(settings, dict) or settings is None:
    settings = Settings(settings)

self.spidercls = spidercls
self.settings = settings.copy()
self.spidercls.update_settings(self.settings)

self.signals = SignalManager(self)

self.stats = load_object(self.settings['STATS_CLASS'])(self)

handler = LogCounterHandler(self, level=self.settings.get('LOG_LEVEL'))
logging.root.addHandler(handler)

d = dict(overridden_settings(self.settings))
logger.info("Overridden settings:\n%(settings)s",
            {'settings': pprint.pformat(d)})

if get_scrapy_root_handler() is not None:
    # scrapy root handler already installed: update it with new settings
    install_scrapy_root_handler(self.settings)
# lambda is assigned to Crawler attribute because this way it is not
# garbage collected after leaving __init__ scope
self.__remove_handler = lambda: logging.root.removeHandler(handler)
self.signals.connect(self.__remove_handler, signals.engine_stopped)

lf_cls = load_object(self.settings['LOG_FORMATTER'])
self.logformatter = lf_cls.from_crawler(self)

self.request_fingerprinter: RequestFingerprinter = create_instance(
    load_object(self.settings['REQUEST_FINGERPRINTER_CLASS']),
    settings=self.settings,
    crawler=self,
)

reactor_class = self.settings["TWISTED_REACTOR"]
event_loop = self.settings["ASYNCIO_EVENT_LOOP"]
if init_reactor:
    # this needs to be done after the spider settings are merged,
    # but before something imports twisted.internet.reactor
    if reactor_class:
        install_reactor(reactor_class, event_loop)
    else:
        from twisted.internet import reactor  # noqa: F401
    log_reactor_info()
if reactor_class:
    verify_installed_reactor(reactor_class)
    if is_asyncio_reactor_installed() and event_loop:
        verify_installed_asyncio_event_loop(event_loop)

self.extensions = ExtensionManager.from_crawler(self)

self.settings.freeze()
self.crawling = False
self.spider = None
self.engine: Optional[ExecutionEngine] = None
