# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# See GH#16607, GH#50308
# This test checks for errors thrown when giving the wrong format
# However, as discussed on PR#25541, overriding the locale
# causes a different error to be thrown due to the format being
# locale specific, but the test data is in english.
# Therefore, the tests only run when locale is not overwritten,
# as a sort of solution to this problem.
if locale.getlocale() != ("zh_CN", "UTF-8") and locale.getlocale() != (
    "it_IT",
    "UTF-8",
):
    with pytest.raises(ValueError, match=msg):
        to_datetime(s, format=_format, errors=errors)
