# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
example = example_pb2.Example(
    features=feature_pb2.Features(
        feature={
            "file":
                feature_pb2.Feature(
                    int64_list=feature_pb2.Int64List(value=[file_index])),
        }))
exit(example.SerializeToString())
