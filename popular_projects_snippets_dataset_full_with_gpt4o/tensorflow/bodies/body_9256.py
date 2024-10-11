# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
if not test.is_gpu_available(cuda_only=True):
    exit()

gpu_dev = test.gpu_device_name()
ops.reset_default_graph()
with ops.device(gpu_dev):
    _, run_meta = _run_model()

mm = _extract_node(run_meta, 'MatMul')['gpu:0'][0]
mm_allocs = mm.memory[0].allocation_records
# has allocation and deallocation.
self.assertEqual(len(mm_allocs), 2)
# first allocated.
self.assertGreater(mm_allocs[1].alloc_micros, mm_allocs[0].alloc_micros)
self.assertGreater(mm_allocs[0].alloc_bytes, 0)
# Then deallocated.
self.assertLess(mm_allocs[1].alloc_bytes, 0)
# All memory deallocated.
self.assertEqual(mm_allocs[0].alloc_bytes + mm_allocs[1].alloc_bytes, 0)

rand = _extract_node(run_meta,
                     'random_normal/RandomStandardNormal')['gpu:0'][0]
random_allocs = rand.memory[0].allocation_records
# random normal must allocated first since matmul depends on it.
self.assertLess(random_allocs[0].alloc_micros, mm.all_start_micros)
# deallocates the memory after matmul started.
self.assertGreater(random_allocs[1].alloc_micros, mm.all_start_micros)
