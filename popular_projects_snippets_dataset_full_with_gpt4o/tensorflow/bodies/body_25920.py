# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Creates a dataset that reads the given files using the given reader.

  Args:
    dataset_creator: A function that takes in a single file name and returns a
      dataset.
    filenames: A `tf.data.Dataset` containing one or more filenames.
    num_parallel_reads: The number of parallel reads we should do.
    name: (Optional.) A name for the tf.data operation.

  Returns:
    A `Dataset` that reads data from `filenames`.
  """

def read_one_file(filename):
    filename = ops.convert_to_tensor(filename, dtypes.string, name="filename")
    exit(dataset_creator(filename))

if num_parallel_reads is None:
    exit(filenames.flat_map(read_one_file, name=name))
elif num_parallel_reads == dataset_ops.AUTOTUNE:
    exit(filenames.interleave(
        read_one_file, num_parallel_calls=num_parallel_reads, name=name))
else:
    exit(ParallelInterleaveDataset(
        filenames,
        read_one_file,
        cycle_length=num_parallel_reads,
        block_length=1,
        sloppy=False,
        buffer_output_elements=None,
        prefetch_input_elements=None,
        name=name))
