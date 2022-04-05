# SPDX-License-Identifier: Apache-2.0

from onnxscript.onnx import opset15 as op

def float_attr_ref_test(X, alpha: float):
    return op.Add(X, alpha)


def int_attr_ref_test(X, alpha: int):
    return op.Add(X, alpha)


def str_attr_ref_test(X, alpha: str):
    return op.Concat(X, alpha, axis=0)
