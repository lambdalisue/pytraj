from __future__ import absolute_import, print_function
import os

from .decorators import test_if_having, no_test, local_test
from .data_sample.load_sample_data import load_sample_data
from .utils import eq, aa_eq
from .utils.check_and_assert import is_linux
from .utils import duplicate_traj
from .Topology import Topology

try:
    amberhome = os.environ['AMBERHOME']
    cpptraj_test_dir = os.path.join(amberhome, 'AmberTools', 'test', 'cpptraj')
except:
    amberhome = None
    cpptraj_test_dir = None

possible_path = "../cpptraj/test/"
if os.path.exists(possible_path):
    cpptraj_test_dir = possible_path

def make_fake_traj(n_frames=100, n_atoms=10000):
    import numpy as np
    from pytraj.core import Atom
    from pytraj import Trajectory

    pseudotop = Topology()
    pseudotop.start_new_mol()
    for i in range(n_atoms):
        aname, atype = "X", "X"
        charge, mass = 0.0, 1.0
        atom = Atom(aname, atype, charge, mass)
        resid = 1
        resname = "XXX"
        pseudotop.add_atom(atom=atom, resid=resid, resname=resname)
    traj = Trajectory(top=pseudotop)
    traj._allocate(n_frames, n_atoms)
    traj.update_xyz(np.random.rand(n_frames, n_atoms, 3))
    return traj

if __name__ == "__main__":
    print (amberhome)
    print (cpptraj_test_dir)
