# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
for tsk in self.tasks:
    if tsk.running:
        tsk.stop()
