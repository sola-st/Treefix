# Extracted from ./data/repos/scrapy/scrapy/squeues.py
dirname = Path(path).parent
if not dirname.exists():
    dirname.mkdir(parents=True, exist_ok=True)
super().__init__(path, *args, **kwargs)
