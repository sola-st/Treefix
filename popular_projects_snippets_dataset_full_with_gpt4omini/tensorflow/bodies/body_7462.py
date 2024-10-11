# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
# TODO(b/210887657): Support last partial batch.
self.skipTest('Test failed due to last partial batch')
dataset = dataset_ops.Dataset.from_tensors(
    (self.images, self.labels)).repeat(30)  # There is a last partial batch

strategy = mirrored_strategy.MirroredStrategy(self.mesh)
global_batch_size = 8
dataset = dataset.batch(global_batch_size).prefetch(2)

distributed_dataset = strategy.experimental_distribute_dataset(dataset)
expected_element_batch_size = [8, 8, 8, 6]
# The last batch with 6 element will fail to produce with StopIteration.
iterator = iter(distributed_dataset)
for batch_size in expected_element_batch_size:
    element = next(iterator)
    batched_image, batched_label = element
    self.assertEqual(batched_image.shape, [batch_size, 8, 8, 3])
    self.assertEqual(batched_label.shape, [batch_size, 1])

    # Make sure when unpack the tensor, each of them has enough shards.
    self.assertLen(d_api.unpack(batched_image), self.mesh.num_local_devices())
    self.assertLen(d_api.unpack(batched_label), self.mesh.num_local_devices())
