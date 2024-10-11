# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
dataset = dataset_ops.Dataset.range(10)
iterator = iter(dataset)
get_next = iterator.get_next
checkpoint = trackable_utils.Checkpoint(iterator=iterator)
for i in range(5):
    checkpoint.restore(
        checkpoint_management.latest_checkpoint(
            checkpoint_directory)).initialize_or_restore()
    for j in range(2):
        self.assertEqual(i * 2 + j, self.evaluate(get_next()))
    checkpoint.save(file_prefix=checkpoint_prefix)
