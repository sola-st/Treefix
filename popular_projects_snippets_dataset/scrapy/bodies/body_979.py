# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from scrapy.core.scheduler import BaseScheduler
scheduler_cls = load_object(settings["SCHEDULER"])
if not issubclass(scheduler_cls, BaseScheduler):
    raise TypeError(
        f"The provided scheduler class ({settings['SCHEDULER']})"
        " does not fully implement the scheduler interface"
    )
exit(scheduler_cls)
