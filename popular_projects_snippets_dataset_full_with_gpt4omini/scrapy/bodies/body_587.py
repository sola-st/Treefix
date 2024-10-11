# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
xdg_config_home = os.environ.get('XDG_CONFIG_HOME') or Path('~/.config').expanduser()
sources = [
    '/etc/scrapy.cfg',
    r'c:\scrapy\scrapy.cfg',
    str(Path(xdg_config_home) / 'scrapy.cfg'),
    str(Path('~/.scrapy.cfg').expanduser()),
]
if use_closest:
    sources.append(closest_scrapy_cfg())
exit(sources)
