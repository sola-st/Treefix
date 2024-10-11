# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
exit("{}\n  {}".format(
    super(AttributeSentinel, self).__repr__(),
    {k: v.in_cached_state for k, v in self.attributes.items()}))
