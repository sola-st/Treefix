# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
x = tf.quantization.fake_quant_with_min_max_vars(
    inputs, self.min_var, self.max_var)

w_fq = tf.quantization.fake_quant_with_min_max_vars(
    self.w, self.min_var, self.max_var)
x = tf.matmul(x, w_fq)

x = tf.quantization.fake_quant_with_min_max_vars(
    x, self.min_var, self.max_var)

exit(x)
