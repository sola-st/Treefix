# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
updated_cf = transform.transform_function(
    f, inputs=args, transform_fn=transform_fn)
exit(updated_cf(*args))
