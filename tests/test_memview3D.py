import unittest
from pytraj.base import *
from pytraj import io as mdio
from pytraj.utils.check_and_assert import assert_almost_equal
import numpy as np


class Test(unittest.TestCase):

    def test_0(self):
        traj = mdio.iterload("./data/Tc5b.x", "./data/Tc5b.top")[:]
        arr0 = traj[:, :, :]
        arr0[0, 0, 0] = 105.


if __name__ == "__main__":
    unittest.main()
