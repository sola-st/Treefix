# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
with self.cached_session() as sess:
    decay = 0.5
    weight = array_ops.placeholder(dtypes.bfloat16, [])
    val = array_ops.placeholder(dtypes.bfloat16, [])

    wma = moving_averages.weighted_moving_average(val, decay, weight)
    self.evaluate(variables.global_variables_initializer())

    # Get the first weighted moving average.
    val_1 = 3.0
    weight_1 = 4.0
    wma_array = sess.run(wma, feed_dict={val: val_1, weight: weight_1})
    numerator_1 = val_1 * weight_1 * (1.0 - decay)
    denominator_1 = weight_1 * (1.0 - decay)
    self.assertAllClose(numerator_1 / denominator_1, wma_array)

    # Get the second weighted moving average.
    val_2 = 11.0
    weight_2 = 22.0
    wma_array = sess.run(wma, feed_dict={val: val_2, weight: weight_2})
    numerator_2 = numerator_1 * decay + val_2 * weight_2 * (1.0 - decay)
    denominator_2 = denominator_1 * decay + weight_2 * (1.0 - decay)
    self.assertAllClose(
        dtypes._np_bfloat16(numerator_2 / denominator_2), wma_array)
