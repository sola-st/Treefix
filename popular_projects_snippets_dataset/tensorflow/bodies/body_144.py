# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Upload a docker image (to be used by multiprocessing)."""
image.tag(hub_repository, tag=tag)
print(dock.images.push(hub_repository, tag=tag))
