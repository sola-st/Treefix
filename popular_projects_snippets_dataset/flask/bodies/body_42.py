# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`Flask.add_url_rule` but for a blueprint.  The endpoint for
        the :func:`url_for` function is prefixed with the name of the blueprint.
        """
if endpoint and "." in endpoint:
    raise ValueError("'endpoint' may not contain a dot '.' character.")

if view_func and hasattr(view_func, "__name__") and "." in view_func.__name__:
    raise ValueError("'view_func' name may not contain a dot '.' character.")

self.record(
    lambda s: s.add_url_rule(
        rule,
        endpoint,
        view_func,
        provide_automatic_options=provide_automatic_options,
        **options,
    )
)
