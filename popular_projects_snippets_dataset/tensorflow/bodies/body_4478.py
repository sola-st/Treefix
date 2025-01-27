# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/train.py
# Set the verbosity based on flags (default is INFO, so we see all messages)
tf.compat.v1.logging.set_verbosity(FLAGS.verbosity)

# Start a new TensorFlow session.
sess = tf.compat.v1.InteractiveSession()

# Begin by making sure we have the training data we need. If you already have
# training data of your own, use `--data_url= ` on the command line to avoid
# downloading.
model_settings = models.prepare_model_settings(
    len(input_data.prepare_words_list(FLAGS.wanted_words.split(','))),
    FLAGS.sample_rate, FLAGS.clip_duration_ms, FLAGS.window_size_ms,
    FLAGS.window_stride_ms, FLAGS.feature_bin_count, FLAGS.preprocess)
audio_processor = input_data.AudioProcessor(
    FLAGS.data_url, FLAGS.data_dir,
    FLAGS.silence_percentage, FLAGS.unknown_percentage,
    FLAGS.wanted_words.split(','), FLAGS.validation_percentage,
    FLAGS.testing_percentage, model_settings, FLAGS.summaries_dir)
fingerprint_size = model_settings['fingerprint_size']
label_count = model_settings['label_count']
time_shift_samples = int((FLAGS.time_shift_ms * FLAGS.sample_rate) / 1000)
# Figure out the learning rates for each training phase. Since it's often
# effective to have high learning rates at the start of training, followed by
# lower levels towards the end, the number of steps and learning rates can be
# specified as comma-separated lists to define the rate at each stage. For
# example --how_many_training_steps=10000,3000 --learning_rate=0.001,0.0001
# will run 13,000 training loops in total, with a rate of 0.001 for the first
# 10,000, and 0.0001 for the final 3,000.
training_steps_list = list(map(int, FLAGS.how_many_training_steps.split(',')))
learning_rates_list = list(map(float, FLAGS.learning_rate.split(',')))
if len(training_steps_list) != len(learning_rates_list):
    raise Exception(
        '--how_many_training_steps and --learning_rate must be equal length '
        'lists, but are %d and %d long instead' % (len(training_steps_list),
                                                   len(learning_rates_list)))

input_placeholder = tf.compat.v1.placeholder(
    tf.float32, [None, fingerprint_size], name='fingerprint_input')
if FLAGS.quantize:
    fingerprint_min, fingerprint_max = input_data.get_features_range(
        model_settings)
    fingerprint_input = tf.quantization.fake_quant_with_min_max_args(
        input_placeholder, fingerprint_min, fingerprint_max)
else:
    fingerprint_input = input_placeholder

logits, dropout_rate = models.create_model(
    fingerprint_input,
    model_settings,
    FLAGS.model_architecture,
    is_training=True)

# Define loss and optimizer
ground_truth_input = tf.compat.v1.placeholder(
    tf.int64, [None], name='groundtruth_input')

# Optionally we can add runtime checks to spot when NaNs or other symptoms of
# numerical errors start occurring during training.
control_dependencies = []
if FLAGS.check_nans:
    checks = tf.compat.v1.add_check_numerics_ops()
    control_dependencies = [checks]

# Create the back propagation and training evaluation machinery in the graph.
with tf.compat.v1.name_scope('cross_entropy'):
    cross_entropy_mean = tf.compat.v1.losses.sparse_softmax_cross_entropy(
        labels=ground_truth_input, logits=logits)

if FLAGS.quantize:
    try:
        tf.contrib.quantize.create_training_graph(quant_delay=0)
    except AttributeError as e:
        msg = e.args[0]
        msg += ('\n\n The --quantize option still requires contrib, which is not '
                'part of TensorFlow 2.0. Please install a previous version:'
                '\n    `pip install tensorflow<=1.15`')
        e.args = (msg,)
        raise e

with tf.compat.v1.name_scope('train'), tf.control_dependencies(
    control_dependencies):
    learning_rate_input = tf.compat.v1.placeholder(
        tf.float32, [], name='learning_rate_input')
    if FLAGS.optimizer == 'gradient_descent':
        train_step = tf.compat.v1.train.GradientDescentOptimizer(
            learning_rate_input).minimize(cross_entropy_mean)
    elif FLAGS.optimizer == 'momentum':
        train_step = tf.compat.v1.train.MomentumOptimizer(
            learning_rate_input, .9,
            use_nesterov=True).minimize(cross_entropy_mean)
    else:
        raise Exception('Invalid Optimizer')
predicted_indices = tf.argmax(input=logits, axis=1)
correct_prediction = tf.equal(predicted_indices, ground_truth_input)
confusion_matrix = tf.math.confusion_matrix(labels=ground_truth_input,
                                            predictions=predicted_indices,
                                            num_classes=label_count)
evaluation_step = tf.reduce_mean(input_tensor=tf.cast(correct_prediction,
                                                      tf.float32))
with tf.compat.v1.get_default_graph().name_scope('eval'):
    tf.compat.v1.summary.scalar('cross_entropy', cross_entropy_mean)
    tf.compat.v1.summary.scalar('accuracy', evaluation_step)

global_step = tf.compat.v1.train.get_or_create_global_step()
increment_global_step = tf.compat.v1.assign(global_step, global_step + 1)

saver = tf.compat.v1.train.Saver(tf.compat.v1.global_variables())

# Merge all the summaries and write them out to /tmp/retrain_logs (by default)
merged_summaries = tf.compat.v1.summary.merge_all(scope='eval')
train_writer = tf.compat.v1.summary.FileWriter(FLAGS.summaries_dir + '/train',
                                               sess.graph)
