# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
if '://' in basedir:
    basedir = basedir.split('://', 1)[1]
self.basedir = basedir
self._mkdir(Path(self.basedir))
self.created_directories: DefaultDict[str, Set[str]] = defaultdict(set)
