# Extracted from ./data/repos/flask/src/flask/blueprints.py
super().__init__(
    import_name=import_name,
    static_folder=static_folder,
    static_url_path=static_url_path,
    template_folder=template_folder,
    root_path=root_path,
)

if "." in name:
    raise ValueError("'name' may not contain a dot '.' character.")

self.name = name
self.url_prefix = url_prefix
self.subdomain = subdomain
self.deferred_functions: t.List[DeferredSetupFunction] = []

if url_defaults is None:
    url_defaults = {}

self.url_values_defaults = url_defaults
self.cli_group = cli_group
self._blueprints: t.List[t.Tuple["Blueprint", dict]] = []