validation_writer = tf.compat.v1.summary.FileWriter(
    FLAGS.summaries_dir + '/validation')

tf.compat.v1.global_variables_initializer().run()

start_step = 1

if FLAGS.start_checkpoint:
    models.load_variables_from_checkpoint(sess, FLAGS.start_checkpoint)
    start_step = global_step.eval(session=sess)

tf.compat.v1.logging.info('Training from step: %d ', start_step)

# Save graph.pbtxt.
tf.io.write_graph(sess.graph_def, FLAGS.train_dir,
                  FLAGS.model_architecture + '.pbtxt')

# Save list of words.
with gfile.GFile(
    os.path.join(FLAGS.train_dir, FLAGS.model_architecture + '_labels.txt'),
    'w') as f:
    f.write('\n'.join(audio_processor.words_list))

# Training loop.
training_steps_max = np.sum(training_steps_list)
for training_step in range(start_step, training_steps_max + 1):
    # Figure out what the current learning rate is.
    training_steps_sum = 0
    for i in range(len(training_steps_list)):
        training_steps_sum += training_steps_list[i]
        if training_step <= training_steps_sum:
            learning_rate_value = learning_rates_list[i]
            break
    # Pull the audio samples we'll use for training.
    train_fingerprints, train_ground_truth = audio_processor.get_data(
        FLAGS.batch_size, 0, model_settings, FLAGS.background_frequency,
        FLAGS.background_volume, time_shift_samples, 'training', sess)
    # Run the graph with this batch of training data.
    train_summary, train_accuracy, cross_entropy_value, _, _ = sess.run(
        [
            merged_summaries,
            evaluation_step,
            cross_entropy_mean,
            train_step,
            increment_global_step,
        ],
        feed_dict={
            fingerprint_input: train_fingerprints,
            ground_truth_input: train_ground_truth,
            learning_rate_input: learning_rate_value,
            dropout_rate: 0.5
        })
    train_writer.add_summary(train_summary, training_step)
    tf.compat.v1.logging.debug(
        'Step #%d: rate %f, accuracy %.1f%%, cross entropy %f' %
        (training_step, learning_rate_value, train_accuracy * 100,
         cross_entropy_value))
    is_last_step = (training_step == training_steps_max)
    if (training_step % FLAGS.eval_step_interval) == 0 or is_last_step:
        tf.compat.v1.logging.info(
            'Step #%d: rate %f, accuracy %.1f%%, cross entropy %f' %
            (training_step, learning_rate_value, train_accuracy * 100,
             cross_entropy_value))
        set_size = audio_processor.set_size('validation')
        total_accuracy = 0
        total_conf_matrix = None
        for i in range(0, set_size, FLAGS.batch_size):
            validation_fingerprints, validation_ground_truth = (
                audio_processor.get_data(FLAGS.batch_size, i, model_settings, 0.0,
                                         0.0, 0, 'validation', sess))
            # Run a validation step and capture training summaries for TensorBoard
            # with the `merged` op.
            validation_summary, validation_accuracy, conf_matrix = sess.run(
                [merged_summaries, evaluation_step, confusion_matrix],
                feed_dict={
                    fingerprint_input: validation_fingerprints,
                    ground_truth_input: validation_ground_truth,
                    dropout_rate: 0.0
                })
            validation_writer.add_summary(validation_summary, training_step)
            batch_size = min(FLAGS.batch_size, set_size - i)
            total_accuracy += (validation_accuracy * batch_size) / set_size
            if total_conf_matrix is None:
                total_conf_matrix = conf_matrix
            else:
                total_conf_matrix += conf_matrix
        tf.compat.v1.logging.info('Confusion Matrix:\n %s' % (total_conf_matrix))
        tf.compat.v1.logging.info('Step %d: Validation accuracy = %.1f%% (N=%d)' %
                                  (training_step, total_accuracy * 100, set_size))

    # Save the model checkpoint periodically.
    if (training_step % FLAGS.save_step_interval == 0 or
        training_step == training_steps_max):
        checkpoint_path = os.path.join(FLAGS.train_dir,
                                       FLAGS.model_architecture + '.ckpt')
        tf.compat.v1.logging.info('Saving to "%s-%d"', checkpoint_path,
                                  training_step)
        saver.save(sess, checkpoint_path, global_step=training_step)

set_size = audio_processor.set_size('testing')
tf.compat.v1.logging.info('set_size=%d', set_size)
total_accuracy = 0
total_conf_matrix = None
for i in range(0, set_size, FLAGS.batch_size):
    test_fingerprints, test_ground_truth = audio_processor.get_data(
        FLAGS.batch_size, i, model_settings, 0.0, 0.0, 0, 'testing', sess)
    test_accuracy, conf_matrix = sess.run(
        [evaluation_step, confusion_matrix],
        feed_dict={
            fingerprint_input: test_fingerprints,
            ground_truth_input: test_ground_truth,
            dropout_rate: 0.0
        })
    batch_size = min(FLAGS.batch_size, set_size - i)
    total_accuracy += (test_accuracy * batch_size) / set_size
    if total_conf_matrix is None:
        total_conf_matrix = conf_matrix
    else:
        total_conf_matrix += conf_matrix
tf.compat.v1.logging.warn('Confusion Matrix:\n %s' % (total_conf_matrix))
tf.compat.v1.logging.warn('Final test accuracy = %.1f%% (N=%d)' %
                          (total_accuracy * 100, set_size))
