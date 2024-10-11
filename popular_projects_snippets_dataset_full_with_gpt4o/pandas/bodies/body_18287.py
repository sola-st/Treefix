# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# invalid ops
box = box_with_array

obj_ser = tm.makeObjectSeries()
obj_ser.name = "objects"

obj_ser = tm.box_expected(obj_ser, box)
msg = "|".join(
    ["can only concatenate str", "unsupported operand type", "must be str"]
)
with pytest.raises(Exception, match=msg):
    op(obj_ser, 1)
with pytest.raises(Exception, match=msg):
    op(obj_ser, np.array(1, dtype=np.int64))
