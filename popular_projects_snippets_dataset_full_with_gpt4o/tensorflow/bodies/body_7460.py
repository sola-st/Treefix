# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
global_batch_size = 8
dataset = self.dataset.batch(global_batch_size).prefetch(2)

distributed_dataset = strategy.experimental_distribute_dataset(dataset)
element = next(iter(distributed_dataset))
batched_image, batched_label = element
self.assertEqual(batched_image.shape, [global_batch_size, 8, 8, 3])
self.assertEqual(batched_label.shape, [global_batch_size, 1])

# Make sure when unpack the tensor, each of them has enough shards.
self.assertLen(d_api.unpack(batched_image), self.mesh.num_local_devices())
self.assertLen(d_api.unpack(batched_label), self.mesh.num_local_devices())
