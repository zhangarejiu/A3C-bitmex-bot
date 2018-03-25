import gym
import numpy as np
import global_share as gs

NUM_SYNCHRONIZE_STEP = 10
NUM_SYNCHRONIZE_WITH_GOD = 10
import Bunshin_action as ba

is_done = False

class Environment:

    total_reward = np.zeros(NUM_SYNCHRONIZE_STEP)
    bunshin_trial_counter = 0

    def __init__(self,bunshin_name,bunshin_type,God_brain):
       self.name = bunshin_name
       self.bunshin_type = bunshin_type
       self.env = gym.make('CartPole-v0')
       self.bunshin = ba.Bunshin_action(bunshin_name=bunshin_name,God_brain=God_brain)

    def go(self):
        self.bunshin.brain.pull_God_brain()

        s = self.env.reset()
        accumulated_reward = 0
        step = 0

        while True:
            a = self.bunshin.act(s)
            s_next,r,done,info = self.env.step(a)
            step +=1
            gs.sum_trial_num +=1

            reward = 0
            if done == True:
                s_ = None
                if step < 199:
                    r = -1
                else:
                    r = 1

            self.bunshin.advantage_push_bunshin_brain(s,a,r,s_next)

        s = s_next
        accumulated_reward += r

        #ワンゲームが終わったら
        if done == True or step % NUM_SYNCHRONIZE_WITH_GOD ==0:
            if not gs.is_done and self.bunshin_type == 'learning':
                self.bunshin.brain.update_God_brain()
                self.bunshin.brain.pull_God_brain()

        if done == True:
            self.total_reward = np.hstack((self.total_reward[1:],step))
            self.bunshin_trial_counter += 1
            break

        print("分身体:" + self.name + " 試行回数:" + str(self.bunshin_trial_counter)))
        print("今回のステップ数:" + str(step) + " 平均ステップ数:" + str(self.total_reward_.mean())


        #満足のいく数値が観測されたら、親のパラメーターに反映する
        if self.total_reward.mean() > 199:
            gs.is_done = True
            time.sleep(2.0)
            self.bunshin.brain.push_God_brain()













