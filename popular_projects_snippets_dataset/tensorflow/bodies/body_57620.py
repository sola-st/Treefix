# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, None, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Test invalid shape. None after 1st dimension. Run with TOCO in order to
# invoke shape checking code.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
converter.experimental_new_converter = False
with self.assertRaises(ValueError) as error:
    converter.convert()
self.assertEqual(
    'None is only supported in the 1st dimension. Tensor '
    '\'Placeholder\' has invalid shape \'[1, None, 16, 3]\'.',
    str(error.exception))
