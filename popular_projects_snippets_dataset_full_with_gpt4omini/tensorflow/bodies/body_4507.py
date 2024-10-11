# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/generate_streaming_test_wav.py
words_list = input_data.prepare_words_list(FLAGS.wanted_words.split(','))
model_settings = models.prepare_model_settings(
    len(words_list), FLAGS.sample_rate, FLAGS.clip_duration_ms,
    FLAGS.window_size_ms, FLAGS.window_stride_ms, FLAGS.feature_bin_count,
    'mfcc')
audio_processor = input_data.AudioProcessor(
    '', FLAGS.data_dir, FLAGS.silence_percentage, 10,
    FLAGS.wanted_words.split(','), FLAGS.validation_percentage,
    FLAGS.testing_percentage, model_settings, FLAGS.data_dir)

output_audio_sample_count = FLAGS.sample_rate * FLAGS.test_duration_seconds
output_audio = np.zeros((output_audio_sample_count,), dtype=np.float32)

# Set up background audio.
background_crossover_ms = 500
background_segment_duration_ms = (
    FLAGS.clip_duration_ms + background_crossover_ms)
background_segment_duration_samples = int(
    (background_segment_duration_ms * FLAGS.sample_rate) / 1000)
background_segment_stride_samples = int(
    (FLAGS.clip_duration_ms * FLAGS.sample_rate) / 1000)
background_ramp_samples = int(
    ((background_crossover_ms / 2) * FLAGS.sample_rate) / 1000)

# Mix the background audio into the main track.
how_many_backgrounds = int(
    math.ceil(output_audio_sample_count / background_segment_stride_samples))
for i in range(how_many_backgrounds):
    output_offset = int(i * background_segment_stride_samples)
    background_index = np.random.randint(len(audio_processor.background_data))
    background_samples = audio_processor.background_data[background_index]
    background_offset = np.random.randint(
        0, len(background_samples) - model_settings['desired_samples'])
    background_volume = np.random.uniform(0, FLAGS.background_volume)
    mix_in_audio_sample(output_audio, output_offset, background_samples,
                        background_offset, background_segment_duration_samples,
                        background_volume, background_ramp_samples,
                        background_ramp_samples)

# Mix the words into the main track, noting their labels and positions.
output_labels = []
word_stride_ms = FLAGS.clip_duration_ms + FLAGS.word_gap_ms
word_stride_samples = int((word_stride_ms * FLAGS.sample_rate) / 1000)
clip_duration_samples = int(
    (FLAGS.clip_duration_ms * FLAGS.sample_rate) / 1000)
word_gap_samples = int((FLAGS.word_gap_ms * FLAGS.sample_rate) / 1000)
how_many_words = int(
    math.floor(output_audio_sample_count / word_stride_samples))
all_test_data, all_test_labels = audio_processor.get_unprocessed_data(
    -1, model_settings, 'testing')
for i in range(how_many_words):
    output_offset = (
        int(i * word_stride_samples) + np.random.randint(word_gap_samples))
    output_offset_ms = (output_offset * 1000) / FLAGS.sample_rate
    is_unknown = np.random.randint(100) < FLAGS.unknown_percentage
    if is_unknown:
        wanted_label = input_data.UNKNOWN_WORD_LABEL
    else:
        wanted_label = words_list[2 + np.random.randint(len(words_list) - 2)]
    test_data_start = np.random.randint(len(all_test_data))
    found_sample_data = None
    index_lookup = np.arange(len(all_test_data), dtype=np.int32)
    np.random.shuffle(index_lookup)
    for test_data_offset in range(len(all_test_data)):
        test_data_index = index_lookup[(
            test_data_start + test_data_offset) % len(all_test_data)]
        current_label = all_test_labels[test_data_index]
        if current_label == wanted_label:
            found_sample_data = all_test_data[test_data_index]
            break
    mix_in_audio_sample(output_audio, output_offset, found_sample_data, 0,
                        clip_duration_samples, 1.0, 500, 500)
    output_labels.append({'label': wanted_label, 'time': output_offset_ms})

input_data.save_wav_file(FLAGS.output_audio_file, output_audio,
                         FLAGS.sample_rate)
tf.compat.v1.logging.info('Saved streaming test wav to %s',
                          FLAGS.output_audio_file)

with open(FLAGS.output_labels_file, 'w') as f:
    for output_label in output_labels:
        f.write('%s, %f\n' % (output_label['label'], output_label['time']))
tf.compat.v1.logging.info('Saved streaming test labels to %s',
                          FLAGS.output_labels_file)
