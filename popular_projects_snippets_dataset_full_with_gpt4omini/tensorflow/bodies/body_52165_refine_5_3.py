import numpy as np # pragma: no cover

_normalize_feature_columns = lambda x: x # pragma: no cover
_DenseColumn = type('MockDenseColumn', (object,), {}) # pragma: no cover
weight_collections = None # pragma: no cover
ops = type('MockOps', (object,), {'GraphKeys': type('GraphKeys', (object,), {'GLOBAL_VARIABLES': 'global_variables', 'MODEL_VARIABLES': 'model_variables'})}) # pragma: no cover
from_template = False # pragma: no cover
variable_scope = type('MockVariableScope', (object,), {'variable_scope': staticmethod(lambda *args, **kwargs: None), 'get_variable_scope': staticmethod(lambda: type('MockVarScope', (object,), {'name': 'mock_scope'})())}) # pragma: no cover
scope = 'input_layer_scope' # pragma: no cover
features = {'feature1': np.array([[1.0], [2.0]]), 'feature2': np.array([[3.0], [4.0]])} # pragma: no cover
_LazyBuilder = type('MockLazyBuilder', (object,), {'__init__': lambda self, features: None}) # pragma: no cover
trainable = True # pragma: no cover
array_ops = type('MockArrayOps', (object,), {'shape': staticmethod(lambda x: np.shape(x)), 'reshape': staticmethod(lambda x, shape: np.reshape(x, shape)), 'concat': staticmethod(lambda tensors, axis: np.concatenate(tensors, axis=axis))}) # pragma: no cover
cols_to_vars = {} # pragma: no cover
cols_to_output_tensors = {} # pragma: no cover
_verify_static_batch_size_equality = lambda output_tensors, ordered_columns: None # pragma: no cover

_normalize_feature_columns = lambda x: x # pragma: no cover
_DenseColumn = type('MockDenseColumn', (object,), {}) # pragma: no cover
weight_collections = [] # pragma: no cover
ops = type('MockOps', (object,), {'GraphKeys': type('GraphKeys', (object,), {'GLOBAL_VARIABLES': 'global_variables', 'MODEL_VARIABLES': 'model_variables'})})() # pragma: no cover
from_template = False # pragma: no cover
variable_scope = type('MockVariableScope', (object,), {'variable_scope': staticmethod(lambda name, default_name: None)})() # pragma: no cover
scope = 'input_layer_scope' # pragma: no cover
_LazyBuilder = type('MockLazyBuilder', (object,), {'__init__': lambda self, features: None}) # pragma: no cover
trainable = True # pragma: no cover
array_ops = type('MockArrayOps', (object,), {'shape': staticmethod(lambda x: tf.shape(x)), 'reshape': staticmethod(lambda x, shape: tf.reshape(x, shape)), 'concat': staticmethod(lambda tensors, axis: tf.concat(tensors, axis))})() # pragma: no cover
cols_to_vars = {} # pragma: no cover
cols_to_output_tensors = {} # pragma: no cover
_verify_static_batch_size_equality = lambda output_tensors, ordered_columns: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
from l3.Runtime import _l_
"""See input_layer. `scope` is a name or variable scope to use."""

feature_columns = _normalize_feature_columns(feature_columns)
_l_(8562)
for column in feature_columns:
    _l_(8565)

    if not isinstance(column, _DenseColumn):
        _l_(8564)

        raise ValueError(
            'Items of feature_columns must be a _DenseColumn. '
            'You can wrap a categorical column with an '
            'embedding_column or indicator_column. Given: {}'.format(column))
        _l_(8563)
weight_collections = list(weight_collections or [])
_l_(8566)
if ops.GraphKeys.GLOBAL_VARIABLES not in weight_collections:
    _l_(8568)

    weight_collections.append(ops.GraphKeys.GLOBAL_VARIABLES)
    _l_(8567)
if ops.GraphKeys.MODEL_VARIABLES not in weight_collections:
    _l_(8570)

    weight_collections.append(ops.GraphKeys.MODEL_VARIABLES)
    _l_(8569)

def _get_logits():
    _l_(8588)

    builder = _LazyBuilder(features)
    _l_(8571)
    output_tensors = []
    _l_(8572)
    ordered_columns = []
    _l_(8573)
    for column in sorted(feature_columns, key=lambda x: x.name):
        _l_(8585)

        ordered_columns.append(column)
        _l_(8574)
        with variable_scope.variable_scope(
            None, default_name=column._var_scope_name):
            _l_(8584)

            tensor = column._get_dense_tensor(  # pylint: disable=protected-access
                builder,
                weight_collections=weight_collections,
                trainable=trainable)
            _l_(8575)
            num_elements = column._variable_shape.num_elements()  # pylint: disable=protected-access
            _l_(8576)  # pylint: disable=protected-access
            batch_size = array_ops.shape(tensor)[0]
            _l_(8577)
            output_tensor = array_ops.reshape(
                tensor, shape=(batch_size, num_elements))
            _l_(8578)
            output_tensors.append(output_tensor)
            _l_(8579)
            if cols_to_vars is not None:
                _l_(8581)

                # Retrieve any variables created (some _DenseColumn's don't create
                # variables, in which case an empty list is returned).
                cols_to_vars[column] = ops.get_collection(
                    ops.GraphKeys.GLOBAL_VARIABLES,
                    scope=variable_scope.get_variable_scope().name)
                _l_(8580)
            if cols_to_output_tensors is not None:
                _l_(8583)

                cols_to_output_tensors[column] = output_tensor
                _l_(8582)
    _verify_static_batch_size_equality(output_tensors, ordered_columns)
    _l_(8586)
    aux = array_ops.concat(output_tensors, 1)
    _l_(8587)
    exit(aux)

# If we're constructing from the `make_template`, that by default adds a
# variable scope with the name of the layer. In that case, we dont want to
# add another `variable_scope` as that would break checkpoints.
if from_template:
    _l_(8592)

    aux = _get_logits()
    _l_(8589)
    exit(aux)
else:
    with variable_scope.variable_scope(
        scope, default_name='input_layer', values=features.values()):
        _l_(8591)

        aux = _get_logits()
        _l_(8590)
        exit(aux)
