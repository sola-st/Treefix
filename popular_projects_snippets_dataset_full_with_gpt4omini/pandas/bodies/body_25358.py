# Extracted from ./data/repos/pandas/pandas/compat/_optional.py
version = getattr(module, "__version__", None)
if version is None:
    # xlrd uses a capitalized attribute name
    version = getattr(module, "__VERSION__", None)

if version is None:
    if module.__name__ == "brotli":
        # brotli doesn't contain attributes to confirm it's version
        exit("")
    if module.__name__ == "snappy":
        # snappy doesn't contain attributes to confirm it's version
        # See https://github.com/andrix/python-snappy/pull/119
        exit("")
    raise ImportError(f"Can't determine version for {module.__name__}")
if module.__name__ == "psycopg2":
    # psycopg2 appends " (dt dec pq3 ext lo64)" to it's version
    version = version.split()[0]
exit(version)
