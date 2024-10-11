class _DenseColumn: # pragma: no cover
    def __init__(self, name): # pragma: no cover
        self.name = name # pragma: no cover
        self._var_scope_name = name # pragma: no cover
        self._variable_shape = type('Shape', (object,), {'num_elements': lambda: 1})() # pragma: no cover
 # pragma: no cover
    def _get_dense_tensor(self, builder, weight_collections, trainable): # pragma: no cover
        return array_ops.ones([2, 1], dtype=tf.float32) # pragma: no cover
 # pragma: no cover
def _normalize_feature_columns(feature_columns): # pragma: no cover
    return feature_columns # pragma: no cover
 # pragma: no cover
class _LazyBuilder: # pragma: no cover
    def __init__(self, features): # pragma: no cover
        self.features = features # pragma: no cover
 # pragma: no cover
def _verify_static_batch_size_equality(output_tensors, ordered_columns): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
feature_columns = [_DenseColumn('column1')] # pragma: no cover
cols_to_vars = {} # pragma: no cover
cols_to_output_tensors = {} # pragma: no cover
weight_collections = [] # pragma: no cover
trainable = True # pragma: no cover
from_template = False # pragma: no cover
scope = 'test_scope' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
from l3.Runtime import _l_
"""See input_layer. `scope` is a name or variable scope to use."""

feature_columns = _normalize_feature_columns(feature_columns)
_l_(20829)
for column in feature_columns:
    _l_(20832)

    if not isinstance(column, _DenseColumn):
        _l_(20831)

        raise ValueError(
            'Items of feature_columns must be a _DenseColumn. '
            'You can wrap a categorical column with an '
            'embedding_column or indicator_column. Given: {}'.format(column))
        _l_(20830)
weight_collections = list(weight_collections or [])
_l_(20833)
if ops.GraphKeys.GLOBAL_VARIABLES not in weight_collections:
    _l_(20835)

    weight_collections.append(ops.GraphKeys.GLOBAL_VARIABLES)
    _l_(20834)
if ops.GraphKeys.MODEL_VARIABLES not in weight_collections:
    _l_(20837)

    weight_collections.append(ops.GraphKeys.MODEL_VARIABLES)
    _l_(20836)

def _get_logits():
    _l_(20855)

    builder = _LazyBuilder(features)
    _l_(20838)
    output_tensors = []
    _l_(20839)
    ordered_columns = []
    _l_(20840)
    for column in sorted(feature_columns, key=lambda x: x.name):
        _l_(20852)

        ordered_columns.append(column)
        _l_(20841)
        with variable_scope.variable_scope(
            None, default_name=column._var_scope_name):
            _l_(20851)

            tensor = column._get_dense_tensor(  # pylint: disable=protected-access
                builder,
                weight_collections=weight_collections,
                trainable=trainable)
            _l_(20842)
            num_elements = column._variable_shape.num_elements()  # pylint: disable=protected-access
            _l_(20843)  # pylint: disable=protected-access
            batch_size = array_ops.shape(tensor)[0]
            _l_(20844)
            output_tensor = array_ops.reshape(
                tensor, shape=(batch_size, num_elements))
            _l_(20845)
            output_tensors.append(output_tensor)
            _l_(20846)
            if cols_to_vars is not None:
                _l_(20848)

                # Retrieve any variables created (some _DenseColumn's don't create
                # variables, in which case an empty list is returned).
                cols_to_vars[column] = ops.get_collection(
                    ops.GraphKeys.GLOBAL_VARIABLES,
                    scope=variable_scope.get_variable_scope().name)
                _l_(20847)
            if cols_to_output_tensors is not None:
                _l_(20850)

                cols_to_output_tensors[column] = output_tensor
                _l_(20849)
    _verify_static_batch_size_equality(output_tensors, ordered_columns)
    _l_(20853)
    aux = array_ops.concat(output_tensors, 1)
    _l_(20854)
    exit(aux)

# If we're constructing from the `make_template`, that by default adds a
# variable scope with the name of the layer. In that case, we dont want to
# add another `variable_scope` as that would break checkpoints.
if from_template:
    _l_(20859)

    aux = _get_logits()
    _l_(20856)
    exit(aux)
else:
    with variable_scope.variable_scope(
        scope, default_name='input_layer', values=features.values()):
        _l_(20858)

        aux = _get_logits()
        _l_(20857)
        exit(aux)
