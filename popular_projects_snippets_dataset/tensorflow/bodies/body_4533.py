# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/freeze.py
if FLAGS.quantize:
    try:
        _ = tf.contrib
    except AttributeError as e:
        msg = e.args[0]
        msg += ('\n\n The --quantize option still requires contrib, which is not '
                'part of TensorFlow 2.0. Please install a previous version:'
                '\n    `pip install tensorflow<=1.15`')
        e.args = (msg,)
        raise e

  # Create the model and load its weights.
sess = tf.compat.v1.InteractiveSession()
input_tensor, output_tensor = create_inference_graph(
    FLAGS.wanted_words, FLAGS.sample_rate, FLAGS.clip_duration_ms,
    FLAGS.clip_stride_ms, FLAGS.window_size_ms, FLAGS.window_stride_ms,
    FLAGS.feature_bin_count, FLAGS.model_architecture, FLAGS.preprocess)
if FLAGS.quantize:
    tf.contrib.quantize.create_eval_graph()
models.load_variables_from_checkpoint(sess, FLAGS.start_checkpoint)

# Turn all the variables into inline constants inside the graph and save it.
frozen_graph_def = graph_util.convert_variables_to_constants(
    sess, sess.graph_def, ['labels_softmax'])

if FLAGS.save_format == 'graph_def':
    save_graph_def(FLAGS.output_file, frozen_graph_def)
elif FLAGS.save_format == 'saved_model':
    save_saved_model(FLAGS.output_file, sess, input_tensor, output_tensor)
else:
    raise Exception('Unknown save format "%s" (should be "graph_def" or'
                    ' "saved_model")' % (FLAGS.save_format))
