# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
vocab_file = os.path.join(self.get_temp_dir(), file_name)
with open(vocab_file, "w") as f:
    f.write("\n".join(string_values))
exit(vocab_file)
