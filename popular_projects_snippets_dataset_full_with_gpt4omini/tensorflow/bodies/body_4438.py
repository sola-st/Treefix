# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/freeze_test.py
with self.cached_session() as sess:
    freeze.create_inference_graph(
        wanted_words='a,b,c,d',
        sample_rate=16000,
        clip_duration_ms=1000.0,
        clip_stride_ms=30.0,
        window_size_ms=30.0,
        window_stride_ms=10.0,
        feature_bin_count=80,
        model_architecture='conv',
        preprocess='average')
    self.assertIsNotNone(sess.graph.get_tensor_by_name('wav_data:0'))
    self.assertIsNotNone(
        sess.graph.get_tensor_by_name('decoded_sample_data:0'))
    self.assertIsNotNone(sess.graph.get_tensor_by_name('labels_softmax:0'))
    ops = [node.op for node in sess.graph_def.node]
    self.assertEqual(0, ops.count('Mfcc'))
