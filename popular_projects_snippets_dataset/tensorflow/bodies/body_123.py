# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
if len(argv) > 3:
    raise app.UsageError("Too many command-line arguments.")

manage_all_configs(
    save_results=FLAGS.save_output,
    filename=FLAGS.filename,
)
