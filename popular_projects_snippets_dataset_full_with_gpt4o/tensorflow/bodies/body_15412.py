# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
# Ops that should be listed as supported in both v1 and v2.
supported_ops = [
    'bitcast', 'bitwise.bitwise_and', 'bitwise.bitwise_or',
    'bitwise.bitwise_xor', 'bitwise.invert', 'bitwise.left_shift',
    'bitwise.right_shift', 'clip_by_value', 'concat',
    'debugging.assert_equal', 'debugging.assert_near',
    'debugging.assert_none_equal', 'debugging.assert_greater',
    'debugging.assert_greater_equal', 'debugging.assert_less',
    'debugging.assert_less_equal', 'debugging.check_numerics',
    'cast', 'dtypes.complex',
    'dtypes.saturate_cast', 'expand_dims', 'gather_nd', 'gather',
    'io.decode_base64', 'io.decode_compressed', 'io.encode_base64',
    'math.abs', 'math.acos', 'math.acosh', 'math.add_n', 'math.add',
    'math.angle', 'math.asin', 'math.asinh', 'math.atan2', 'math.atan',
    'math.atanh', 'math.bessel_i0', 'math.bessel_i0e', 'math.bessel_i1',
    'math.bessel_i1e', 'math.ceil', 'math.conj', 'math.cos', 'math.cosh',
    'math.digamma', 'math.divide_no_nan', 'math.divide', 'math.equal',
    'math.erf', 'math.erfc', 'math.erfcinv', 'math.erfinv', 'math.exp',
    'math.expm1', 'math.floor', 'math.floordiv', 'math.floormod',
    'math.greater_equal', 'math.greater', 'math.imag', 'math.is_finite',
    'math.is_inf', 'math.is_nan', 'math.less_equal', 'math.less',
    'math.lgamma', 'math.log1p', 'math.log_sigmoid', 'math.log',
    'math.logical_and', 'math.logical_not', 'math.logical_or',
    'math.logical_xor', 'math.maximum', 'math.minimum',
    'math.multiply_no_nan', 'math.multiply', 'math.negative',
    'math.nextafter', 'math.not_equal', 'math.pow', 'math.real',
    'math.reciprocal', 'math.reciprocal_no_nan', 'math.reduce_any',
    'math.reduce_max', 'math.reduce_mean', 'math.reduce_variance',
    'math.reduce_std', 'math.reduce_min', 'math.reduce_prod',
    'math.reduce_sum', 'math.rint', 'math.round', 'math.rsqrt', 'math.sign',
    'math.sigmoid', 'math.sin', 'math.sinh', 'math.softplus', 'math.sqrt',
    'math.square', 'math.squared_difference', 'math.subtract', 'math.tan',
    'math.tanh', 'math.truediv', 'math.unsorted_segment_max',
    'math.unsorted_segment_mean', 'math.unsorted_segment_min',
    'math.unsorted_segment_prod', 'math.unsorted_segment_sqrt_n',
    'math.unsorted_segment_sum', 'one_hot', 'ones_like', 'rank', 'realdiv',
    'math.reduce_all', 'size', 'split', 'squeeze', 'stack',
    'strings.as_string', 'strings.join', 'strings.length',
    'strings.reduce_join', 'strings.regex_full_match',
    'strings.regex_replace', 'strings.strip', 'strings.substr',
    'strings.to_hash_bucket_fast', 'strings.to_hash_bucket_strong',
    'strings.to_hash_bucket', 'strings.to_number', 'strings.unicode_script',
    'tile', 'truncatediv', 'truncatemod', 'zeros_like', 'dynamic_partition',
    'reverse', 'nn.dropout', 'strings.format', 'print'
]

# Ops that should be listed as supported in v1 only.
supported_ops_v1 = ['batch_gather']

# Ops that should be listed as supported in v2 only.
supported_ops_v2 = ['nn.softmax']

v1_ragged_ops = ragged_dispatch.ragged_op_list(tf_version=1)
for element in supported_ops + supported_ops_v1:
    self.assertIn('`tf.' + element + '`', v1_ragged_ops)
for element in supported_ops_v2:
    self.assertNotIn('`tf.' + element + '`', v1_ragged_ops)

v2_ragged_ops = ragged_dispatch.ragged_op_list(tf_version=2)
for element in supported_ops + supported_ops_v2:
    self.assertIn('`tf.' + element + '`', v2_ragged_ops)
for element in supported_ops_v1:
    self.assertNotIn('`tf.' + element + '`', v2_ragged_ops)
