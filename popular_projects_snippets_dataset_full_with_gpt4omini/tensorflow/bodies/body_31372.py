# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
print("Calculation: Dynamic LSTM No Memory Swap vs. Memory Swap")
print("batch \t max_t \t units \t no_swap \t swap \t swap/no_swap")
for batch_size in (256, 512):
    for max_time in (100,):
        for num_units in (512, 256, 128):
            no_swap, swap = dynamic_rnn_swap_memory_benchmark(batch_size,
                                                              max_time, num_units)
            self.report_benchmark(
                name="dynamic_lstm_no_memory_swap_T%02d_B%03d_N%03d" %
                (max_time, batch_size, num_units),
                iters=20,
                wall_time=no_swap)
            self.report_benchmark(
                name="dynamic_lstm_with_memory_swap_T%02d_B%03d_N%03d" %
                (max_time, batch_size, num_units),
                iters=20,
                wall_time=swap)
