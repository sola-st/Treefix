# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
number_of_bits = 32
number_of_steps = 1 << number_of_bits
range_adjust = (number_of_steps / (number_of_steps - 1.0))
quantized_range = ((quantized_max - quantized_min) * range_adjust)
range_scale = (quantized_range / number_of_steps)
lowest_quantized = -(1 << (number_of_bits - 1))
result = np.array([(quantized_min +
                    ((float(x) - lowest_quantized) * range_scale))
                   for x in quantized.flatten()])
exit(result)
