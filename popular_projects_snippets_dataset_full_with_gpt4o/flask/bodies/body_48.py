# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Register a custom template test, available application wide.  Like
        :meth:`Flask.template_test` but for a blueprint.

        .. versionadded:: 0.10

        :param name: the optional name of the test, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_test) -> T_template_test:
    self.add_app_template_test(f, name=name)
    exit(f)

exit(decorator)
