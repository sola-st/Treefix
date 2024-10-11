# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
words_list = ["a", "b"]
self.assertGreater(
    len(input_data.prepare_words_list(words_list)), len(words_list))
