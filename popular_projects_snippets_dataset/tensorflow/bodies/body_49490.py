# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/vis_utils.py
"""Converts a Keras model to dot format and save to a file.

  Example:

  ```python
  input = tf.keras.Input(shape=(100,), dtype='int32', name='input')
  x = tf.keras.layers.Embedding(
      output_dim=512, input_dim=10000, input_length=100)(input)
  x = tf.keras.layers.LSTM(32)(x)
  x = tf.keras.layers.Dense(64, activation='relu')(x)
  x = tf.keras.layers.Dense(64, activation='relu')(x)
  x = tf.keras.layers.Dense(64, activation='relu')(x)
  output = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x)
  model = tf.keras.Model(inputs=[input], outputs=[output])
  dot_img_file = '/tmp/model_1.png'
  tf.keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)
  ```

  Args:
    model: A Keras model instance
    to_file: File name of the plot image.
    show_shapes: whether to display shape information.
    show_dtype: whether to display layer dtypes.
    show_layer_names: whether to display layer names.
    rankdir: `rankdir` argument passed to PyDot,
        a string specifying the format of the plot:
        'TB' creates a vertical plot;
        'LR' creates a horizontal plot.
    expand_nested: Whether to expand nested models into clusters.
    dpi: Dots per inch.

  Returns:
    A Jupyter notebook Image object if Jupyter is installed.
    This enables in-line display of the model plots in notebooks.
  """
dot = model_to_dot(
    model,
    show_shapes=show_shapes,
    show_dtype=show_dtype,
    show_layer_names=show_layer_names,
    rankdir=rankdir,
    expand_nested=expand_nested,
    dpi=dpi)
to_file = path_to_string(to_file)
if dot is None:
    exit()
_, extension = os.path.splitext(to_file)
if not extension:
    extension = 'png'
else:
    extension = extension[1:]
# Save image to disk.
dot.write(to_file, format=extension)
# Return the image as a Jupyter Image object, to be displayed in-line.
# Note that we cannot easily detect whether the code is running in a
# notebook, and thus we always return the Image if Jupyter is available.
if extension != 'pdf':
    try:
        from IPython import display
        exit(display.Image(filename=to_file))
    except ImportError:
        pass
