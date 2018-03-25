

import Bunshin_brain as bb
import global_share as gs
import numpy as np

e_greedy_start = 0.5
e_greedy_end = 0.0
e_greedy_threshold = 10000

class Bunshin_action:
    def __init__(self,bunshin_name,God_brain):
        self.brain = bb.Bunshin_brain(bunshin_name=bunshin_name,God_brain=God_brain)

        self.short_memory = []
        self.accumulated_reward = 0

    def act(self,s):
        if gs.sum_trial_num > e_greedy_threshold:
            e_greedy_probability = e_greedy_end
        else:
            e_greedy_probability = e_greedy_start + gs.sum_trial_num * (e_greedy_end-e_greedy_start) / e_greedy_threshold

        if random.random() < e_greedy_probability:
            return random.randinit(0,gs.num_action-1)
        else:
            s = np.array([s])
            p = self.brain.predict_action_probability(s)
            a = np.random.choice(gs.num_action,p=p[0])
            return a

    def advantage_push_bunshin_brain(self,s,a,r,s_next):








