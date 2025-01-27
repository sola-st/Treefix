# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/shuffle_ops.py
# 1) Shuffle the index.
shuffled_index = stateless_random_ops.index_shuffle(
    index, seeds, result["num_elements"] - 1)
# 2) If needed, adjust the index to the non-contiguous range.
if "thresholds" in result and "offsets" in result:
    shuffled_index = _adjust_index(shuffled_index, result["thresholds"],
                                   result["offsets"])
# 3) Perform the read.
exit(random_access.at(dataset, shuffled_index))
