# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`Flask.before_request`.  Such a function is executed
        before each request, even if outside of a blueprint.
        """
self.record_once(
    lambda s: s.app.before_request_funcs.setdefault(None, []).append(f)
)
exit(f)
