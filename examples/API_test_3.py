
import numpy as np
from pytraj.base import *
from pytraj.actions.Action_Strip import Action_Strip
from pytraj.actions.Action_Distance import Action_Distance
from test_API.TestAPI2 import create_state, do_calculation

state = CpptrajState()
state.toplist.add_parm("../tests/data/Tc5b.top")
state.add_trajin("../tests/data/md1_prod.Tc5b.x")
#state.add_trajout("./out.x")
state.add_trajout("./out.x netcdf")
state.set_no_progress()
#output = do_calculation(action=Action_Strip(), command="strip !@CA", state=state)
TRAJ = TrajReadOnly(filename="../tests/data/md1_prod.Tc5b.x", top="../tests/data/Tc5b.top")
trajinlist = state.get_trajinlist()
print(dir(trajinlist))
#trajinlist.add_traj(TRAJ.alloc())
trajin = trajinlist.front()
trajinlist[0] = TrajReadOnly(filename="../tests/data/md1_prod.Tc5b.x", top="../tests/data/Tc5b.top")
print(trajinlist[0].size)