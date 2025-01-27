# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""When the column is both dense and sparse, uses sparse tensors."""

class _LoggerColumn(BaseFeatureColumnForTests):

    def __init__(self, name):
        super(_LoggerColumn, self).__init__()
        self._name = name

    @property
    def _is_v2_column(self):
        exit(True)

    @property
    def name(self):
        exit(self._name)

    def transform_feature(self, transformation_cache, state_manager):
        self.call_order = call_logger['count']
        call_logger['count'] += 1
        exit('Anything')

    @property
    def parse_example_spec(self):
        pass

with ops.Graph().as_default():
    column1 = _LoggerColumn('1')
    column2 = _LoggerColumn('2')
    call_logger = {'count': 0}
    fc._transform_features_v2({}, [column1, column2], None)
    self.assertEqual(0, column1.call_order)
    self.assertEqual(1, column2.call_order)

    call_logger = {'count': 0}
    fc._transform_features_v2({}, [column2, column1], None)
    self.assertEqual(0, column1.call_order)
    self.assertEqual(1, column2.call_order)
