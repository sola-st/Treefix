# Extracted from https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
#%%

def _to_json_dict_with_strings(dictionary):
    """
    Convert dict to dict with leafs only being strings. So it recursively makes keys to strings
    if they are not dictionaries.

    Use case:
        - saving dictionary of tensors (convert the tensors to strins!)
        - saving arguments from script (e.g. argparse) for it to be pretty

    e.g.

    """
    if type(dictionary) != dict:
        return str(dictionary)
    d = {k: _to_json_dict_with_strings(v) for k, v in dictionary.items()}
    return d

def to_json(dic):
    import types
    import argparse

    if type(dic) is dict:
        dic = dict(dic)
    else:
        dic = dic.__dict__
    return _to_json_dict_with_strings(dic)

def save_to_json_pretty(dic, path, mode='w', indent=4, sort_keys=True):
    import json

    with open(path, mode) as f:
        json.dump(to_json(dic), f, indent=indent, sort_keys=sort_keys)

def my_pprint(dic):
    """

    @param dic:
    @return:

    Note: this is not the same as pprint.
    """
    import json

    # make all keys strings recursively with their naitve str function
    dic = to_json(dic)
    # pretty print
    pretty_dic = json.dumps(dic, indent=4, sort_keys=True)
    print(pretty_dic)
    # print(json.dumps(dic, indent=4, sort_keys=True))
    # return pretty_dic

import torch
# import json  # results in non serializabe errors for torch.Tensors
from pprint import pprint

dic = {'x': torch.randn(1, 3), 'rec': {'y': torch.randn(1, 3)}}

my_pprint(dic)
pprint(dic)

{
    "rec": {
        "y": "tensor([[-0.3137,  0.3138,  1.2894]])"
    },
    "x": "tensor([[-1.5909,  0.0516, -1.5445]])"
}
{'rec': {'y': tensor([[-0.3137,  0.3138,  1.2894]])},
 'x': tensor([[-1.5909,  0.0516, -1.5445]])}

TypeError: tensor is not JSON serializable

    pprint(stats, indent=4, sort_dicts=True)

{   'cca': {   'all': {'avg': tensor(0.5132), 'std': tensor(0.1532)},
               'avg': tensor([0.5993, 0.5571, 0.4910, 0.4053]),
               'rep': {'avg': tensor(0.5491), 'std': tensor(0.0743)},
               'std': tensor([0.0316, 0.0368, 0.0910, 0.2490])},
    'cka': {   'all': {'avg': tensor(0.7885), 'std': tensor(0.3449)},
               'avg': tensor([1.0000, 0.9840, 0.9442, 0.2260]),
               'rep': {'avg': tensor(0.9761), 'std': tensor(0.0468)},
               'std': tensor([5.9043e-07, 2.9688e-02, 6.3634e-02, 2.1686e-01])},
    'cosine': {   'all': {'avg': tensor(0.5931), 'std': tensor(0.7158)},
                  'avg': tensor([ 0.9825,  0.9001,  0.7909, -0.3012]),
                  'rep': {'avg': tensor(0.8912), 'std': tensor(0.1571)},
                  'std': tensor([0.0371, 0.1232, 0.1976, 0.9536])},
    'nes': {   'all': {'avg': tensor(0.6771), 'std': tensor(0.2891)},
               'avg': tensor([0.9326, 0.8038, 0.6852, 0.2867]),
               'rep': {'avg': tensor(0.8072), 'std': tensor(0.1596)},
               'std': tensor([0.0695, 0.1266, 0.1578, 0.2339])},
    'nes_output': {   'all': {'avg': None, 'std': None},
                      'avg': tensor(0.2975),
                      'rep': {'avg': None, 'std': None},
                      'std': tensor(0.0945)},
    'query_loss': {   'all': {'avg': None, 'std': None},
                      'avg': tensor(12.3746),
                      'rep': {'avg': None, 'std': None},
                      'std': tensor(13.7910)}}

{
    "cca": {
        "all": {
            "avg": "tensor(0.5144)",
            "std": "tensor(0.1553)"
        },
        "avg": "tensor([0.6023, 0.5612, 0.4874, 0.4066])",
        "rep": {
            "avg": "tensor(0.5503)",
            "std": "tensor(0.0796)"
        },
        "std": "tensor([0.0285, 0.0367, 0.1004, 0.2493])"
    },
    "cka": {
        "all": {
            "avg": "tensor(0.7888)",
            "std": "tensor(0.3444)"
        },
        "avg": "tensor([1.0000, 0.9840, 0.9439, 0.2271])",
        "rep": {
            "avg": "tensor(0.9760)",
            "std": "tensor(0.0468)"
        },
        "std": "tensor([5.7627e-07, 2.9689e-02, 6.3541e-02, 2.1684e-01])"
    },
    "cosine": {
        "all": {
            "avg": "tensor(0.5945)",
            "std": "tensor(0.7146)"
        },
        "avg": "tensor([ 0.9825,  0.9001,  0.7907, -0.2953])",
        "rep": {
            "avg": "tensor(0.8911)",
            "std": "tensor(0.1571)"
        },
        "std": "tensor([0.0371, 0.1231, 0.1975, 0.9554])"
    },
    "nes": {
        "all": {
            "avg": "tensor(0.6773)",
            "std": "tensor(0.2886)"
        },
        "avg": "tensor([0.9326, 0.8037, 0.6849, 0.2881])",
        "rep": {
            "avg": "tensor(0.8070)",
            "std": "tensor(0.1595)"
        },
        "std": "tensor([0.0695, 0.1265, 0.1576, 0.2341])"
    },
    "nes_output": {
        "all": {
            "avg": "None",
            "std": "None"
        },
        "avg": "tensor(0.2976)",
        "rep": {
            "avg": "None",
            "std": "None"
        },
        "std": "tensor(0.0945)"
    },
    "query_loss": {
        "all": {
            "avg": "None",
            "std": "None"
        },
        "avg": "tensor(12.3616)",
        "rep": {
            "avg": "None",
            "std": "None"
        },
        "std": "tensor(13.7976)"
    }
}

