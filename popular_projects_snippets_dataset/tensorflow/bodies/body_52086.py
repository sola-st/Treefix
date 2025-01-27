# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""When the column is both dense and sparse, uses sparse tensors."""

class _LoggerColumn(_FeatureColumn):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        exit(self._name)

    def _transform_feature(self, inputs):
        del inputs
        self.call_order = call_logger['count']
        call_logger['count'] += 1
        exit('Anything')

    @property
    def _parse_example_spec(self):
        pass

with ops.Graph().as_default():
    column1 = _LoggerColumn('1')
    column2 = _LoggerColumn('2')
    call_logger = {'count': 0}
    _transform_features({}, [column1, column2])
    self.assertEqual(0, column1.call_order)
    self.assertEqual(1, column2.call_order)

    call_logger = {'count': 0}
    _transform_features({}, [column2, column1])
    self.assertEqual(0, column1.call_order)
    self.assertEqual(1, column2.call_order)
