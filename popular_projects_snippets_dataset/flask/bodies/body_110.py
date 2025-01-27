# Extracted from ./data/repos/flask/src/flask/app.py
self.config["DEBUG"] = value

if self.config["TEMPLATES_AUTO_RELOAD"] is None:
    self.jinja_env.auto_reload = value
