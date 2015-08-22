from pytraj.datasetlist import _groupby
from pytraj.datasetlist import DatasetList


class BaseAnalysisResult(object):
    def __init__(self, dslist=None):
        if dslist is not None:
            self._dslist = dslist
        else:
            self._dslist = DatasetList()

    @property
    def dataset(self):
        return self._dslist

    def to_ndarray(self):
        return self._dslist.to_ndarray()

    def to_dict(self):
        return self._dslist.to_dict()

    def grep(self, key):
        return self._dslist.grep(key)

    def __getitem__(self, idx):
        return self.__class__(self._dslist[idx])

    def __iter__(self):
        return self._dslist.__iter__()

    def groupby(self, key):
        return _groupby(self, key)

    def append(self, value):
        self._dslist.append(value)

    @property
    def values(self):
        return self._dslist.values
