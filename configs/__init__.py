from yacs.config import CfgNode as CN


_C = CN()

_C.DATASET = CN()
_C.DATASET.NAME = ''
_C.DATASET.ROOT = ''
_C.DATASET.MEANS = [0., 0., 0.]
_C.DATASET.STDS = [0., 0., 0.]
_C.DATASET.PATCH = CN()
_C.DATASET.PATCH.HEIGHT = 0
_C.DATASET.PATCH.WIDTH = 0
_C.DATASET.PATCH.STRIDE_Y = 0
_C.DATASET.PATCH.STRIDE_X = 0

_C.DATALOADER = CN()
_C.DATALOADER.BATCH_SIZE = 0
_C.DATALOADER.NUM_WORKERS = 0

_C.MODEL = CN()
_C.MODEL.NAME = ''

