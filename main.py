
import time
import numpy as np
import os
import threading


import tensor as tf
from keras.utils import plot_model
from keras import backend as K

import God_brain as gb
import Bunshin_main as bm


NUM_STATES = 4
NUM_ACTIONS = 2
NONE_STATE = np.zeros(NUM_STATES)
NUM_BUNSHIN = 3


# python - Using global variables between files? - Stack Overflow
# https://stackoverflow.com/questions/13034496/using-global-variables-between-files


def main():
    print("set God brain")
    God_brain = gb.God_brain()
    bunshin_case = []

    for i in range(NUM_BUNSHIN):
        bunshin_name = "bunshin%d" % i
        bunshin_case.append(bm.Bunshin_main(bunshin_name=bunshin_name,bunshin_type="learning",God_brain=God_brain))

    for i,bunshin in enumerate(bunshin_case):
        job = lambda: bunshin.run
        t = threading.Thread(target=job)
        print("bunshin{} created".format(i))
        t.start()



if __name__ == '__main__':
    main()








