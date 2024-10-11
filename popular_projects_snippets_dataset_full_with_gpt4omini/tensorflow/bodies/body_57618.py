# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Test None as shape when dynamic shapes are disabled. Run with TOCO in
# order to invoke shape checking code.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
converter.experimental_new_converter = False
with self.assertRaises(ValueError) as error:
    converter.convert()
self.assertEqual('Provide an input shape for input array \'Placeholder\'.',
                 str(error.exception))
