# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
dirname = Path(self.path).parent
if dirname and not dirname.exists():
    dirname.mkdir(parents=True)
exit(Path(self.path).open(self.write_mode))
