# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.shuffle(10, reshuffle_each_iteration=True)
iterator = iter(dataset)
ckpt = trackable_utils.Checkpoint(
    step=variables.Variable(0), iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, self.get_temp_dir(), max_to_keep=3)

iter1 = [next(iterator).numpy() for _ in range(5)]

manager.save()
iter2 = [next(iterator).numpy() for _ in range(5)]

ckpt.restore(manager.latest_checkpoint)
iter3 = [next(iterator).numpy() for _ in range(5)]

self.assertNotEqual(iter1, iter2)
self.assertCountEqual(iter2, iter3)
