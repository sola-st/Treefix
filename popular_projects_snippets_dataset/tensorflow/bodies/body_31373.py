# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
print("Calculation: Static Unroll with Halved Sequence Length "
      "vs. Half Static Unroll")
print("batch \t full_t \t units \t gpu \t dt(half_seq_len) "
      "\t dt(unroll_half) \t dt(half_seq_len)/dt(unroll_half)")
for batch_size in (128,):
    for max_time in (50,):
        for num_units in (256,):
            for use_gpu in (False, True):
                s_dt, d_dt = half_seq_len_vs_unroll_half_rnn_benchmark(batch_size,
                                                                       max_time,
                                                                       num_units,
                                                                       use_gpu)
                self.report_benchmark(
                    name="half_seq_len_time_T%02d_B%03d_N%03d_gpu_%s" %
                    (max_time, batch_size, num_units, use_gpu),
                    iters=20,
                    wall_time=s_dt)
                self.report_benchmark(
                    name="unroll_half_time_T%02d_B%03d_N%03d_gpu_%s" %
                    (max_time, batch_size, num_units, use_gpu),
                    iters=20,
                    wall_time=d_dt)
