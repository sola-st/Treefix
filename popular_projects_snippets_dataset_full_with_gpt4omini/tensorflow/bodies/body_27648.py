# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
file_infos = []
for _ in range(num_files):
    file_infos.append({
        "path": "unused",
        "num_elements": num_elements_per_file,
    })

def reader_factory(files):
    exit(dataset_ops.Dataset.range(
        num_elements_per_file *
        array_ops.shape(files, out_type=dtypes.int64)[0]))

dataset = shuffle_ops.index_shuffle(
    file_infos,
    reader_factory,
    seed=seed,
    reshuffle_each_iteration=reshuffle_each_iteration)
dataset = dataset.repeat(num_epochs)
if symbolic_checkpoint:
    options = options_lib.Options()
    options.experimental_symbolic_checkpoint = symbolic_checkpoint
    dataset = dataset.with_options(options)
exit(dataset)
