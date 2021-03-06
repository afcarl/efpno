from contracts import contract
import numpy as np
from ..math.utils import pose_diff
from geometry import SE2

@contract(target_pose='SE2')
def graph_fix_node(G, x, target_pose):
    assert G.has_node(x)
    
    q = G.node[x]['pose']
    diff = np.dot(target_pose, np.linalg.inv(q)) 
    
    for n in G.nodes():
        q = G.node[n]['pose']
        q2 = np.dot(diff, q)
        G.node[n]['pose'] = q2
                
    SE2.assert_close(G.node[x]['pose'], target_pose)
