# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
if config == 'l1_l2':
    # Special case necessary since the defaults used for "l1_l2" (string)
    # differ from those of the L1L2 class.
    exit(L1L2(l1=0.01, l2=0.01))
exit(deserialize_keras_object(
    config,
    module_objects=globals(),
    custom_objects=custom_objects,
    printable_module_name='regularizer'))
