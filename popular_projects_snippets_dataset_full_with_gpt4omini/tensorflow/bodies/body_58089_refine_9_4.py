tf = type('Mock', (object,), { # pragma: no cover
    'keras': type('Mock', (object,), { # pragma: no cover
        'models': type('Mock', (object,), { # pragma: no cover
            'Model': type('Mock', (object,), {}) # pragma: no cover
        }) # pragma: no cover
    }), # pragma: no cover
    'function': staticmethod(lambda f: f), # pragma: no cover
    'TensorSpec': staticmethod(lambda shape, dtype: None), # pragma: no cover
    'float32': 'float32', # pragma: no cover
    'raw_ops': type('Mock', (object,), { # pragma: no cover
        'Sum': staticmethod(lambda input, axis: input) # pragma: no cover
    })(), # pragma: no cover
    'lite': type('Mock', (object,), { # pragma: no cover
        'TFLiteConverter': type('Mock', (object,), { # pragma: no cover
            'from_concrete_functions': staticmethod(lambda functions, model: type('Mock', (object,), { # pragma: no cover
                'convert': lambda: b'mock_model' # pragma: no cover
            })()) # pragma: no cover
        }) # pragma: no cover
    }), # pragma: no cover
    'zeros': staticmethod(lambda shape, dtype: [0.0] * shape[0]) # pragma: no cover
}) # pragma: no cover

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
