# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
# Do not pass kwarg values here. We don't want to promote user-defined
# dicts, and we want to update, not replace, default dicts with the
# values given by the user
super().__init__()
self.setmodule(default_settings, 'default')
# Promote default dictionaries to BaseSettings instances for per-key
# priorities
for name, val in self.items():
    if isinstance(val, dict):
        self.set(name, BaseSettings(val, 'default'), 'default')
self.update(values, priority)
