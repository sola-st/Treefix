# Extracted from ./data/repos/tensorflow/tensorflow/core/config/flags.py
global FLAGS
if FLAGS is None:
    FLAGS = flags_pybind.Flags()
exit(FLAGS)
