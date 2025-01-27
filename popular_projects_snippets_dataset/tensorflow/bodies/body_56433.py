# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
graph_def = self._MakeGraphDef("""
    node { name: 'A' op: 'IntOutput' }
    node { name: 'B' op: 'IntInput' input: 'A:0' }
    """)

with ops.Graph().as_default():
    # Initial import
    a, b = importer.import_graph_def(
        graph_def,
        return_elements=["A", "B"],
        name="")
    self.assertEqual(a.name, "A")
    self.assertEqual(b.name, "B")
    self.assertEqual(list(b.inputs), [a.outputs[0]])

    # Repeat the same import
    a1, b1 = importer.import_graph_def(
        graph_def,
        return_elements=["A", "B"],
        name="")
    self.assertEqual(a1.name, "A_1")
    self.assertEqual(b1.name, "B_1")
    self.assertEqual(list(b1.inputs), [a1.outputs[0]])

    # Repeat the same import again
    a2, b2 = importer.import_graph_def(
        graph_def,
        return_elements=["A", "B"],
        name="")
    self.assertEqual(a2.name, "A_2")
    self.assertEqual(b2.name, "B_2")
    self.assertEqual(list(b2.inputs), [a2.outputs[0]])

    # Import with an already-used name
    a3, b3 = importer.import_graph_def(
        graph_def,
        return_elements=["A", "B"],
        name="A")
    self.assertEqual(a3.name, "A_3/A")
    self.assertEqual(b3.name, "A_3/B")
    self.assertEqual(list(b3.inputs), [a3.outputs[0]])

    # Import with an already-used name but with a '/' to indicate an
    # "absolute" name scope (see the Graph.name_scope docstring).
    a_a, a_b = importer.import_graph_def(
        graph_def,
        return_elements=["A", "B"],
        name="A/")
    self.assertEqual(a_a.name, "A/A")
    self.assertEqual(a_b.name, "A/B")
    self.assertEqual(list(a_b.inputs), [a_a.outputs[0]])

    # Repeat the same import.
    a_a1, a_b1 = importer.import_graph_def(
        graph_def,
        return_elements=["A", "B"],
        name="A/")
    self.assertEqual(a_a1.name, "A/A_1")
    self.assertEqual(a_b1.name, "A/B_1")
    self.assertEqual(list(a_b1.inputs), [a_a1.outputs[0]])

    # Import with existing de-duped node names
    a1_1, b1_1 = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A_1' op: 'IntOutput' }
          node { name: 'B_1' op: 'IntInput' input: 'A_1:0' }
          """),
        return_elements=["A_1", "B_1"],
        name="")
    self.assertEqual(a1_1.name, "A_1_1")
    self.assertEqual(b1_1.name, "B_1_1")
    self.assertEqual(list(b1_1.inputs), [a1_1.outputs[0]])

    # Create a name scope and then import node with same name
    with ops.name_scope("foo"):
        constant_op.constant(1)
    foo, = importer.import_graph_def(
        self._MakeGraphDef("node { name: 'foo' op: 'IntOutput' }"),
        return_elements=["foo"],
        name="")
    self.assertEqual(foo.name, "foo_1")

    # Imported node name can't conflict with intermediate name scope (but can
    # conflict with outer scope and full name scope)
    with ops.name_scope("outer"):
        with ops.name_scope("inner"):
            c = constant_op.constant(1, name="c")
            self.assertEqual(c.op.name, "outer/inner/c")

    outer, inner, new_c, outer_inner, outer_inner_c = (
        importer.import_graph_def(
            self._MakeGraphDef(
                "node { name: 'outer' op: 'IntOutput' }"
                "node { name: 'inner' op: 'IntOutput' }"
                "node { name: 'c' op: 'IntOutput' }"
                "node { name: 'outer/inner' op: 'IntOutput' }"
                "node { name: 'outer/inner/c' op: 'IntOutput' }"),
            return_elements=["outer", "inner", "c", "outer/inner",
                             "outer/inner/c"],
            name=""))
    self.assertEqual(outer.name, "outer_1")
    self.assertEqual(inner.name, "inner")
    self.assertEqual(new_c.name, "c")
    self.assertEqual(outer_inner.name, "outer/inner_1")
    self.assertEqual(outer_inner_c.name, "outer/inner/c_1")
