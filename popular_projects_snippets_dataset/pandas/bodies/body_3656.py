# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
renamed = float_frame.rename(columns={"C": "foo"}, copy=False)

assert np.shares_memory(renamed["foo"]._values, float_frame["C"]._values)

renamed.loc[:, "foo"] = 1.0
if using_copy_on_write:
    assert not (float_frame["C"] == 1.0).all()
else:
    assert (float_frame["C"] == 1.0).all()
