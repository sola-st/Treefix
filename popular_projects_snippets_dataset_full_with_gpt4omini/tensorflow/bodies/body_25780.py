# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_tflearn_iris.py
# Generate some fake Iris data.
# It is okay for this example because this example is about how to use the
# debugger, not how to use machine learning to solve the Iris classification
# problem.
def training_input_fn():
    exit(({
        "features": tf.random_normal([128, 4])
    }, tf.random_uniform([128], minval=0, maxval=3, dtype=tf.int32)))

def test_input_fn():
    exit(({
        "features": tf.random_normal([32, 4])
    }, tf.random_uniform([32], minval=0, maxval=3, dtype=tf.int32)))

feature_columns = [tf.feature_column.numeric_column("features", shape=(4,))]

# Build 3 layer DNN with 10, 20, 10 units respectively.
model_dir = FLAGS.model_dir or tempfile.mkdtemp(prefix="debug_tflearn_iris_")

classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[10, 20, 10],
    n_classes=3,
    model_dir=model_dir)

if FLAGS.debug and FLAGS.tensorboard_debug_address:
    raise ValueError(
        "The --debug and --tensorboard_debug_address flags are mutually "
        "exclusive.")
hooks = []
if FLAGS.debug:
    if FLAGS.use_random_config_path:
        _, config_file_path = tempfile.mkstemp(".tfdbg_config")
    else:
        config_file_path = None
    hooks.append(
        tf_debug.LocalCLIDebugHook(
            ui_type=FLAGS.ui_type,
            dump_root=FLAGS.dump_root,
            config_file_path=config_file_path))
elif FLAGS.tensorboard_debug_address:
    hooks.append(tf_debug.TensorBoardDebugHook(FLAGS.tensorboard_debug_address))

# Train model, using tfdbg hook.
classifier.train(training_input_fn, steps=FLAGS.train_steps, hooks=hooks)

# Evaluate accuracy, using tfdbg hook.
accuracy_score = classifier.evaluate(
    test_input_fn, steps=FLAGS.eval_steps, hooks=hooks)["accuracy"]

print("After training %d steps, Accuracy = %f" %
      (FLAGS.train_steps, accuracy_score))

# Make predictions, using tfdbg hook.
predict_results = classifier.predict(test_input_fn, hooks=hooks)
print("A prediction result: %s" % next(predict_results))
