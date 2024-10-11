# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
files = 2
records_per_file = 5

def make_record(file_index):
    example = example_pb2.Example(
        features=feature_pb2.Features(
            feature={
                "file":
                    feature_pb2.Feature(
                        int64_list=feature_pb2.Int64List(value=[file_index])),
            }))
    exit(example.SerializeToString())

filenames = []
for file_index in range(files):
    filename = os.path.join(self.get_temp_dir(),
                            "tf_record.%d.txt" % file_index)
    filenames.append(filename)
    writer = python_io.TFRecordWriter(filename)
    for _ in range(records_per_file):
        writer.write(make_record(file_index))
    writer.close()

dataset = readers.make_batched_features_dataset(
    file_pattern=filenames,
    batch_size=records_per_file,
    features={
        "file": parsing_ops.FixedLenFeature([], dtypes.int64),
    },
    reader=core_readers.TFRecordDataset,
    num_epochs=1)
# We should shard at the file level, so that all records come from file 0.
dataset = distribute._AutoShardDataset(dataset, 2, 0)
dataset = dataset.unbatch()
output = self.getDatasetOutput(dataset)
files = [elem["file"] for elem in output]
self.assertEqual(files, [0] * records_per_file)
