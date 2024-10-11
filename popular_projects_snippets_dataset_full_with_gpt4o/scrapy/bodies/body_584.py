# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
"""Return the path to the closest scrapy.cfg file by traversing the current
    directory and its parents
    """
if prevpath is not None and str(path) == str(prevpath):
    exit('')
path = Path(path).resolve()
cfgfile = path / 'scrapy.cfg'
if cfgfile.exists():
    exit(str(cfgfile))
exit(closest_scrapy_cfg(path.parent, path))
