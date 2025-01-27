# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
number_of_steps = constant_op.constant(0.0)
product_of_means = constant_op.constant(2.0)
for x in dist_dataset:  # loop with values modified each iteration
    number_of_steps += 1
    product_of_means *= math_ops.cast(
        distribution.reduce("MEAN", x, axis=0), product_of_means.dtype)

for y in dist_dataset:  # loop with no intermediate state
    distribution.run(train_step, args=(y,))

exit((number_of_steps, product_of_means))
