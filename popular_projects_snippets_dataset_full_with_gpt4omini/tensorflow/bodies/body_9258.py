# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
ops.reset_default_graph()
with ops.device('/cpu:0'):
    tfprof_node, run_meta = _run_loop_model()
    # The while-loop caused a node to appear 4 times in scheduling.
    ret = _extract_node(run_meta, 'rnn/while/basic_rnn_cell/MatMul')
    self.assertEqual(len(ret['cpu:0']), 4)

    total_cpu_execs = 0
    for node in ret['cpu:0']:
        total_cpu_execs += node.op_end_rel_micros

    mm_node = lib.SearchTFProfNode(tfprof_node,
                                   'rnn/while/basic_rnn_cell/MatMul')

    self.assertEqual(mm_node.run_count, 4)
    self.assertEqual(mm_node.cpu_exec_micros, total_cpu_execs)
    self.assertEqual(mm_node.exec_micros, total_cpu_execs)
