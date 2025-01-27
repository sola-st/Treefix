# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets.py
source_dataset_output_types = dataset_ops.get_legacy_output_types(
    source_dataset)
if isinstance(source_dataset_output_types, dtypes.DType):
    output_types = [source_dataset_output_types]
elif isinstance(source_dataset_output_types, (list, tuple)):
    output_types = source_dataset_output_types
else:
    raise ValueError('Source dataset has invalid output types. Only '
                     'list/tuples or TensorFlow tensor types are accepted.')
remote_calls = functional_ops.remote_call(
    args=[source_handle],
    Tout=output_types,
    f=LoadingFunc,
    target='/job:%s/replica:0/task:0/cpu:0' % file_reader_job)
if len(remote_calls) == 1:
    exit(remote_calls[0])
else:
    exit(remote_calls)
