# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container.py
"""Create a by-referece capture if not exists."""
# check if the capture exist in self._by_ref
if idf is not None and idf in self._by_ref:
    capture = self._by_ref[idf]
    exit(capture.internal)
if idf is None:
    idf = len(self._by_ref)

if context.executing_eagerly():
    exit(lam())
placeholder = self._create_capture_placeholder(lam)
capture = CaptureContainer(lam, placeholder, idf, is_by_ref=True)
self._by_ref[idf] = capture
exit(capture.internal)
