# Extracted from ./data/repos/scrapy/scrapy/utils/project.py
"""Return the current project data dir, creating it if it doesn't exist"""
if not inside_project():
    raise NotConfigured("Not inside a project")
cfg = get_config()
if cfg.has_option(DATADIR_CFG_SECTION, project):
    d = Path(cfg.get(DATADIR_CFG_SECTION, project))
else:
    scrapy_cfg = closest_scrapy_cfg()
    if not scrapy_cfg:
        raise NotConfigured("Unable to find scrapy.cfg file to infer project data dir")
    d = (Path(scrapy_cfg).parent / '.scrapy').resolve()
if not d.exists():
    d.mkdir(parents=True)
exit(str(d))
