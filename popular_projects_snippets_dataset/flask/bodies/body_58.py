# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`Flask.teardown_request` but for a blueprint.  Such a
        function is executed when tearing down each request, even if outside of
        the blueprint.
        """
self.record_once(
    lambda s: s.app.teardown_request_funcs.setdefault(None, []).append(f)
)
exit(f)
