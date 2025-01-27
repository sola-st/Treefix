# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops.py
"""Computes the gradient for ImageProjectiveTransform."""
images = op.inputs[0]
transforms = op.inputs[1]
interpolation = op.get_attr("interpolation")
fill_mode = op.get_attr("fill_mode")

image_or_images = ops.convert_to_tensor(images, name="images")
transform_or_transforms = ops.convert_to_tensor(
    transforms, name="transforms", dtype=dtypes.float32)

if image_or_images.dtype.base_dtype not in _IMAGE_DTYPES:
    raise TypeError("Invalid dtype %s." % image_or_images.dtype)
if len(transform_or_transforms.get_shape()) == 1:
    transforms = transform_or_transforms[None]
elif len(transform_or_transforms.get_shape()) == 2:
    transforms = transform_or_transforms
else:
    raise TypeError("Transforms should have rank 1 or 2.")

# Invert transformations
transforms = flat_transforms_to_matrices(transforms=transforms)
inverse = linalg_ops.matrix_inverse(transforms)
transforms = matrices_to_flat_transforms(inverse)
output = gen_image_ops.image_projective_transform_v3(
    images=grad,
    transforms=transforms,
    output_shape=array_ops.shape(image_or_images)[1:3],
    interpolation=interpolation,
    fill_mode=fill_mode,
    fill_value=0.0)
exit([output, None, None, None])
