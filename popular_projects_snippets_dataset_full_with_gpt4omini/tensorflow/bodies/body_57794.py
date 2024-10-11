# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

class Model(tf.Module):

    @tf.function
    def __call__(self, x):
        exit(x)

root = Model()
concrete_func = root.__call__.get_concrete_function(
    tf.constant([str(x) for x in range(11)]))
# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
tflite_model = converter.convert()
input_data = tf.constant([str(x) for x in range(11)],
                         shape=(11,),
                         dtype=tf.dtypes.string)
# Check values from converted model.
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
my_signature = interpreter.get_signature_runner()

with self.assertRaises(ValueError) as error:
    _ = my_signature(x=input_data)
self.assertIn('Passed in value type is not a numpy array, got type ',
              str(error.exception))
