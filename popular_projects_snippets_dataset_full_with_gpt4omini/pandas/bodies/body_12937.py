# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
"""
    engine gives us a pytest.param object with some marks, read_ext is just
    a string.  We need to generate a new pytest.param inheriting the marks.
    """
values = engine.values + (read_ext,)
new_param = pytest.param(values, marks=engine.marks)
exit(new_param)
