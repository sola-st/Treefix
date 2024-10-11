# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/generate_streaming_test_wav.py
"""Mixes the sample data into the main track at the specified offset.

  Args:
    track_data: Numpy array holding main audio data. Modified in-place.
    track_offset: Where to mix the sample into the main track.
    sample_data: Numpy array of audio data to mix into the main track.
    sample_offset: Where to start in the audio sample.
    clip_duration: How long the sample segment is.
    sample_volume: Loudness to mix the sample in at.
    ramp_in: Length in samples of volume increase stage.
    ramp_out: Length in samples of volume decrease stage.
  """
ramp_out_index = clip_duration - ramp_out
track_end = min(track_offset + clip_duration, track_data.shape[0])
track_end = min(track_end,
                track_offset + (sample_data.shape[0] - sample_offset))
sample_range = track_end - track_offset
for i in range(sample_range):
    if i < ramp_in:
        envelope_scale = i / ramp_in
    elif i > ramp_out_index:
        envelope_scale = (clip_duration - i) / ramp_out
    else:
        envelope_scale = 1
    sample_input = sample_data[sample_offset + i]
    track_data[track_offset
               + i] += sample_input * envelope_scale * sample_volume
