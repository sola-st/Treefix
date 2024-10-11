# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Register a custom template filter, available application wide.  Like
        :meth:`Flask.add_template_filter` but for a blueprint.  Works exactly
        like the :meth:`app_template_filter` decorator.

        :param name: the optional name of the filter, otherwise the
                     function name will be used.
        """

def register_template(state: BlueprintSetupState) -> None:
    state.app.jinja_env.filters[name or f.__name__] = f

self.record_once(register_template)
