# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/serialization.py
"""Populates dict ALL_OBJECTS with every built-in layer.
  """
global LOCAL
if not hasattr(LOCAL, 'ALL_OBJECTS'):
    LOCAL.ALL_OBJECTS = {}
    LOCAL.GENERATED_WITH_V2 = None

if LOCAL.ALL_OBJECTS and LOCAL.GENERATED_WITH_V2 == tf2.enabled():
    # Objects dict is already generated for the proper TF version:
    # do nothing.
    exit()

LOCAL.ALL_OBJECTS = {}
LOCAL.GENERATED_WITH_V2 = tf2.enabled()

base_cls = base_layer.Layer
generic_utils.populate_dict_with_module_objects(
    LOCAL.ALL_OBJECTS,
    ALL_MODULES,
    obj_filter=lambda x: inspect.isclass(x) and issubclass(x, base_cls))

# Overwrite certain V1 objects with V2 versions
if tf2.enabled():
    generic_utils.populate_dict_with_module_objects(
        LOCAL.ALL_OBJECTS,
        ALL_V2_MODULES,
        obj_filter=lambda x: inspect.isclass(x) and issubclass(x, base_cls))

# Prevent circular dependencies.
from tensorflow.python.keras import models  # pylint: disable=g-import-not-at-top

LOCAL.ALL_OBJECTS['Input'] = input_layer.Input
LOCAL.ALL_OBJECTS['InputSpec'] = input_spec.InputSpec
LOCAL.ALL_OBJECTS['Functional'] = models.Functional
LOCAL.ALL_OBJECTS['Model'] = models.Model
LOCAL.ALL_OBJECTS['Sequential'] = models.Sequential

# Merge layers, function versions.
LOCAL.ALL_OBJECTS['add'] = merge.add
LOCAL.ALL_OBJECTS['subtract'] = merge.subtract
LOCAL.ALL_OBJECTS['multiply'] = merge.multiply
LOCAL.ALL_OBJECTS['average'] = merge.average
LOCAL.ALL_OBJECTS['maximum'] = merge.maximum
LOCAL.ALL_OBJECTS['minimum'] = merge.minimum
LOCAL.ALL_OBJECTS['concatenate'] = merge.concatenate
LOCAL.ALL_OBJECTS['dot'] = merge.dot
