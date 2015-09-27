from __future__ import print_function
import unittest
import numpy as np
import pytraj as pt
from pytraj.utils import eq, aa_eq
from pytraj.testing import cpptraj_test_dir


class Test(unittest.TestCase):
    def test_0(self):
        traj = pt.iterload("./data/tz2.nc", "./data/tz2.parm7")
        iter_options = {'start': 9, 'stop': 30, 'stride': 2}
        #print(traj(**iter_options))

        bfactors = pt.calc_bfactors(traj(**iter_options))
        s_fname = "/".join((cpptraj_test_dir, "Test_AtomicFluct",
                            "fluct.4.dat.save"))
        saved_bfactors = np.loadtxt(s_fname).T[1]

        aa_eq(saved_bfactors, bfactors.T[1])

        b2 = pt.calc_bfactors(traj(**iter_options), dtype='dataset')
        assert b2[0].key == 'B-factors'


if __name__ == "__main__":
    unittest.main()