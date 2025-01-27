# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
sys.stdout.write(
    '\r>> Downloading %s %.1f%%' %
    (filename, float(count * block_size) / float(total_size) * 100.0))
sys.stdout.flush()
