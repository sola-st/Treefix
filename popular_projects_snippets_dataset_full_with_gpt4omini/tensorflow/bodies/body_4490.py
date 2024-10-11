# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav_dir.py
"""Runs the audio data through the graph and prints predictions."""
with tf.compat.v1.Session() as sess:
    # Feed the audio data as input to the graph.
    #   predictions  will contain a two-dimensional array, where one
    #   dimension represents the input image count, and the other has
    #   predictions per class
    for wav_path in glob.glob(wav_dir + '/*.wav'):
        if not wav_path or not tf.io.gfile.exists(wav_path):
            raise ValueError('Audio file does not exist at {0}'.format(wav_path))
        with open(wav_path, 'rb') as wav_file:
            wav_data = wav_file.read()

        softmax_tensor = sess.graph.get_tensor_by_name(output_layer_name)
        predictions, = sess.run(softmax_tensor, {input_layer_name: wav_data})

        # Sort to show labels in order of confidence
        print('\n%s' % (wav_path.split('/')[-1]))
        top_k = predictions.argsort()[-num_top_predictions:][::-1]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))

    exit(0)
