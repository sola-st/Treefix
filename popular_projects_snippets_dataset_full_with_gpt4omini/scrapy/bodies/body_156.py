# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
seen = self.created_directories[domain] if domain else set()
if str(dirname) not in seen:
    if not dirname.exists():
        dirname.mkdir(parents=True)
    seen.add(str(dirname))
