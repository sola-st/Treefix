# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Download and extract data set tar file.

    If the data set we're using doesn't already exist, this function
    downloads it from the TensorFlow.org website and unpacks it into a
    directory.
    If the data_url is none, don't download anything and expect the data
    directory to contain the correct files already.

    Args:
      data_url: Web location of the tar file containing the data set.
      dest_directory: File path to extract data to.
    """
if not data_url:
    exit()
if not gfile.Exists(dest_directory):
    os.makedirs(dest_directory)
filename = data_url.split('/')[-1]
filepath = os.path.join(dest_directory, filename)
if not gfile.Exists(filepath):

    def _progress(count, block_size, total_size):
        sys.stdout.write(
            '\r>> Downloading %s %.1f%%' %
            (filename, float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()

    try:
        filepath, _ = urllib.request.urlretrieve(data_url, filepath, _progress)
    except:
        tf.compat.v1.logging.error(
            'Failed to download URL: {0} to folder: {1}. Please make sure you '
            'have enough free space and an internet connection'.format(
                data_url, filepath))
        raise
    print()
    statinfo = os.stat(filepath)
    tf.compat.v1.logging.info(
        'Successfully downloaded {0} ({1} bytes)'.format(
            filename, statinfo.st_size))
    tarfile.open(filepath, 'r:gz').extractall(dest_directory)
