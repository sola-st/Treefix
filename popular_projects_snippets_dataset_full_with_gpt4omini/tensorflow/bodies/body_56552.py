# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize_test.py
model = test_utils.build_mock_flatbuffer_model()
tmp_dir = self.get_temp_dir()
model_filename = os.path.join(tmp_dir, 'model.tflite')
with open(model_filename, 'wb') as model_file:
    model_file.write(model)

html_text = visualize.create_html(model_filename)

# It's hard to test debug output without doing a full HTML parse,
# but at least sanity check that expected identifiers are present.
self.assertRegex(
    html_text, re.compile(r'%s' % model_filename, re.MULTILINE | re.DOTALL))
self.assertRegex(html_text,
                 re.compile(r'input_tensor', re.MULTILINE | re.DOTALL))
self.assertRegex(html_text,
                 re.compile(r'constant_tensor', re.MULTILINE | re.DOTALL))
self.assertRegex(html_text, re.compile(r'ADD', re.MULTILINE | re.DOTALL))
