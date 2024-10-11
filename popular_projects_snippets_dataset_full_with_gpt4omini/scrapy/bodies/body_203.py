# Extracted from ./data/repos/scrapy/scrapy/extensions/telnet.py
# Note: if you add entries here also update topics/telnetconsole.rst
telnet_vars = {
    'engine': self.crawler.engine,
    'spider': self.crawler.engine.spider,
    'slot': self.crawler.engine.slot,
    'crawler': self.crawler,
    'extensions': self.crawler.extensions,
    'stats': self.crawler.stats,
    'settings': self.crawler.settings,
    'est': lambda: print_engine_status(self.crawler.engine),
    'p': pprint.pprint,
    'prefs': print_live_refs,
    'help': "This is Scrapy telnet console. For more info see: "
            "https://docs.scrapy.org/en/latest/topics/telnetconsole.html",
}
self.crawler.signals.send_catch_log(update_telnet_vars, telnet_vars=telnet_vars)
exit(telnet_vars)
