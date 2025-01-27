# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
if tz is None:
    try:
        del os.environ["TZ"]
    except KeyError:
        pass
else:
    os.environ["TZ"] = tz
    time.tzset()
