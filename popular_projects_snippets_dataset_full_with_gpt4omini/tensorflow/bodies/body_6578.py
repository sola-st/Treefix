# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if tf2.enabled():
    self.skipTest("Only V1 is supported.")
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:CPU:0"])]
dataset_fn = lambda _: dataset_ops.DatasetV1.range(10)

input_workers = input_lib.InputWorkers(worker_device_pairs)

dist_dataset = input_util.get_distributed_dataset(
    dataset_fn(distribute_lib.InputContext()), input_workers, distribution)

iterator = dataset_ops.make_one_shot_iterator(dist_dataset)

@def_function.function
def init_func_for_iter():
    self.evaluate(iterator.initializer)

init_func_for_iter()
