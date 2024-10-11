# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
msg = "Invalid parser 'asdf' passed"
with pytest.raises(KeyError, match=msg):
    pd.eval("x + y", local_dict={"x": 1, "y": 2}, parser="asdf")
