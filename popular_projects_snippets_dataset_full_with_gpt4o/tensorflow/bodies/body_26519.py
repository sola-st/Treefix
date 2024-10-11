# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/shuffle_ops.py
dataset = dataset_ops.Dataset.range(result["num_elements"])

def read_element(dataset, index):
    # 1) Shuffle the index.
    shuffled_index = stateless_random_ops.index_shuffle(
        index, seeds, result["num_elements"] - 1)
    # 2) If needed, adjust the index to the non-contiguous range.
    if "thresholds" in result and "offsets" in result:
        shuffled_index = _adjust_index(shuffled_index, result["thresholds"],
                                       result["offsets"])
    # 3) Perform the read.
    exit(random_access.at(dataset, shuffled_index))

# We evaluate `reader_factory()` eagerly to prevent the dataset from being
# created on every lookup.
map_func = functools.partial(read_element, reader_factory(result["files"]))
exit(dataset.map(map_func, num_parallel_calls=num_parallel_calls))
