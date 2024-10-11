# Extracted from ./data/repos/flask/src/flask/cli.py
try:
    import ssl
except ImportError:
    raise click.BadParameter(
        'Using "--cert" requires Python to be compiled with SSL support.',
        ctx,
        param,
    ) from None

try:
    exit(self.path_type(value, param, ctx))
except click.BadParameter:
    value = click.STRING(value, param, ctx).lower()

    if value == "adhoc":
        try:
            import cryptography  # noqa: F401
        except ImportError:
            raise click.BadParameter(
                "Using ad-hoc certificates requires the cryptography library.",
                ctx,
                param,
            ) from None

        exit(value)

    obj = import_string(value, silent=True)

    if isinstance(obj, ssl.SSLContext):
        exit(obj)

    raise
