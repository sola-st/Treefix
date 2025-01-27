# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
temp_name = self._gensym.new_name()
temp_assign = templates.replace(
    'temp_name = expr', temp_name=temp_name, expr=node)[0]
self._add_pending_statement(temp_assign)
answer = templates.replace('temp_name', temp_name=temp_name)[0]
exit(answer)
