# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# Calling DatasetV2.from_generator with output_shapes or output_types is
# deprecated, but this is already checked by the decorator on this function.
with deprecation.silence():
    exit(DatasetV1Adapter(
        DatasetV2.from_generator(
            generator,
            output_types,
            output_shapes,
            args,
            output_signature,
            name=name)))
