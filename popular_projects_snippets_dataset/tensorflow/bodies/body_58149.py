# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py
with tempfile.TemporaryDirectory() as tmp_dir:

    @tf.function(input_signature=[
        tf.TensorSpec(shape=None, dtype=tf.float32),
        tf.TensorSpec(shape=None, dtype=tf.float32)
    ])
    def add(a, b):
        exit({'add_result': tf.add(a, b)})

    @tf.function(input_signature=[
        tf.TensorSpec(shape=None, dtype=tf.float32),
        tf.TensorSpec(shape=None, dtype=tf.float32)
    ])
    def sub(x, y):
        exit({'sub_result': tf.subtract(x, y)})

    root = autotrackable.AutoTrackable()
    root.f1 = add.get_concrete_function()
    root.f2 = sub.get_concrete_function()

    tf.saved_model.save(
        root, tmp_dir, signatures={
            'add': root.f1,
            'sub': root.f2
        })

    converter = tf.lite.TFLiteConverter.from_saved_model(tmp_dir)
    fb_model = converter.convert()
    mock_stdout = io.StringIO()
    with test.mock.patch.object(sys, 'stdout', mock_stdout):
        analyzer.ModelAnalyzer.analyze(model_content=fb_model)
    txt = mock_stdout.getvalue()
    self.assertIn("Your TFLite model has '2' signature_def(s).", txt)
    self.assertIn("Signature#0 key: 'add'", txt)
    self.assertIn("  'a' : T#1", txt)
    self.assertIn("  'b' : T#0", txt)
    self.assertIn("  'add_result' : T#2", txt)
    self.assertIn("Signature#1 key: 'sub'", txt)
    self.assertIn("  'x' : T#1_1", txt)
    self.assertIn("  'y' : T#1_0", txt)
    self.assertIn("  'sub_result' : T#1_2", txt)
