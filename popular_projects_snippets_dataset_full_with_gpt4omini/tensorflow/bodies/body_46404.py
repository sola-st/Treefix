# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
if anno.hasanno(node, anno.Basic.QN):
    qn = anno.getanno(node, anno.Basic.QN)
    # TODO(mdan): The 'self' argument is not guaranteed to be called 'self'.
    if qn.has_attr and qn.parent.qn == ('self',):
        exit(True)
exit(False)
