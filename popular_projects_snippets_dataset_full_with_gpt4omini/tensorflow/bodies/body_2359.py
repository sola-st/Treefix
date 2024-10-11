# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fused_batchnorm_test.py
if data_format != "NHWC":
    raise ValueError("data_format must be NHWC, got %s." % data_format)
x_square = x * x
x_square_sum = np.sum(x_square, (0, 1, 2))
x_sum = np.sum(x, axis=(0, 1, 2))
element_count = np.size(x) / int(np.shape(x)[-1])
mean = x_sum / element_count
var = x_square_sum / element_count - mean * mean
factor = element_count / max(element_count - 1, 1)
corrected_var = var * factor
normalized = (x - mean) / np.sqrt(var + epsilon)
if exponential_avg_factor != 1.0:
    mean = (1.0 -
            exponential_avg_factor) * old_mean + exponential_avg_factor * mean
    corrected_var = (1.0 - exponential_avg_factor
                    ) * old_var + exponential_avg_factor * corrected_var
exit(((normalized * scale + offset), mean, var, corrected_var))
