# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
exit(old_doc.replace('`%s`' % old_argument,
                       '`%s`' % new_argument).replace('%s:' % old_argument,
                                                      '%s:' % new_argument))
