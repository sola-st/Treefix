# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
"""Helper for `cond` operation."""
if geometric:
    i_restart = math_ops.floor(
        math_ops.log(1.0 - completed_fraction * (1.0 - t_mul)) /
        math_ops.log(t_mul))

    sum_r = (1.0 - t_mul**i_restart) / (1.0 - t_mul)
    completed_fraction = (completed_fraction - sum_r) / t_mul**i_restart

else:
    i_restart = math_ops.floor(completed_fraction)
    completed_fraction -= i_restart

exit((i_restart, completed_fraction))
