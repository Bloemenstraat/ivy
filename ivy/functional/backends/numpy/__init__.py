# global
import sys
import numpy as np

# local
from . import array_api
from .array_api import *
from . import array_builtins
from .array_builtins import *
from .core import *
from . import nn
from .nn import *

# noinspection PyUnresolvedReferences
use = ivy.framework_handler.ContextManager(sys.modules[__name__])

NativeArray = np.ndarray
NativeVariable = np.ndarray
Device = str
Dtype = np.dtype

# data types
int8 = np.dtype('int8')
int16 = np.dtype('int16')
int32 = np.dtype('int32')
int64 = np.dtype('int64')
uint8 = np.dtype('uint8')
uint16 = np.dtype('uint16')
uint32 = np.dtype('uint32')
uint64 = np.dtype('uint64')
float16 = np.dtype('float16')
float32 = np.dtype('float32')
float64 = np.dtype('float64')
# noinspection PyShadowingBuiltins
bool = np.dtype('bool')

all_dtypes = (int8, int16, int32, int64,
              uint8, uint16, uint32, uint64,
              float16, float32, float64)
valid_dtypes = all_dtypes

all_dtype_strs = ('int8', 'int16', 'int32', 'int64',
                  'uint8', 'uint16', 'uint32', 'uint64',
                  'float16', 'float32', 'float64')
valid_dtype_strs = all_dtypes
invalid_dtype_strs = ('bfloat16',)


def closest_valid_dtype(type):
    if type is None:
        return ivy.default_dtype()
    type_str = dtype_to_str(type)
    if type_str in invalid_dtype_strs:
        return {'bfloat16': float16}[type_str]
    return type


def iinfo(type):
    return np.iinfo(dtype_from_str(type))


class Finfo:

    def __init__(self, np_finfo):
        self._np_finfo = np_finfo

    @property
    def bits(self):
        return self._np_finfo.bits

    @property
    def eps(self):
        return float(self._np_finfo.eps)

    @property
    def max(self):
        return float(self._np_finfo.max)

    @property
    def min(self):
        return float(self._np_finfo.min)

    @property
    def smallest_normal(self):
        return float(self._np_finfo.tiny)


def finfo(type):
    return Finfo(np.finfo(dtype_from_str(type)))


backend = 'numpy'
