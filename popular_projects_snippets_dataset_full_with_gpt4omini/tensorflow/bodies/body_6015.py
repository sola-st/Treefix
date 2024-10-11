# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
with distribution.scope():
    var1 = variables.Variable([0.0, 0.0])
    var2 = variables.Variable([0.0, 0.0])
    var3 = variables.Variable([0.0, 0.0])

    def update_fn(v, value):
        v.assign_add(value)
        moving_averages.assign_moving_average(var2, [2.0, 4.0], decay=0.25)
        moving_averages.assign_moving_average(
            var3, [2.0, 4.0], decay=0.25, zero_debias=False)

    distribution.extended.update(var1, update_fn, ([1.0, 1.0],))

    self.assertAllClose([2.0, 4.0], var2.read_value())
    self.assertAllClose([1.5, 3.0], var3.read_value())
