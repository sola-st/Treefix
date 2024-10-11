# Extracted from ./data/repos/scrapy/scrapy/extensions/telnet.py
if not crawler.settings.getbool('TELNETCONSOLE_ENABLED'):
    raise NotConfigured
if not TWISTED_CONCH_AVAILABLE:
    raise NotConfigured(
        'TELNETCONSOLE_ENABLED setting is True but required twisted '
        'modules failed to import:\n' + _TWISTED_CONCH_TRACEBACK)
self.crawler = crawler
self.noisy = False
self.portrange = [int(x) for x in crawler.settings.getlist('TELNETCONSOLE_PORT')]
self.host = crawler.settings['TELNETCONSOLE_HOST']
self.username = crawler.settings['TELNETCONSOLE_USERNAME']
self.password = crawler.settings['TELNETCONSOLE_PASSWORD']

if not self.password:
    self.password = binascii.hexlify(os.urandom(8)).decode('utf8')
    logger.info('Telnet Password: %s', self.password)

self.crawler.signals.connect(self.start_listening, signals.engine_started)
self.crawler.signals.connect(self.stop_listening, signals.engine_stopped)
