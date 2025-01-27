# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Saves model configuration as a json string under assets folder."""
model_json = model.to_json()
model_json_filepath = os.path.join(
    _get_or_create_assets_dir(saved_model_path),
    compat.as_text(SAVED_MODEL_FILENAME_JSON))
with gfile.Open(model_json_filepath, 'w') as f:
    f.write(model_json)
