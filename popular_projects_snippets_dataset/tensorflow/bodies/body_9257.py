# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
ops.reset_default_graph()
with ops.device('/cpu:0'):
    tfprof_node, run_meta = _run_model()
    self.assertEqual(tfprof_node.children[0].name, 'MatMul')
    self.assertGreater(tfprof_node.children[0].exec_micros, 0)

ret = _extract_node(run_meta, 'MatMul')
self.assertEqual(len(ret['cpu:0']), 1)

ret = _extract_node(run_meta, 'MatMul:MatMul')
self.assertEqual(len(ret), 0)
