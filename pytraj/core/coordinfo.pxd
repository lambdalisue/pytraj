# distutils: language = c++
from ..core.box cimport _Box


cdef extern from "CoordinateInfo.h": 
    cdef cppclass CoordinateInfo:
        CoordinateInfo() 
        CoordinateInfo(const _Box& b, bint v, bint t, bint m)
        #CoordinateInfo(const _ReplicaDimArray& r, const _Box& b, bint v, bint t, bint m, bint f)
        #CoordinateInfo(int e, const _ReplicaDimArray& r, const _Box& b, bint v, bint t, bint m, bint f)
        bint HasBox() const 
        const _Box& TrajBox() const 
        int EnsembleSize() const 
        bint HasVel()
        bint HasTemp()
        bint HasTime()
        bint HasForce()
        bint HasReplicaDims()
        #const _ReplicaDimArray& Replica_Dimensions() const 
        void SetTime(bint m)
        void SetTemperature(bint t)
        void SetVelocity(bint v)
        void SetEnsembleSize(int s)
        void SetBox(const _Box& b)
