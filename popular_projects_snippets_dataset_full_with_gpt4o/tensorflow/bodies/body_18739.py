# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad.py
"""The gradients for `rgb_to_hsv` operation.

  This function is a piecewise continuous function as defined here:
  https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB
  We perform the multivariate derivative and compute all partial derivatives
  separately before adding them in the end. Formulas are given before each
  partial derivative calculation.

  Args:
    op: The `rgb_to_hsv` `Operation` that we are differentiating.
    grad: Gradient with respect to the output of the `rgb_to_hsv` op.

  Returns:
    Gradients with respect to the input of `rgb_to_hsv`.
  """
# Input Channels
reds = op.inputs[0][..., 0]
greens = op.inputs[0][..., 1]
blues = op.inputs[0][..., 2]
# Output Channels
saturation = op.outputs[0][..., 1]
value = op.outputs[0][..., 2]

dtype = op.inputs[0].dtype

# Mask/Indicator for max and min values of each pixel.
# Arbitrary assignment in case of tie breakers with R>G>B.
# Max values
red_biggest = math_ops.cast((reds >= blues) & \
                 (reds >= greens), dtype)
green_biggest = math_ops.cast((greens > reds) & \
                   (greens >= blues), dtype)
blue_biggest = math_ops.cast((blues > reds) & \
                  (blues > greens), dtype)
# Min values
red_smallest = math_ops.cast((reds < blues) & \
                  (reds < greens), dtype)
green_smallest = math_ops.cast((greens <= reds) & \
                    (greens < blues), dtype)
blue_smallest = math_ops.cast((blues <= reds) & \
                   (blues <= greens), dtype)

# Derivatives of R, G, B wrt Value slice
dv_dr = red_biggest
dv_dg = green_biggest
dv_db = blue_biggest

# Derivatives of R, G, B wrt Saturation slice

# The first term in the addition is the case when the corresponding color
# from (r,g,b) was "MAX"
# -> derivative = MIN/square(MAX), MIN could be one of the other two colors
# The second term is the case when the corresponding color from
# (r,g,b) was "MIN"
# -> derivative = -1/MAX, MAX could be one of the other two colours.
ds_dr = math_ops.cast(reds > 0, dtype) * math_ops.add(
    red_biggest * math_ops.add(green_smallest * greens, blue_smallest * blues)
    * _CustomReciprocal(math_ops.square(reds)), red_smallest * -1 *
    _CustomReciprocal((green_biggest * greens) + (blue_biggest * blues)))
ds_dg = math_ops.cast(greens > 0, dtype) * math_ops.add(
    green_biggest * math_ops.add(red_smallest * reds, blue_smallest * blues) *
    _CustomReciprocal(math_ops.square(greens)), green_smallest * -1 *
    _CustomReciprocal((red_biggest * reds) + (blue_biggest * blues)))
ds_db = math_ops.cast(blues > 0, dtype) * math_ops.add(
    blue_biggest * math_ops.add(green_smallest * greens, red_smallest * reds)
    * _CustomReciprocal(math_ops.square(blues)), blue_smallest * -1 *
    _CustomReciprocal((green_biggest * greens) + (red_biggest * reds)))

# Derivatives of R, G, B wrt Hue slice

