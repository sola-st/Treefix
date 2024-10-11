# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with ops.name_scope('outer'):
    i = constant_op.constant(11)
    summ = summary_lib.scalar('inner', i)
    self.assertEqual(summ.op.name, 'outer/inner')
    summ_f = summary_lib.scalar('inner', i, family='family')
    self.assertEqual(summ_f.op.name, 'outer/family/inner')

metagraph_def, _ = meta_graph.export_scoped_meta_graph(export_scope='outer')

with ops.Graph().as_default() as g:
    meta_graph.import_scoped_meta_graph(metagraph_def, graph=g,
                                        import_scope='new_outer')
    # The summaries should exist, but with outer scope renamed.
    new_summ = g.get_tensor_by_name('new_outer/inner:0')
    new_summ_f = g.get_tensor_by_name('new_outer/family/inner:0')

    # However, the tags are unaffected.
    with self.cached_session() as s:
        new_summ_str, new_summ_f_str = s.run([new_summ, new_summ_f])
        new_summ_pb = summary_pb2.Summary()
        new_summ_pb.ParseFromString(new_summ_str)
        self.assertEqual('outer/inner', new_summ_pb.value[0].tag)
        new_summ_f_pb = summary_pb2.Summary()
        new_summ_f_pb.ParseFromString(new_summ_f_str)
        self.assertEqual('family/outer/family/inner',
                         new_summ_f_pb.value[0].tag)
