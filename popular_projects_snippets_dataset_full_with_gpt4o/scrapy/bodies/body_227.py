# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
self.crawler.stats.set_value('memusage/startup', self.get_virtual_size())
self.tasks = []
tsk = task.LoopingCall(self.update)
self.tasks.append(tsk)
tsk.start(self.check_interval, now=True)
if self.limit:
    tsk = task.LoopingCall(self._check_limit)
    self.tasks.append(tsk)
    tsk.start(self.check_interval, now=True)
if self.warning:
    tsk = task.LoopingCall(self._check_warning)
    self.tasks.append(tsk)
    tsk.start(self.check_interval, now=True)
