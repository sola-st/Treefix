# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
print("Graph Creation: Static Unroll vs. Dynamic Unroll LSTM")
print("max_t \t dt(static) \t dt(dynamic) \t dt(dynamic)/dt(static)")
for max_time in (1, 25, 50):
    s_dt, d_dt = graph_creation_static_vs_dynamic_rnn_benchmark(max_time)
    self.report_benchmark(
        name="graph_creation_time_static_T%02d" % max_time,
        iters=5,
        wall_time=s_dt)
    self.report_benchmark(
        name="graph_creation_time_dynamic_T%02d" % max_time,
        iters=5,
        wall_time=d_dt)
