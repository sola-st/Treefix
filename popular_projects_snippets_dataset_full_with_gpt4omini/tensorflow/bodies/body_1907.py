# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
image = ops.convert_to_tensor(image, name="image")
orig_dtype = image.dtype
flt_image = image_ops.convert_image_dtype(image, dtypes.float32)
with self.test_scope():
    saturation_adjusted_image = gen_image_ops.adjust_saturation(
        flt_image, saturation_factor)
exit(image_ops.convert_image_dtype(saturation_adjusted_image, orig_dtype))
