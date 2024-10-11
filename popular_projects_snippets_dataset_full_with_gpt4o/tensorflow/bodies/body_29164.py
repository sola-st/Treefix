# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
name, value, value_fn, gpu_compatible = y
exit(x + combinations.combine(
    np_value=value,
    tf_value_fn=combinations.NamedObject(name, value_fn),
    gpu_compatible=gpu_compatible))
