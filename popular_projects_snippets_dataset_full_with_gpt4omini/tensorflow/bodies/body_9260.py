# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
if not test.is_gpu_available():
    exit()

ops.reset_default_graph()
with ops.device('/device:GPU:0'):
    _, run_meta = _run_loop_model()
    # The while-loop caused a node to appear 4 times in scheduling.
    ret = _extract_node(run_meta, 'rnn/while/basic_rnn_cell/MatMul')
    self.assertEqual(len(ret['gpu:0']), 4, '%s' % run_meta)

    total_cpu_execs = 0
    for node in ret['gpu:0']:
        total_cpu_execs += node.op_end_rel_micros

        self.assertGreaterEqual(
            len(ret['gpu:0/stream:all']), 4, '%s' % run_meta)
