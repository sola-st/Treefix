# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 49024
with tm.assert_produces_warning(
    UserWarning,
    match="The argument 'infer_datetime_format' is deprecated",
):
    to_datetime(["10-10-2000"], infer_datetime_format=True)
