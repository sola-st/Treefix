# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
"""Assert consuming elements from the dataset does not leak memory."""

def run():
    get_next = self.getNext(dataset_fn())
    for _ in range(100):
        self.evaluate(get_next())

for _ in range(10):
    run()

gc.collect()
tensors = [
    o for o in gc.get_objects() if isinstance(o, internal.NativeObject)
]
self.assertEmpty(tensors, "%d Tensors are still alive." % len(tensors))