# Need to go case by case for each color.
# for red, dh_dr -> dh_dr_1 + dh_dr_2 + dh_dr_3 + dh_dr_4 + dh_dr_5
# dh_dr_1 ->
# if red was MAX, then derivative = 60 * -1 * (G-B)/square(MAX-MIN) == 60 *\
#  -1 * (greens-blues) * reciprocal(square(saturation)) * \
#  reciprocal(square(value))
# elif green was MAX, there are two subcases
# ie when red was MIN and when red was NOT MIN
#   dh_dr_2 ->
#   if red was MIN (use UV rule) ->  60 * ((1 * -1/(MAX-MIN)) +\
#     (B-R)*(-1/square(MAX-MIN) * -1)) == 60 * (blues - greens) *\
#     reciprocal(square(reds - greens))
#   dh_dr_3 ->
#   if red was NOT MIN -> 60 * -1/MAX-MIN == -60 * reciprocal(greens-blues)
# elif blue was MAX, there are two subcases
#   dh_dr_4 ->
#   if red was MIN (similarly use the UV rule) -> 60 * (blues - greens) *\
#     reciprocal(square(blues - reds))
#   dh_dr_5 ->
#   if red was NOT MIN -> 60 * 1/MAX-MIN == 60 * reciprocal(blues-greens)
dh_dr_1 = 60 * (
    math_ops.cast(reds > 0, dtype) * red_biggest * -1 *
    (greens - blues) * _CustomReciprocal(math_ops.square(saturation)) *
    _CustomReciprocal(math_ops.square(value)))
dh_dr_2 = 60 * (
    math_ops.cast(greens > 0, dtype) * green_biggest * red_smallest *
    (blues - greens) * _CustomReciprocal(math_ops.square(reds - greens)))
dh_dr_3 = 60 * (
    math_ops.cast(greens > 0, dtype) * green_biggest * blue_smallest * -1 *
    _CustomReciprocal(greens - blues))
dh_dr_4 = 60 * (
    math_ops.cast(blues > 0, dtype) * blue_biggest * red_smallest *
    (blues - greens) * _CustomReciprocal(math_ops.square(blues - reds)))
dh_dr_5 = 60 * (
    math_ops.cast(blues > 0, dtype) * blue_biggest * green_smallest *
    _CustomReciprocal(blues - greens))

dh_dr = dh_dr_1 + dh_dr_2 + dh_dr_3 + dh_dr_4 + dh_dr_5
# Converting from degrees to [0,1] scale as specified in
# https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_hsv
dh_dr = dh_dr / 360

# for green, dh_dg -> dh_dg_1 + dh_dg_2 + dh_dg_3 + dh_dg_4 + dh_dg_5
# dh_dg_1 ->
# if green was MAX, then derivative = 60 * -1 * (B-R)/square(MAX-MIN) == 60 *\
#   -1 * (blues - reds) * reciprocal(square(saturation)) * \
#   reciprocal(square(value))
# elif red was MAX, there are two subcases ie
# when green was MIN and when green was NOT MIN
#   dh_dg_2 ->
#   if green was MIN (use UV rule) ->  60 * ((1 * 1/(MAX-MIN)) + \
#     (greens-blues) * (-1/square(MAX-MIN) * -1)) == 60 * \
#     ((reciprocal(reds-greens) + (greens-blues) * \
#     reciprocal(square(reds-greens))))
#   dh_dg_3 ->
#   if green was NOT MIN -> 60 * 1/MAX-MIN == 60 * reciprocal(reds - blues)
# elif blue was MAX, there are two subcases
#   dh_dg_4 ->
#   if green was MIN (similarly use the UV rule) -> 60 * -1 * \
#     (reciprocal(blues - greens) + (reds-greens)* -1 * \
#     reciprocal(square(blues-greens)))
#   dh_dr_5 ->
#   if green was NOT MIN -> 60 * -1/MAX-MIN == -60 * reciprocal(blues - reds)
dh_dg_1 = 60 * (
    math_ops.cast(greens > 0, dtype) * green_biggest * -1 *
    (blues - reds) * _CustomReciprocal(math_ops.square(saturation)) *
    _CustomReciprocal(math_ops.square(value)))
dh_dg_2 = 60 * (
    math_ops.cast(reds > 0, dtype) * red_biggest * green_smallest *
    (reds - blues) * _CustomReciprocal(math_ops.square(reds - greens)))
dh_dg_3 = 60 * (
    math_ops.cast(reds > 0, dtype) * red_biggest * blue_smallest *
    _CustomReciprocal(reds - blues))
