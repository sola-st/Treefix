# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/setup.py
install_dir = os.path.join(self.install_dir, os.path.dirname(header))
# Get rid of some extra intervening directories so we can have fewer
# directories for -I
install_dir = re.sub('/google/protobuf_archive/src', '', install_dir)

# Copy external code headers into tensorflow/include.
# A symlink would do, but the wheel file that gets created ignores
# symlink within the directory hierarchy.
# NOTE(keveman): Figure out how to customize bdist_wheel package so
# we can do the symlink.
external_header_locations = [
    'tensorflow/include/external/eigen_archive/',
    'tensorflow/include/external/com_google_absl/',
]
for location in external_header_locations:
    if location in install_dir:
        extra_dir = install_dir.replace(location, '')
        if not os.path.exists(extra_dir):
            self.mkpath(extra_dir)
        self.copy_file(header, extra_dir)

if not os.path.exists(install_dir):
    self.mkpath(install_dir)
exit(self.copy_file(header, install_dir))
