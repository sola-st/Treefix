# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
pyval = {"a": 12, "b": {"c": 23, "d": {"e": 11}}}
st = StructuredTensor.from_pyval(pyval)

# Try to set non-existent sub-structure.
with self.assertRaisesRegex(
    ValueError, r"cannot create new sub-field.*\('b', 'x'\).*is not set"):
    st.with_updates({("b", "x", "e"): 5})

# Try to set with path to a non-sub-structure.
with self.assertRaisesRegex(
    ValueError, r"cannot create new sub-field.*\('b', 'c'\).*is not a "
    r"`StructuredTensor`"):
    st.with_updates({("b", "c", "e"): 5})

# Try to apply function to non-existing value.
with self.assertRaisesRegex(
    ValueError, r"cannot update.*\('b', 'd', 'x'\).*does not already "
    r"exist"):
    st.with_updates({("b", "d", "x"): lambda x: x + 1})

# Empty names not allowed.
with self.assertRaisesRegex(ValueError, r"does not allow empty names"):
    st.with_updates({(): lambda x: x + 1})
with self.assertRaisesRegex(ValueError, r"does not allow empty names"):
    st.with_updates({("b", ""): lambda x: x + 1})

# Parent and child nodes cannot be updated simultaneously.
with self.assertRaisesRegex(
    ValueError, r"does not allow both parent and child nodes.*"
    r"parent=\('b'.*child=\('b', 'd'"):
    st.with_updates({("b", "d"): lambda x: x + 1, "a": 3, "b": 10})

# Invalid shape change.
with self.assertRaisesRegex(
    ValueError,
    r"`StructuredTensor.with_updates` failed for field \('c',\)"):
    st_with_shape = StructuredTensor.from_pyval([[{
        "c": {
            "a": 5,
            "b": 2
        }
    }], [{
        "c": {
            "a": 3,
            "b": 1
        }
    }, {
        "c": {
            "a": 8,
            "b": 18
        }
    }]])
    st_with_shape.with_updates({("c", "a"): 3})
