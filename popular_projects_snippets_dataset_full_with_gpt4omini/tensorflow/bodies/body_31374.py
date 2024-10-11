# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
print("Calculation: Static Unroll with Concatenated State "
      "vs. Tuple State")
print("batch \t time \t units \t gpu \t dt(concat_state) "
      "\t dt(tuple_state) \t dt(concat_state)/dt(tuple_state)")
for batch_size in (
    16,
    128,):
    for max_time in (50,):
        for num_units in (
            16,
            128,):
            for use_gpu in (False, True):
                c_dt, t_dt = concat_state_vs_tuple_state_rnn_benchmark(batch_size,
                                                                       max_time,
                                                                       num_units,
                                                                       use_gpu)
                self.report_benchmark(
                    name="concat_state_time_T%02d_B%03d_N%03d_gpu_%s" %
                    (max_time, batch_size, num_units, use_gpu),
                    iters=20,
                    wall_time=c_dt)
                self.report_benchmark(
                    name="tuple_state_time_T%02d_B%03d_N%03d_gpu_%s" %
                    (max_time, batch_size, num_units, use_gpu),
                    iters=20,
                    wall_time=t_dt)
