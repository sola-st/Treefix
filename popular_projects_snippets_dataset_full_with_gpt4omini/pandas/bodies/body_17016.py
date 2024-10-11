# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
constructor = dict if mapping == "dict" else non_dict_mapping_subclass
frames = constructor(
    {
        "foo": DataFrame(np.random.randn(4, 3)),
        "bar": DataFrame(np.random.randn(4, 3)),
        "baz": DataFrame(np.random.randn(4, 3)),
        "qux": DataFrame(np.random.randn(4, 3)),
    }
)

sorted_keys = list(frames.keys())

result = concat(frames)
expected = concat([frames[k] for k in sorted_keys], keys=sorted_keys)
tm.assert_frame_equal(result, expected)

result = concat(frames, axis=1)
expected = concat([frames[k] for k in sorted_keys], keys=sorted_keys, axis=1)
tm.assert_frame_equal(result, expected)

keys = ["baz", "foo", "bar"]
result = concat(frames, keys=keys)
expected = concat([frames[k] for k in keys], keys=keys)
tm.assert_frame_equal(result, expected)
