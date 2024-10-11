# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with self.assertRaisesRegex(ValueError,
                            'Prediction output key must be a string'):
    export_output_lib.PredictOutput({1: constant_op.constant([0])})

with self.assertRaisesRegex(ValueError,
                            'Prediction output value must be a Tensor'):
    export_output_lib.PredictOutput({
        'prediction1': sparse_tensor.SparseTensor(
            indices=[[0, 0]], values=[1], dense_shape=[1, 1]),
    })
