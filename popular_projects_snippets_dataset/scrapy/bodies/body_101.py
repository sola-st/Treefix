# Extracted from ./data/repos/scrapy/scrapy/shell.py
# disable accidental Ctrl-C key press from shutting down the engine
signal.signal(signal.SIGINT, signal.SIG_IGN)
if url:
    self.fetch(url, spider, redirect=redirect)
elif request:
    self.fetch(request, spider)
elif response:
    request = response.request
    self.populate_vars(response, request, spider)
else:
    self.populate_vars()
if self.code:
    print(eval(self.code, globals(), self.vars))
else:
    """
            Detect interactive shell setting in scrapy.cfg
            e.g.: ~/.config/scrapy.cfg or ~/.scrapy.cfg
            [settings]
            # shell can be one of ipython, bpython or python;
            # to be used as the interactive python console, if available.
            # (default is ipython, fallbacks in the order listed above)
            shell = python
            """
    cfg = get_config()
    section, option = 'settings', 'shell'
    env = os.environ.get('SCRAPY_PYTHON_SHELL')
    shells = []
    if env:
        shells += env.strip().lower().split(',')
    elif cfg.has_option(section, option):
        shells += [cfg.get(section, option).strip().lower()]
    else:  # try all by default
        shells += DEFAULT_PYTHON_SHELLS.keys()
    # always add standard shell as fallback
    shells += ['python']
    start_python_console(self.vars, shells=shells,
                         banner=self.vars.pop('banner', ''))
