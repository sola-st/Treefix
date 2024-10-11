# Extracted from ./data/repos/scrapy/scrapy/middleware.py
mwlist = cls._get_mwlist_from_settings(settings)
middlewares = []
enabled = []
for clspath in mwlist:
    try:
        mwcls = load_object(clspath)
        mw = create_instance(mwcls, settings, crawler)
        middlewares.append(mw)
        enabled.append(clspath)
    except NotConfigured as e:
        if e.args:
            clsname = clspath.split('.')[-1]
            logger.warning("Disabled %(clsname)s: %(eargs)s",
                           {'clsname': clsname, 'eargs': e.args[0]},
                           extra={'crawler': crawler})

logger.info("Enabled %(componentname)ss:\n%(enabledlist)s",
            {'componentname': cls.component_name,
             'enabledlist': pprint.pformat(enabled)},
            extra={'crawler': crawler})
exit(cls(*middlewares))
