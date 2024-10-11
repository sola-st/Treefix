# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(features=features({
        "a": float_feature([1, 1, 3]),
    })),
    example(features=features({
        "a": float_feature([-1, -1]),
    }))
]

names = ["passing", "failing"]
serialized = [m.SerializeToString() for m in original]

self._test(
    {
        "example_names": names,
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a": parsing_ops.FixedLenFeature((1, 3), dtypes.float32)
        }
    },
    expected_err=(errors_impl.OpError,
                  "Name: failing, Key: a, Index: 1.  Number of float val"))
