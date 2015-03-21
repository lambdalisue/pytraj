# distutils: language = c++
from cpython.array cimport array as pyarray
from pytraj.cpptraj_dict import MatrixDict, MatrixKindDict, get_key

cdef class DataSet_MatrixDbl (DataSet_2D):
    def __cinit__(self):
        self.thisptr = new _DataSet_MatrixDbl()
        self.baseptr_1 = <_DataSet_2D*> self.thisptr
        self.baseptr0 = <_DataSet*> self.thisptr

    def __dealloc__(self):
        if self.py_free_mem:
            del self.thisptr

    def __getitem__(self, int idx):
        if idx >= self.size:
            raise IndexError("out of index")
        return self.thisptr.index_opr(idx)

    def alloc(self):
        cdef DataSet dset = DataSet()
        dset.baseptr0 = _DataSet_MatrixDbl.Alloc()
        return dset

    @property
    def mtype(self):
        return get_key(self.thisptr.matType(), MatrixDict)

    @property
    def n_snapshots(self):
        return self.thisptr.Nsnapshots()

    def element(self, size_t x, size_t y):
        return self.thisptr.Element(x, y)

    def add_element(self, double d):
        return self.thisptr.AddElement(d)

    def set_element(self,size_t x, size_t y, double d):
        self.thisptr.SetElement(x, y, d)

    def vect(self):
        return self.thisptr.Vect()

    def allocate_vector(self,size_t vsize):
        self.thisptr.AllocateVector(vsize)

    def store_mass(self, Darray mIn):
        self.thisptr.StoreMass(mIn)

    @property
    def mass(self):
        return self.thisptr.Mass()

    def get_full_matrix(self):
        """return python array with length = n_rows*n_cols"""
        cdef int nr = self.n_rows
        cdef int nc = self.n_cols 
        cdef int i, j
        cdef pyarray arr0 = pyarray('d', [])

        for i in range(nr):
            for j in range(nc):
                arr0.append(self.baseptr_1.GetElement(i, j))
        return arr0
