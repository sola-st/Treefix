# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
dataset = dataset_ops.Dataset.range(20)
map_fn = lambda x: dataset_ops.Dataset.range(20 * x, 20 * (x + 1))
dataset = dataset.apply(
    interleave_ops.parallel_interleave(
        map_fn,
        cycle_length=3,
        sloppy=False,
        buffer_output_elements=1,
        prefetch_input_elements=0))
dataset = dataset.batch(32)

results = []
for _ in range(2):
    elements = []
    next_element = self.getNext(dataset)
    try:
        while True:
            elements.extend(self.evaluate(next_element()))
    except errors.OutOfRangeError:
        pass
    results.append(elements)
self.assertAllEqual(results[0], results[1])
