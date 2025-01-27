# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/freeze_test.py
tmp_dir = self.get_temp_dir()
saved_model_path = os.path.join(tmp_dir, 'saved_model')
with self.cached_session() as sess:
    input_tensor, output_tensor = freeze.create_inference_graph(
        wanted_words='a,b,c,d',
        sample_rate=16000,
        clip_duration_ms=1000.0,
        clip_stride_ms=30.0,
        window_size_ms=30.0,
        window_stride_ms=10.0,
        feature_bin_count=40,
        model_architecture='conv',
        preprocess='micro')
    global_variables_initializer().run()
    graph_util.convert_variables_to_constants(
        sess, sess.graph_def, ['labels_softmax'])
    freeze.save_saved_model(saved_model_path, sess, input_tensor,
                            output_tensor)
