# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py

from l3.Runtime import _l_
class TestModel(tf.keras.models.Model):
    _l_(16083)


    @tf.function(
        input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
    def TestSum(self, x):
        _l_(16082)

        aux = tf.raw_ops.Sum(input=x, axis=[0])
        _l_(16081)
        exit(aux)

test_model = TestModel()
_l_(16084)
converter = tf.lite.TFLiteConverter.from_concrete_functions([
    test_model.TestSum.get_concrete_function(
        tf.TensorSpec([None], tf.float32))
], test_model)
_l_(16085)
model = converter.convert()
_l_(16086)
interpreter = tf.lite.Interpreter(model_content=model)
_l_(16087)
# Make sure that passing empty tensor doesn't cause any errors.
interpreter.get_signature_runner()(x=tf.zeros([0], tf.float32))
_l_(16088)
