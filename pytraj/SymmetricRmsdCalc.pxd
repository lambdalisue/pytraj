# distutils: language = c++
from libcpp.vector cimport vector
from pytraj.Topology cimport _Topology, Topology
from pytraj.Hungarian cimport *
from pytraj.AtomMap cimport _AtomMap, AtomMap
from pytraj.AtomMask cimport _AtomMask, AtomMask
from pytraj.Frame cimport _Frame, Frame
from pytraj.Matrix_3x3 cimport _Matrix_3x3, Matrix_3x3
from pytraj.Vec3 cimport _Vec3, Vec3


cdef extern from "SymmetricRmsdCalc.h": 
    ctypedef vector[int] Iarray
    cdef cppclass _SymmetricRmsdCalc "SymmetricRmsdCalc":
        _SymmetricRmsdCalc() 
        _SymmetricRmsdCalc(const _AtomMask&, bint, bint, const _Topology&, int)
        int InitSymmRMSD(bint, bint, int)
        int SetupSymmRMSD(const _Topology&, const _AtomMask&, bint)
        double SymmRMSD(const _Frame&, _Frame&)
        double SymmRMSD_CenteredRef(const _Frame&, const _Frame&)
        bint Fit() const 
        bint UseMass() const 
        const _Matrix_3x3& RotMatrix() const 
        const _Vec3& TgtTrans() const 
        const Iarray& AMap() const 