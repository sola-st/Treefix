# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
print("Calculation: Static Unroll with Dynamic Flow LSTM "
      "vs. Dynamic Unroll LSTM")
print("batch \t max_t \t units \t gpu \t dt(static) \t dt(dynamic) "
      "\t dt(dynamic)/dt(static)")
for batch_size in (256,):
    for max_time in (50,):
        for num_units in (512, 256, 128):
            for use_gpu in (False, True):
                s_dt, d_dt = static_vs_dynamic_rnn_benchmark(batch_size, max_time,
                                                             num_units, use_gpu)
                self.report_benchmark(
                    name="static_unroll_time_T%02d_B%03d_N%03d_gpu_%s" %
                    (max_time, batch_size, num_units, use_gpu),
                    iters=20,
                    wall_time=s_dt)
                self.report_benchmark(
                    name="dynamic_unroll_time_T%02d_B%03d_N%03d_gpu_%s" %
                    (max_time, batch_size, num_units, use_gpu),
                    iters=20,
                    wall_time=d_dt)
