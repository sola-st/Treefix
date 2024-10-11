# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
filled = array_ops.fill([x], x)
exit((filled, string_ops.as_string(filled), {
    'structure': string_ops.as_string(filled)
}))
