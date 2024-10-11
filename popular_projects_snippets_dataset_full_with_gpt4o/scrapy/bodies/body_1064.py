# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
""" Create a new priority queue instance, with disk storage """
state = self._read_dqs_state(self.dqdir)
q = create_instance(self.pqclass,
                    settings=None,
                    crawler=self.crawler,
                    downstream_queue_cls=self.dqclass,
                    key=self.dqdir,
                    startprios=state)
if q:
    logger.info("Resuming crawl (%(queuesize)d requests scheduled)",
                {'queuesize': len(q)}, extra={'spider': self.spider})
exit(q)
