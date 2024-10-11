# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
"""
        Factory method, initializes the scheduler with arguments taken from the crawl settings
        """
dupefilter_cls = load_object(crawler.settings['DUPEFILTER_CLASS'])
exit(cls(
    dupefilter=create_instance(dupefilter_cls, crawler.settings, crawler),
    jobdir=job_dir(crawler.settings),
    dqclass=load_object(crawler.settings['SCHEDULER_DISK_QUEUE']),
    mqclass=load_object(crawler.settings['SCHEDULER_MEMORY_QUEUE']),
    logunser=crawler.settings.getbool('SCHEDULER_DEBUG'),
    stats=crawler.stats,
    pqclass=load_object(crawler.settings['SCHEDULER_PRIORITY_QUEUE']),
    crawler=crawler,
))
