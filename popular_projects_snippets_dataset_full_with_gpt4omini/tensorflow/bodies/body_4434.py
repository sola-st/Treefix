# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/test_streaming_accuracy.py
label_list = read_label_file(FLAGS.labels)
sample_rate, data = read_wav_file(FLAGS.wav)
# Init instance of RecognizeCommands with given parameters.
recognize_commands = RecognizeCommands(
    labels=label_list,
    average_window_duration_ms=FLAGS.average_window_duration_ms,
    detection_threshold=FLAGS.detection_threshold,
    suppression_ms=FLAGS.suppression_ms,
    minimum_count=4)

# Init instance of StreamingAccuracyStats and load ground truth.
stats = StreamingAccuracyStats()
stats.read_ground_truth_file(FLAGS.ground_truth)
recognize_element = RecognizeResult()
all_found_words = []
data_samples = data.shape[0]
clip_duration_samples = int(FLAGS.clip_duration_ms * sample_rate / 1000)
clip_stride_samples = int(FLAGS.clip_stride_ms * sample_rate / 1000)
audio_data_end = data_samples - clip_duration_samples

# Load model and create a tf session to process audio pieces
recognize_graph = load_graph(FLAGS.model)
with recognize_graph.as_default():
    with tf.compat.v1.Session() as sess:

        # Get input and output tensor
        data_tensor = sess.graph.get_tensor_by_name(FLAGS.input_names[0])
        sample_rate_tensor = sess.graph.get_tensor_by_name(FLAGS.input_names[1])
        output_softmax_tensor = sess.graph.get_tensor_by_name(FLAGS.output_name)

        # Inference along audio stream.
        for audio_data_offset in range(0, audio_data_end, clip_stride_samples):
            input_start = audio_data_offset
            input_end = audio_data_offset + clip_duration_samples
            outputs = sess.run(
                output_softmax_tensor,
                feed_dict={
                    data_tensor:
                        numpy.expand_dims(data[input_start:input_end], axis=-1),
                    sample_rate_tensor:
                        sample_rate
                })
            outputs = numpy.squeeze(outputs)
            current_time_ms = int(audio_data_offset * 1000 / sample_rate)
            try:
                recognize_commands.process_latest_result(outputs, current_time_ms,
                                                         recognize_element)
            except ValueError as e:
                tf.compat.v1.logging.error('Recognition processing failed: {}' % e)
                exit()
            if (recognize_element.is_new_command and
                recognize_element.founded_command != '_silence_'):
                all_found_words.append(
                    [recognize_element.founded_command, current_time_ms])
                if FLAGS.verbose:
                    stats.calculate_accuracy_stats(all_found_words, current_time_ms,
                                                   FLAGS.time_tolerance_ms)
                    try:
                        recognition_state = stats.delta()
                    except ValueError as e:
                        tf.compat.v1.logging.error(
                            'Statistics delta computing failed: {}'.format(e))
                    else:
                        tf.compat.v1.logging.info('{}ms {}:{}{}'.format(
                            current_time_ms, recognize_element.founded_command,
                            recognize_element.score, recognition_state))
                        stats.print_accuracy_stats()
stats.calculate_accuracy_stats(all_found_words, -1, FLAGS.time_tolerance_ms)
stats.print_accuracy_stats()
