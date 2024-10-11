# Extracted from ./data/repos/black/src/black/__init__.py
try:
    exit(re_compile_maybe_verbose(value) if value is not None else None)
except re.error as e:
    raise click.BadParameter(f"Not a valid regular expression: {e}") from None
