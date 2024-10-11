# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
size = self.resource.getrusage(self.resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    # on macOS ru_maxrss is in bytes, on Linux it is in KB
    size *= 1024
exit(size)
