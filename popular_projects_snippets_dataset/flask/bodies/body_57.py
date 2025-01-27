# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`Flask.after_request` but for a blueprint.  Such a function
        is executed after each request, even if outside of the blueprint.
        """
self.record_once(
    lambda s: s.app.after_request_funcs.setdefault(None, []).append(f)
)
exit(f)
