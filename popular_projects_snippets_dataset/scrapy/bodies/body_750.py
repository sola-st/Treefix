# Extracted from ./data/repos/scrapy/scrapy/commands/bench.py
from scrapy.utils.test import get_testenv
pargs = [sys.executable, '-u', '-m', 'scrapy.utils.benchserver']
self.proc = subprocess.Popen(pargs, stdout=subprocess.PIPE,
                             env=get_testenv())
self.proc.stdout.readline()
