# Extracted from ./data/repos/tensorflow/tensorflow/examples/label_image/label_image.py
input_name = "file_reader"
output_name = "normalized"
file_reader = tf.read_file(file_name, input_name)
if file_name.endswith(".png"):
    image_reader = tf.io.decode_png(file_reader, channels=3, name="png_reader")
elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(tf.io.decode_gif(file_reader, name="gif_reader"))
elif file_name.endswith(".bmp"):
    image_reader = tf.io.decode_bmp(file_reader, name="bmp_reader")
else:
    image_reader = tf.io.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
float_caster = tf.cast(image_reader, tf.float32)
dims_expander = tf.expand_dims(float_caster, 0)
resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
sess = tf.compat.v1.Session()
exit(sess.run(normalized))
