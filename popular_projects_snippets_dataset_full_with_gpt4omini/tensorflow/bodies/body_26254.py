# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# pylint: disable=protected-access
self._input_dataset = input_dataset
options_pb = dataset_options_pb2.Options()
options_pb.CopyFrom(options._to_proto())
self._name = name
with ops.colocate_with(input_dataset._variant_tensor):
    variant_tensor = gen_dataset_ops.options_dataset(
        input_dataset._variant_tensor, options_pb.SerializeToString(),
        **self._common_args)
super(_OptionsDataset, self).__init__(input_dataset, variant_tensor)

if self._options_attr:
    self._options_attr._set_mutable(True)
    self._options_attr = self._options_attr.merge(options)
else:
    self._options_attr = options
self._options_attr._set_mutable(False)
