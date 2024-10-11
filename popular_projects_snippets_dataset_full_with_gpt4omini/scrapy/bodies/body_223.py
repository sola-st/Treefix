# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
task = getattr(self, 'task', False)
if task and task.active():
    task.cancel()
