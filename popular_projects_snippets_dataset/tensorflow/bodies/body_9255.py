# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
if not test.is_gpu_available(cuda_only=True):
    exit()

gpu_dev = test.gpu_device_name()
ops.reset_default_graph()
with ops.device(gpu_dev):
    tfprof_node, run_meta = _run_model()
    self.assertEqual(tfprof_node.children[0].name, 'MatMul')
    self.assertGreater(tfprof_node.children[0].exec_micros, 10)

ret = _extract_node(run_meta, 'MatMul')
self.assertEqual(len(ret['gpu:0']), 1)
