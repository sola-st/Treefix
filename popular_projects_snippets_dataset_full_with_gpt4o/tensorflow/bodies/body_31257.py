# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
cpu_stats = None
gpu_stats = None
step_stats = run_metadata.step_stats
for ds in step_stats.dev_stats:
    if "cpu:0" in ds.device[-5:].lower():
        cpu_stats = ds.node_stats
    if "gpu:0" == ds.device[-5:].lower():
        gpu_stats = ds.node_stats
exit((cpu_stats, gpu_stats))
