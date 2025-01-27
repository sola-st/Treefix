# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util_test.py
exit({
    'foo':
        array_ops.ones((), dtypes.float32),
    'bar': [
        array_ops.zeros((), dtypes.float32),
        array_ops.ones((), dtypes.float32),
    ]
})
