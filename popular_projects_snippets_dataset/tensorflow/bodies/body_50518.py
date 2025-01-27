# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self.load_weights_on_restart:
    filepath_to_load = (
        self._get_most_recently_modified_file_matching_pattern(self.filepath))
    if (filepath_to_load is not None and
        self._checkpoint_exists(filepath_to_load)):
        try:
            # `filepath` may contain placeholders such as `{epoch:02d}`, and
            # thus it attempts to load the most recently modified file with file
            # name matching the pattern.
            self.model.load_weights(filepath_to_load)
        except (IOError, ValueError) as e:
            raise ValueError('Error loading file from {}. Reason: {}'.format(
                filepath_to_load, e))