dh_dg_4 = 60 * (
    math_ops.cast(blues > 0, dtype) * blue_biggest * green_smallest *
    (reds - blues) * _CustomReciprocal(math_ops.square(blues - greens)))
dh_dg_5 = 60 * (
    math_ops.cast(blues > 0, dtype) * blue_biggest * red_smallest * -1 *
    _CustomReciprocal(blues - reds))

dh_dg = dh_dg_1 + dh_dg_2 + dh_dg_3 + dh_dg_4 + dh_dg_5
# Converting from degrees to [0,1] scale as specified in
# https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_hsv
dh_dg = dh_dg / 360

# for blue, dh_db -> dh_db_1 + dh_db_2 + dh_db_3 + dh_db_4 + dh_db_5
# dh_db_1 ->
# if blue was MAX, then derivative = 60 * -1 * (R-G)/square(MAX-MIN) == 60 *\
#   -1 * reciprocal(square(saturation)) * reciprocal(square(value))
# elif red was MAX, there are two subcases
# ie when blue was MIN and when blue was NOT MIN
#   dh_dg_2 ->
#   if blue was MIN (use UV rule) ->  60 * ((1 * -1/(MAX-MIN)) + \
#     (greens-blues) * (-1/square(MAX-MIN) * -1)) == 60 * (greens - reds) *\
#     reciprocal(square(reds - blues))
#   dh_dg_3 ->
#   if blue was NOT MIN -> 60 * -1/MAX-MIN == 60 * -1 * \
#     reciprocal(reds - greens)
# elif green was MAX, there are two subcases
#   dh_dg_4 ->
#   if blue was MIN (similarly use the UV rule) -> 60 * -1 * \
#     (reciprocal(greens - blues) + (blues - reds) * -1 * \
#     reciprocal(square(greens - blues)))
#   dh_dr_5 ->
#   if blue was NOT MIN -> 60 * 1/MAX-MIN == 60 * reciprocal(greens - reds)
dh_db_1 = 60 * (
    math_ops.cast(blues > 0, dtype) * blue_biggest * -1 *
    (reds - greens) * _CustomReciprocal(math_ops.square(saturation)) *
    _CustomReciprocal(math_ops.square(value)))
dh_db_2 = 60 * (
    math_ops.cast(reds > 0, dtype) * red_biggest * blue_smallest *
    (greens - reds) * _CustomReciprocal(math_ops.square(reds - blues)))
dh_db_3 = 60 * (
    math_ops.cast(reds > 0, dtype) * red_biggest * green_smallest * -1 *
    _CustomReciprocal(reds - greens))
dh_db_4 = 60 * (
    math_ops.cast(greens > 0, dtype) * green_biggest * blue_smallest *
    (greens - reds) * _CustomReciprocal(math_ops.square(greens - blues)))
dh_db_5 = 60 * (
    math_ops.cast(greens > 0, dtype) * green_biggest * red_smallest *
    _CustomReciprocal(greens - reds))

dh_db = dh_db_1 + dh_db_2 + dh_db_3 + dh_db_4 + dh_db_5
# Converting from degrees to [0,1] scale as specified in
# https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_hsv
dh_db = dh_db / 360

# Gradients wrt to inputs
dv_drgb = array_ops.stack(
    [grad[..., 2] * dv_dr, grad[..., 2] * dv_dg, grad[..., 2] * dv_db],
    axis=-1)
ds_drgb = array_ops.stack(
    [grad[..., 1] * ds_dr, grad[..., 1] * ds_dg, grad[..., 1] * ds_db],
    axis=-1)
dh_drgb = array_ops.stack(
    [grad[..., 0] * dh_dr, grad[..., 0] * dh_dg, grad[..., 0] * dh_db],
    axis=-1)

gradient_input = math_ops.add(math_ops.add(dv_drgb, ds_drgb), dh_drgb)
exit(gradient_input)
