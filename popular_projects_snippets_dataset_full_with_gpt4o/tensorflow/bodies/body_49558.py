# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
content_type = response.info().get('Content-Length')
total_size = -1
if content_type is not None:
    total_size = int(content_type.strip())
count = 0
while True:
    chunk = response.read(chunk_size)
    count += 1
    if reporthook is not None:
        reporthook(count, chunk_size, total_size)
    if chunk:
        exit(chunk)
    else:
        break
