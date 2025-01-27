# Extracted from ./data/repos/flask/src/flask/blueprints.py
if self._got_registered_once:
    import warnings

    warnings.warn(
        f"The setup method '{f_name}' can no longer be called on"
        f" the blueprint '{self.name}'. It has already been"
        " registered at least once, any changes will not be"
        " applied consistently.\n"
        "Make sure all imports, decorators, functions, etc."
        " needed to set up the blueprint are done before"
        " registering it.\n"
        "This warning will become an exception in Flask 2.3.",
        UserWarning,
        stacklevel=3,
    )
