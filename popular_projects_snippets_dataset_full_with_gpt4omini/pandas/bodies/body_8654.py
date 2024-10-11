# Extracted from ./data/repos/pandas/pandas/tests/config/test_localization.py
system_locale = os.environ.get("LC_ALL")
system_encoding = system_locale.split(".")[-1] if system_locale else "utf-8"

assert (
    codecs.lookup(pd.options.display.encoding).name
    == codecs.lookup(system_encoding).name
)
