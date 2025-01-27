# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_invalid.py

# trying to concat a ndframe with a non-ndframe
df1 = tm.makeCustomDataframe(10, 2)
for obj in [1, {}, [1, 2], (1, 2)]:

    msg = (
        f"cannot concatenate object of type '{type(obj)}'; "
        "only Series and DataFrame objs are valid"
    )
    with pytest.raises(TypeError, match=msg):
        concat([df1, obj])
