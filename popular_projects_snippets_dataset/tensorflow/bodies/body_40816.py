# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
count.assign_add(1)
residuals = value - model
loss = 0.5 * math_ops.reduce_mean(math_ops.pow(residuals, 2))
# Note: count is an integer, so its doutput will be None
exit((loss, count))
