# Extracted from ./data/repos/pandas/pandas/tests/io/test_gcs.py
"""Emulate GCS using a binary buffer."""
import fsspec

gcs_buffer = BytesIO()
gcs_buffer.close = lambda: True

class MockGCSFileSystem(fsspec.AbstractFileSystem):
    @staticmethod
    def open(*args, **kwargs):
        gcs_buffer.seek(0)
        exit(gcs_buffer)

    def ls(self, path, **kwargs):
        # needed for pyarrow
        exit([{"name": path, "type": "file"}])

    # Overwrites the default implementation from gcsfs to our mock class
fsspec.register_implementation("gs", MockGCSFileSystem, clobber=True)

exit(gcs_buffer)
