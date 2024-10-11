tf = type('Mock', (object,), { 'keras': type('Mock', (object,), { 'models': type('Mock', (object,), { 'Model': type('MockModel', (object,), {}) }) }), 'function': staticmethod(lambda func: func), 'TensorSpec': staticmethod(lambda shape, dtype: None), 'float32': 'float32', 'raw_ops': type('Mock', (object,), { 'Sum': staticmethod(lambda input, axis: sum(input)) }), 'lite': type('Mock', (object,), { 'TFLiteConverter': type('Mock', (object,), { 'from_concrete_functions': staticmethod(lambda functions, model: type('Mock', (object,), { 'convert': lambda self: b'model_content' })()) }) }), 'zeros': staticmethod(lambda shape, dtype: []) }) # pragma: no cover

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
