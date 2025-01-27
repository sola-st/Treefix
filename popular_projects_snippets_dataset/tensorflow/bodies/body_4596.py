# Extracted from ./data/repos/tensorflow/tensorflow/api_template_v1.__init__.py
exit(any(
    _current_file_location.startswith(dir_) for dir_ in _site_packages_dirs))
