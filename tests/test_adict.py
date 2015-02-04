from __future__ import print_function
import unittest
from pytraj.base import *
from pytraj import io as mdio
from pytraj.utils.check_and_assert import assert_almost_equal

class Test(unittest.TestCase):
    def test_0(self):
        traj = mdio.load("./data/md1_prod.Tc5b.x", "./data/Tc5b.top")
        from pytraj import adict

        for key in sorted(adict.keys()):
            print (key)

        act = adict['diffusion']()
        act.help()
        print (act)

if __name__ == "__main__":
    unittest.main()