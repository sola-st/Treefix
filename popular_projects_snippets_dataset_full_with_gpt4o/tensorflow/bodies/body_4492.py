# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav_dir.py
"""Entry point for script, converts flags to arguments."""
label_wav(FLAGS.wav_dir, FLAGS.labels, FLAGS.graph, FLAGS.input_name,
          FLAGS.output_name, FLAGS.how_many_labels)
