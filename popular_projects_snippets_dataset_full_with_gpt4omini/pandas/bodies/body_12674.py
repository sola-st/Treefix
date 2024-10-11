# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
lc_category = locale.LC_NUMERIC

# We just need one of these locales to work.
for new_locale in ("it_IT.UTF-8", "Italian_Italy"):
    if tm.can_set_locale(new_locale, lc_category):
        with tm.set_locale(new_locale, lc_category):
            assert ujson.loads(ujson.dumps(4.78e60)) == 4.78e60
            assert ujson.loads("4.78", precise_float=True) == 4.78
        break
