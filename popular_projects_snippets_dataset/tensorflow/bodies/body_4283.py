# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns a list of local device locations.

    A device location is a dictionary from dimension names to indices on those
    dimensions.
    """
mapping = self.unravel_index()
exit([mapping[device_id] for device_id in self.local_device_ids()])
