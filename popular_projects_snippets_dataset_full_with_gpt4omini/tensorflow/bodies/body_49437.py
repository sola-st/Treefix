# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
# As soon as we've seen the object more than once, we want to attach the
# shared object ID. This allows us to only attach the shared object ID when
# it's strictly necessary, making backwards compatibility breakage less
# likely.
if self.ref_count == 1:
    self[SHARED_OBJECT_KEY] = self.object_id
self.ref_count += 1
