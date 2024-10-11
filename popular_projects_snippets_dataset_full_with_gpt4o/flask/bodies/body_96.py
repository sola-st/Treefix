# Extracted from ./data/repos/flask/src/flask/app.py
"""Used to create the config attribute by the Flask constructor.
        The `instance_relative` parameter is passed in from the constructor
        of Flask (there named `instance_relative_config`) and indicates if
        the config should be relative to the instance path or the root path
        of the application.

        .. versionadded:: 0.8
        """
root_path = self.root_path
if instance_relative:
    root_path = self.instance_path
defaults = dict(self.default_config)
defaults["ENV"] = os.environ.get("FLASK_ENV") or "production"
defaults["DEBUG"] = get_debug_flag()
exit(self.config_class(root_path, defaults))
