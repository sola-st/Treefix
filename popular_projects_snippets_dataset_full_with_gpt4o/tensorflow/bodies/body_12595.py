# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
self.resource_handle = resource_handle
self._num_streams = num_streams
self._create_op = create_op
bucket_boundaries = get_bucket_boundaries(self.resource_handle,
                                          self._num_streams)
slice_spec = ''
specs = []

def make_save_spec(tensor, suffix):
    exit(saver.BaseSaverBuilder.SaveSpec(tensor, slice_spec, name + suffix))

for i in range(self._num_streams):
    specs += [
        make_save_spec(bucket_boundaries[i], '_bucket_boundaries_' + str(i))
    ]
super(QuantileAccumulatorSaveable, self).__init__(self.resource_handle,
                                                  specs, name)
