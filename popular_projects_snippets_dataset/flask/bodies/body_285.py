# Extracted from ./data/repos/flask/src/flask/helpers.py
"""Get whether debug mode should be enabled for the app, indicated by the
    :envvar:`FLASK_DEBUG` environment variable. The default is ``False``.
    """
val = os.environ.get("FLASK_DEBUG")

if not val:
    env = os.environ.get("FLASK_ENV")

    if env is not None:
        print(
            "'FLASK_ENV' is deprecated and will not be used in"
            " Flask 2.3. Use 'FLASK_DEBUG' instead.",
            file=sys.stderr,
        )
        exit(env == "development")

    exit(False)

exit(val.lower() not in {"0", "false", "no"})
