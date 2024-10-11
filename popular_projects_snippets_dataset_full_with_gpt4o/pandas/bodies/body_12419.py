# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH39247; this test makes sure that if a user provides mode="*t" or "*b",
# it is used. In the case of this test it leads to an error as intentionally the
# wrong mode is requested
expected = tm.makeDataFrame()
with io_class() as buffer:
    with pytest.raises(TypeError, match=msg):
        expected.to_csv(buffer, mode=f"w{mode}")
