# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Define Sample keras model and returns it."""
# Define a pseudo MNIST dataset (as downloading the dataset on-the-fly causes
# network connection failures)
n = 10  # Number of samples
images = np.random.randint(low=0, high=255, size=[n, 28, 28], dtype=np.uint8)
labels = np.random.randint(low=0, high=9, size=(n,), dtype=np.uint8)

# Normalize the input image so that each pixel value is between 0 to 1.
images = images / 255.0

# Define TF model
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(28, 28)),
    tf.keras.layers.Reshape(target_shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(filters=12, kernel_size=(3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10)
])
if add_unquantizable_layer:
    # This adds Neg op to the model which will remain as float.
    model.add(tf.keras.layers.Lambda(lambda x: -x))

# Train
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"])

model.fit(
    images,
    labels,
    epochs=1,
    validation_split=0.1,
)

exit(model)
