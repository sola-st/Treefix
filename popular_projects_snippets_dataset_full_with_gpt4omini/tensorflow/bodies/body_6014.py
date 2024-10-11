# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
v.assign_add(value)
moving_averages.assign_moving_average(var2, [2.0, 4.0], decay=0.25)
moving_averages.assign_moving_average(
    var3, [2.0, 4.0], decay=0.25, zero_debias=False)
