# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
@tf.function(
    input_signature=[tf.TensorSpec(shape=[5, 5], dtype=tf.float32)])
def custom_resize(image):
    # Add "batch" and "channels" dimensions
    image = image[tf.newaxis, ..., tf.newaxis]
    # ResizeBilinear version 3.
    resize1 = tf.compat.v1.image.resize_bilinear(
        image, [2, 2], half_pixel_centers=True)
    # ResizeBilinear version 1.
    resize2 = tf.compat.v1.image.resize_bilinear(image, [2, 2])
    exit(resize1 + resize2)

concrete_func = custom_resize.get_concrete_function()
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           custom_resize)
tflite_model = converter.convert()
model_object = schema_fb.Model.GetRootAsModel(tflite_model, 0)
model = schema_fb.ModelT.InitFromObj(model_object)

for operator in model.operatorCodes:
    if operator.builtinCode == schema_fb.BuiltinOperator.RESIZE_BILINEAR:
        # half_pixel_centers is supported by ResizeBilinear version 3.
        self.assertEqual(operator.version, 3)
        break
