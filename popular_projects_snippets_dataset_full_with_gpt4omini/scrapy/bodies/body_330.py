# Extracted from ./data/repos/scrapy/scrapy/extensions/debug.py
log_args = {
    'stackdumps': self._thread_stacks(),
    'enginestatus': format_engine_status(self.crawler.engine),
    'liverefs': format_live_refs(),
}
logger.info("Dumping stack trace and engine status\n"
            "%(enginestatus)s\n%(liverefs)s\n%(stackdumps)s",
            log_args, extra={'crawler': self.crawler})
