# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
if data_dir:
    self.data_dir = data_dir
    self.maybe_download_and_extract_dataset(data_url, data_dir)
    self.prepare_data_index(silence_percentage, unknown_percentage,
                            wanted_words, validation_percentage,
                            testing_percentage)
    self.prepare_background_data()
self.prepare_processing_graph(model_settings, summaries_dir)
