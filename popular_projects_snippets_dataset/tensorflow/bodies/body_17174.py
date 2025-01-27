# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
target_height = 8
target_width = 12
img = np.random.uniform(0, 100, size=(30, 10, 2)).astype(np.float32)
img_bf16 = ops.convert_to_tensor(img, dtype="bfloat16")
new_size = constant_op.constant([target_height, target_width])
img_methods = [
    image_ops.ResizeMethod.BILINEAR,
    image_ops.ResizeMethod.NEAREST_NEIGHBOR, image_ops.ResizeMethod.BICUBIC,
    image_ops.ResizeMethod.AREA
]
for method in img_methods:
    out_op_bf16 = image_ops.resize_images_v2(img_bf16, new_size, method)
    out_op_f32 = image_ops.resize_images_v2(img, new_size, method)
    bf16_val = self.evaluate(out_op_bf16)
    f32_val = self.evaluate(out_op_f32)
    self.assertAllClose(bf16_val, f32_val, rtol=1e-2, atol=1e-2)
