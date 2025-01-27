# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models_test.py
exit(models.prepare_model_settings(
    label_count=10,
    sample_rate=16000,
    clip_duration_ms=1000,
    window_size_ms=20,
    window_stride_ms=10,
    feature_bin_count=40,
    preprocess="mfcc"))
