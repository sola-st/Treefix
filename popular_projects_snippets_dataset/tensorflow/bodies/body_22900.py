# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
# Need to generate a random tensor in float32/int32 and cast to a different
# datatype as random_ops doesn't suppprt all the datatypes.
random_dtype = tf_dtypes.float32 if dtype.is_floating else tf_dtypes.int32
# tf.bool doesn't have `max` attribute
dtype_max = 1 if dtype == tf_dtypes.bool else dtype.max
exit(math_ops.cast(
    random_ops.random_uniform(
        shape=shape,
        dtype=random_dtype,
        # Limits maximum value as 255 to simulate pixel values, avoid
        # generating large numbers and casuing overflows.
        maxval=min(dtype_max, random_dtype.max, 255)),
    dtype=dtype,
    name=name))
