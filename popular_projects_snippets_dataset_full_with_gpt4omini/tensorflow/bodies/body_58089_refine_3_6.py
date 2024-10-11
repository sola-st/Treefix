tf = type('Mock', (object,), {'keras': type('Mock', (object,), {'models': type('Mock', (object,), {'Model': object})}), 'function': staticmethod(lambda *args, **kwargs: None), 'TensorSpec': staticmethod(lambda shape, dtype: None), 'lite': type('Mock', (object,), {'TFLiteConverter': type('Mock', (object,), {'from_concrete_functions': staticmethod(lambda functions, model: None)})}), 'raw_ops': type('Mock', (object,), {'Sum': staticmethod(lambda input, axis: None)}), 'float32': None, 'zeros': staticmethod(lambda shape, dtype: None)}) # pragma: no cover

class MockModel: pass # pragma: no cover
tf = type('Mock', (object,), {'keras': type('MockKeras', (object,), {'models': type('MockModels', (object,), {'Model': MockModel})}), 'function': staticmethod(lambda func: func), 'TensorSpec': staticmethod(lambda shape, dtype: None), 'lite': type('MockLite', (object,), {'TFLiteConverter': type('MockConverter', (object,), {'from_concrete_functions': staticmethod(lambda functions, model: type('Mock', (object,), {'convert': lambda self: None}))})}), 'raw_ops': type('MockRawOps', (object,), {'Sum': staticmethod(lambda input, axis: None)}), 'float32': None, 'zeros': staticmethod(lambda shape, dtype: [])}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py

from l3.Runtime import _l_
class TestModel(tf.keras.models.Model):
    _l_(4384)


    @tf.function(
        input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
    def TestSum(self, x):
        _l_(4383)

        aux = tf.raw_ops.Sum(input=x, axis=[0])
        _l_(4382)
        exit(aux)

test_model = TestModel()
_l_(4385)
converter = tf.lite.TFLiteConverter.from_concrete_functions([
    test_model.TestSum.get_concrete_function(
        tf.TensorSpec([None], tf.float32))
], test_model)
_l_(4386)
model = converter.convert()
_l_(4387)
interpreter = tf.lite.Interpreter(model_content=model)
_l_(4388)
# Make sure that passing empty tensor doesn't cause any errors.
interpreter.get_signature_runner()(x=tf.zeros([0], tf.float32))
_l_(4389)
