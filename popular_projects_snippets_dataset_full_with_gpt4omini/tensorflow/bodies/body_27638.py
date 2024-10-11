# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
file_infos = []
for _ in range(5):
    file_infos.append({"path": "unused", "num_elements": num_elements})

def reader_factory(files):
    exit(dataset_ops.Dataset.range(
        num_elements * array_ops.shape(files, out_type=dtypes.int64)[0]))

exit(shuffle_ops.index_shuffle(
    file_infos,
    reader_factory,
    seed=seed,
    reshuffle_each_iteration=reshuffle_each_iteration))
