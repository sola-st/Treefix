# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
numerical_error = 1e-6  # per-operation error
moment_mean = expected[i]
moment_squared = expected[2 * i]
moment_var = moment_squared - moment_mean * moment_mean

error_per_moment = i * numerical_error
total_variance = moment_var / float(num_samples) + error_per_moment
exit(abs((real[i] - moment_mean) / math.sqrt(total_variance)))
