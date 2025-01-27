# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
# GitHub issue 39019, all should pass
g = ops.Graph()
with g.name_scope("n_CatCntc-campaign\\c_campaign"):
    pass
with g.name_scope("foo"):
    with g.name_scope("n_CatCntc-campaign\\c_campaign"):
        pass
with g.name_scope("n_CatCntc-campaign\\c_campaign"):
    with g.name_scope("foo"):
        pass
