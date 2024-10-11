# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/__init__.py
"""Populates dict ALL_OBJECTS with every built-in initializer.
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

# Compatibility aliases (need to exist in both V1 and V2).
LOCAL.ALL_OBJECTS['ConstantV2'] = initializers_v2.Constant
LOCAL.ALL_OBJECTS['GlorotNormalV2'] = initializers_v2.GlorotNormal
LOCAL.ALL_OBJECTS['GlorotUniformV2'] = initializers_v2.GlorotUniform
LOCAL.ALL_OBJECTS['HeNormalV2'] = initializers_v2.HeNormal
LOCAL.ALL_OBJECTS['HeUniformV2'] = initializers_v2.HeUniform
LOCAL.ALL_OBJECTS['IdentityV2'] = initializers_v2.Identity
LOCAL.ALL_OBJECTS['LecunNormalV2'] = initializers_v2.LecunNormal
LOCAL.ALL_OBJECTS['LecunUniformV2'] = initializers_v2.LecunUniform
LOCAL.ALL_OBJECTS['OnesV2'] = initializers_v2.Ones
LOCAL.ALL_OBJECTS['OrthogonalV2'] = initializers_v2.Orthogonal
LOCAL.ALL_OBJECTS['RandomNormalV2'] = initializers_v2.RandomNormal
LOCAL.ALL_OBJECTS['RandomUniformV2'] = initializers_v2.RandomUniform
LOCAL.ALL_OBJECTS['TruncatedNormalV2'] = initializers_v2.TruncatedNormal
LOCAL.ALL_OBJECTS['VarianceScalingV2'] = initializers_v2.VarianceScaling
LOCAL.ALL_OBJECTS['ZerosV2'] = initializers_v2.Zeros

# Out of an abundance of caution we also include these aliases that have
# a non-zero probability of having been included in saved configs in the past.
LOCAL.ALL_OBJECTS['glorot_normalV2'] = initializers_v2.GlorotNormal
LOCAL.ALL_OBJECTS['glorot_uniformV2'] = initializers_v2.GlorotUniform
LOCAL.ALL_OBJECTS['he_normalV2'] = initializers_v2.HeNormal
LOCAL.ALL_OBJECTS['he_uniformV2'] = initializers_v2.HeUniform
LOCAL.ALL_OBJECTS['lecun_normalV2'] = initializers_v2.LecunNormal
LOCAL.ALL_OBJECTS['lecun_uniformV2'] = initializers_v2.LecunUniform

if tf2.enabled():
    # For V2, entries are generated automatically based on the content of
    # initializers_v2.py.
    v2_objs = {}
    base_cls = initializers_v2.Initializer
    generic_utils.populate_dict_with_module_objects(
        v2_objs,
        [initializers_v2],
        obj_filter=lambda x: inspect.isclass(x) and issubclass(x, base_cls))
    for key, value in v2_objs.items():
        LOCAL.ALL_OBJECTS[key] = value
        # Functional aliases.
        LOCAL.ALL_OBJECTS[generic_utils.to_snake_case(key)] = value
else:
    # V1 initializers.
    v1_objs = {
        'Constant': init_ops.Constant,
        'GlorotNormal': init_ops.GlorotNormal,
        'GlorotUniform': init_ops.GlorotUniform,
        'Identity': init_ops.Identity,
        'Ones': init_ops.Ones,
        'Orthogonal': init_ops.Orthogonal,
        'VarianceScaling': init_ops.VarianceScaling,
        'Zeros': init_ops.Zeros,
        'HeNormal': initializers_v1.HeNormal,
        'HeUniform': initializers_v1.HeUniform,
        'LecunNormal': initializers_v1.LecunNormal,
        'LecunUniform': initializers_v1.LecunUniform,
        'RandomNormal': initializers_v1.RandomNormal,
        'RandomUniform': initializers_v1.RandomUniform,
        'TruncatedNormal': initializers_v1.TruncatedNormal,
    }
    for key, value in v1_objs.items():
        LOCAL.ALL_OBJECTS[key] = value
        # Functional aliases.
        LOCAL.ALL_OBJECTS[generic_utils.to_snake_case(key)] = value

  # More compatibility aliases.
LOCAL.ALL_OBJECTS['normal'] = LOCAL.ALL_OBJECTS['random_normal']
LOCAL.ALL_OBJECTS['uniform'] = LOCAL.ALL_OBJECTS['random_uniform']
LOCAL.ALL_OBJECTS['one'] = LOCAL.ALL_OBJECTS['ones']
LOCAL.ALL_OBJECTS['zero'] = LOCAL.ALL_OBJECTS['zeros']
