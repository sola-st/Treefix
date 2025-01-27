# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
other_tested_ops = [
    # Elementwise ops that have explicit/bespoke test cases in this file.
    string_ops.string_to_hash_bucket,
    string_ops.string_to_hash_bucket_v1,
    string_ops.string_to_hash_bucket_fast,
    string_ops.string_to_hash_bucket_strong,
    string_ops.string_to_number,
    string_ops.regex_full_match,
    string_ops.regex_replace,
    string_ops.substr,
    string_ops.substr_v2,
    string_ops.substr_deprecated,
    string_ops.unicode_transcode,
    clip_ops.clip_by_value,
    array_ops.check_numerics,
    math_ops.cast,
    math_ops.saturate_cast,
    math_ops.nextafter,
    math_ops.tensor_equals,
    math_ops.tensor_not_equals,
    math_ops.to_bfloat16,
    math_ops.to_complex128,
    math_ops.to_complex64,
    math_ops.to_double,
    math_ops.to_float,
    math_ops.to_int32,
    math_ops.to_int64,
    math_ops.scalar_mul,
    math_ops.scalar_mul_v2,
    image_ops_impl.adjust_brightness,
    image_ops_impl.adjust_gamma,
    image_ops_impl.stateless_random_brightness,
    image_ops_impl.random_brightness,
    image_ops_impl.convert_image_dtype,
    nn_impl.sigmoid_cross_entropy_with_logits_v2,
]
untested_ops = (
    set(dispatch.unary_elementwise_apis() +
        dispatch.binary_elementwise_apis()) -
    set(test_ops.UNARY_FLOAT_OPS + test_ops.UNARY_BOOL_OPS +
        test_ops.UNARY_STRING_OPS + test_ops.UNARY_INT_OPS +
        test_ops.BINARY_FLOAT_OPS + test_ops.BINARY_BOOL_OPS +
        test_ops.BINARY_INT_OPS + other_tested_ops))
untested_ops = sorted(f'{x.__module__}.{x.__name__}' for x in untested_ops)
self.assertEmpty(
    untested_ops, 'One or more ops elementwise are not tested; please'
    ' add them to ragged_tensor_test_ops.py or ragged_dispatch_test.py')
