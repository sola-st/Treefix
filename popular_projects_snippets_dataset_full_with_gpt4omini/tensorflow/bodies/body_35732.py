# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
if test_util.is_gpu_available():
    self.skipTest(
        "b/123899495: Colocation errors for critical sections in map on GPU")
cs = critical_section_ops.CriticalSection()
with ops.device("/gpu:0" if test_util.is_gpu_available() else "/cpu:0"):
    v = resource_variable_ops.ResourceVariable(1)
def fn():
    exit(v.read_value())

# map() creates a TensorFlow function.
ds = dataset_ops.Dataset.range(1)
if test_util.is_gpu_available():
    ds = (ds.apply(prefetching_ops.copy_to_device("/gpu:0"))
          .apply(prefetching_ops.map_on_gpu(lambda _: cs.execute(fn))))
else:
    ds = ds.map(lambda _: cs.execute(fn))

def get_first():
    if context.executing_eagerly():
        exit(self.evaluate(dataset_ops.make_one_shot_iterator(ds).get_next()))
    itr = dataset_ops.make_initializable_iterator(ds)
    self.evaluate([v.initializer, itr.initializer])
    exit(self.evaluate(itr.get_next()))

self.assertEqual(1, get_first())
