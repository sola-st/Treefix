# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(0), dtypes.float32)
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(1), dtypes.float16)
self.assertEqual(util._convert_tflite_enum_type_to_tf_type(2), dtypes.int32)
self.assertEqual(util._convert_tflite_enum_type_to_tf_type(3), dtypes.uint8)
self.assertEqual(util._convert_tflite_enum_type_to_tf_type(4), dtypes.int64)
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(5), dtypes.string)
self.assertEqual(util._convert_tflite_enum_type_to_tf_type(6), dtypes.bool)
self.assertEqual(util._convert_tflite_enum_type_to_tf_type(7), dtypes.int16)
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(8), dtypes.complex64)
self.assertEqual(util._convert_tflite_enum_type_to_tf_type(9), dtypes.int8)
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(10), dtypes.float64)
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(11), dtypes.complex128)
self.assertEqual(
    util._convert_tflite_enum_type_to_tf_type(16), dtypes.uint32)
with self.assertRaises(ValueError) as error:
    util._convert_tflite_enum_type_to_tf_type(20)
self.assertEqual(
    "Unsupported enum 20. The valid map of enum to tf types is : "
    "{0: tf.float32, 1: tf.float16, 2: tf.int32, 3: tf.uint8, 4: tf.int64, "
    "5: tf.string, 6: tf.bool, 7: tf.int16, 8: tf.complex64, 9: tf.int8, "
    "10: tf.float64, 11: tf.complex128, 16: tf.uint32}",
    str(error.exception))
