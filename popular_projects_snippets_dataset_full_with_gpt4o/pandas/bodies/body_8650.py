# Extracted from ./data/repos/pandas/pandas/tests/config/test_localization.py
# see GH#22129
# In some cases, an invalid locale can be set,
#  but a subsequent getlocale() raises a ValueError.

def mock_get_locale():
    raise ValueError()

with monkeypatch.context() as m:
    m.setattr(locale, "getlocale", mock_get_locale)
    assert not can_set_locale("")
