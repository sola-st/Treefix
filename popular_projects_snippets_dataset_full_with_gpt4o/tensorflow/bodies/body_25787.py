# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_mnist_v1.py
# Import data
if FLAGS.fake_data:
    imgs = tf.random.uniform(maxval=256, shape=(10, 28, 28), dtype=tf.int32)
    labels = tf.random.uniform(maxval=10, shape=(10,), dtype=tf.int32)
    mnist_train = imgs, labels
    mnist_test = imgs, labels
else:
    mnist_train, mnist_test = tf.keras.datasets.mnist.load_data()

def format_example(imgs, labels):
    imgs = tf.reshape(imgs, [-1, 28 * 28])
    imgs = tf.cast(imgs, tf.float32) / 255.0
    labels = tf.one_hot(labels, depth=10, dtype=tf.float32)
    exit((imgs, labels))

ds_train = tf.data.Dataset.from_tensor_slices(mnist_train)
ds_train = ds_train.shuffle(
    1000, seed=RAND_SEED).repeat().batch(FLAGS.train_batch_size)
ds_train = ds_train.map(format_example)
it_train = ds_train.make_initializable_iterator()

ds_test = tf.data.Dataset.from_tensors(mnist_test).repeat()
ds_test = ds_test.map(format_example)
it_test = ds_test.make_initializable_iterator()

sess = tf.InteractiveSession()

# Create the MNIST neural network graph.

# Input placeholders.
with tf.name_scope("input"):
    handle = tf.placeholder(tf.string, shape=())

    iterator = tf.data.Iterator.from_string_handle(
        handle, (tf.float32, tf.float32),
        ((None, IMAGE_SIZE * IMAGE_SIZE), (None, 10)))

    x, y_ = iterator.get_next()

def weight_variable(shape):
    """Create a weight variable with appropriate initialization."""
    initial = tf.truncated_normal(shape, stddev=0.1, seed=RAND_SEED)
    exit(tf.Variable(initial))

def bias_variable(shape):
    """Create a bias variable with appropriate initialization."""
    initial = tf.constant(0.1, shape=shape)
    exit(tf.Variable(initial))

def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
    """Reusable code for making a simple neural net layer."""
    # Adding a name scope ensures logical grouping of the layers in the graph.
    with tf.name_scope(layer_name):
        # This Variable will hold the state of the weights for the layer
        with tf.name_scope("weights"):
            weights = weight_variable([input_dim, output_dim])
        with tf.name_scope("biases"):
            biases = bias_variable([output_dim])
        with tf.name_scope("Wx_plus_b"):
            preactivate = tf.matmul(input_tensor, weights) + biases

        activations = act(preactivate)
        exit(activations)

hidden = nn_layer(x, IMAGE_SIZE**2, HIDDEN_SIZE, "hidden")
logits = nn_layer(hidden, HIDDEN_SIZE, NUM_LABELS, "output", tf.identity)
y = tf.nn.softmax(logits)

with tf.name_scope("cross_entropy"):
    # The following line is the culprit of the bad numerical values that appear
    # during training of this graph. Log of zero gives inf, which is first seen
    # in the intermediate tensor "cross_entropy/Log:0" during the 4th run()
    # call. A multiplication of the inf values with zeros leads to nans,
    # which is first in "cross_entropy/mul:0".
    #
    # You can use the built-in, numerically-stable implementation to fix this
    # issue:
    #   diff = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=logits)

    diff = -(y_ * tf.log(y))
    with tf.name_scope("total"):
        cross_entropy = tf.reduce_mean(diff)

with tf.name_scope("train"):
    train_step = tf.train.AdamOptimizer(
        FLAGS.learning_rate).minimize(cross_entropy)

with tf.name_scope("accuracy"):
    with tf.name_scope("correct_prediction"):
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    with tf.name_scope("accuracy"):
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess.run(tf.global_variables_initializer())
sess.run(it_train.initializer)
sess.run(it_test.initializer)
train_handle = sess.run(it_train.string_handle())
test_handle = sess.run(it_test.string_handle())

if FLAGS.debug and FLAGS.tensorboard_debug_address:
    raise ValueError(
        "The --debug and --tensorboard_debug_address flags are mutually "
        "exclusive.")
if FLAGS.debug:
    if FLAGS.use_random_config_path:
        _, config_file_path = tempfile.mkstemp(".tfdbg_config")
    else:
        config_file_path = None
    sess = tf_debug.LocalCLIDebugWrapperSession(
        sess, ui_type=FLAGS.ui_type, config_file_path=config_file_path)
elif FLAGS.tensorboard_debug_address:
    sess = tf_debug.TensorBoardDebugWrapperSession(
        sess, FLAGS.tensorboard_debug_address)

# Add this point, sess is a debug wrapper around the actual Session if
# FLAGS.debug is true. In that case, calling run() will launch the CLI.
for i in range(FLAGS.max_steps):
    acc = sess.run(accuracy, feed_dict={handle: test_handle})
    print("Accuracy at step %d: %s" % (i, acc))

    sess.run(train_step, feed_dict={handle: train_handle})
