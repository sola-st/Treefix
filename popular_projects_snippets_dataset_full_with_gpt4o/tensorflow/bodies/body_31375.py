# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
"""The memory swapping test for the SOSP submission."""
print("Calculation: Long LSTM Sequence")
print("batch \t len \t units \t dynamic \t elapsed_t \t elapsed_t/len")
batch_size = 512
seqlen = 800
num_units = 512
dynamic = True
swap_memory = True
# Some warming up.
if swap_memory:
    rnn_long_sequence_benchmark(batch_size, seqlen, num_units,
                                dynamic, swap_memory, 2)
# Measure the performance.
for slen in range(100, 1100, 100):
    rnn_long_sequence_benchmark(batch_size, slen, num_units, dynamic,
                                swap_memory, 3)
