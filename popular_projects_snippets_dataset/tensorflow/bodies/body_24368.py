# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
# Create the .par file first.
temp_file_path = os.path.join(self.get_temp_dir(), "model.py")
with open(temp_file_path, "wb") as f:
    f.write(b"import tensorflow as tf\nx = tf.constant(42.0)\n")
par_path = os.path.join(self.get_temp_dir(), "train_model.par")
with zipfile.ZipFile(par_path, "w") as zf:
    zf.write(temp_file_path, os.path.join("tensorflow_models", "model.py"))

source_path = os.path.join(par_path, "tensorflow_models", "nonexistent.py")
with self.assertRaisesRegex(IOError,
                            "neither exists nor can be loaded.*par.*"):
    source_utils.load_source(source_path)
