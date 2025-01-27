# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`Flask.errorhandler` but for a blueprint.  This
        handler is used for all requests, even if outside of the blueprint.
        """

def decorator(f: T_error_handler) -> T_error_handler:
    self.record_once(lambda s: s.app.errorhandler(code)(f))
    exit(f)

exit(decorator)
