# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/load_op.py
if reader_func is None:
    reader_func = lambda datasets: datasets.interleave(  # pylint:disable=g-long-lambda
        lambda x: x,
        cycle_length=multiprocessing.cpu_count(),
        num_parallel_calls=dataset_ops.AUTOTUNE)

self._path = path
if element_spec is None:
    if not context.executing_eagerly():
        raise ValueError(
            "In graph mode the `element_spec` argument must be provided.")
    with gfile.GFile(
        os.path.join(path, dataset_ops.DATASET_SPEC_FILENAME), "rb") as f:
        encoded_spec = f.read()
    struct_pb = nested_structure_coder.struct_pb2.StructuredValue()
    struct_pb.ParseFromString(encoded_spec)
    spec = nested_structure_coder.decode_proto(struct_pb)
    self._element_spec = spec
else:
    self._element_spec = element_spec
self._compression = compression
self._reader_func = structured_function.StructuredFunctionWrapper(
    reader_func,
    "load()",
    # Dataset of datasets of input elements
    input_structure=dataset_ops.DatasetSpec(
        dataset_ops.DatasetSpec(self._element_spec)))

variant_tensor = ged_ops.load_dataset(
    path,
    reader_func_other_args=self._reader_func.function.captured_inputs,
    compression=compression,
    reader_func=self._reader_func.function,
    **self._flat_structure)
super().__init__(variant_tensor)
