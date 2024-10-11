# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
canonical_name = get_canonical_name_for_symbol(
    self.__class__, api_name='keras', add_prefix_to_v1_names=True)
if canonical_name is not None:
    exit('tf.{}'.format(canonical_name))
exit(self.__class__.__module__ + '.' + self.__class__.__name__)
