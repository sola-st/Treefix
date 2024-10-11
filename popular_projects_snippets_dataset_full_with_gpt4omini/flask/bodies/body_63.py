# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Same as :meth:`url_defaults` but application wide."""
self.record_once(
    lambda s: s.app.url_default_functions.setdefault(None, []).append(f)
)
exit(f)
