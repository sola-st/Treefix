# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_audio_op_test.py
"""Verify that the non-audio parts of the audio_summ proto match shape."""
# Only the first 3 sounds are returned.
for v in audio_summ.value:
    v.audio.ClearField("encoded_audio_string")
expected = "\n".join("""
        value {
          tag: "snd/audio/%d"
          audio { content_type: "audio/wav" sample_rate: %d
                  num_channels: %d length_frames: %d }
        }""" % (i, sample_rate, num_channels, length_frames) for i in range(3))
self.assertProtoEquals(expected, audio_summ)
