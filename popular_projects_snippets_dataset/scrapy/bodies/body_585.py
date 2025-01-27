# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
"""Initialize environment to use command-line tool from inside a project
    dir. This sets the Scrapy settings module and modifies the Python path to
    be able to locate the project module.
    """
cfg = get_config()
if cfg.has_option('settings', project):
    os.environ['SCRAPY_SETTINGS_MODULE'] = cfg.get('settings', project)
closest = closest_scrapy_cfg()
if closest:
    projdir = str(Path(closest).parent)
    if set_syspath and projdir not in sys.path:
        sys.path.append(projdir)
