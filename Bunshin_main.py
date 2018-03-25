
import Environment.Environment as env
import time


class Bunshin_main:
    def __init__(self,bunshin_name,bunshin_type,God_brain):
        self.environment = env(bunshin_name=bunshin_name,bunshin_type=bunshin_type,God_brain=God_brain)
        self.bunshin_type = bunshin_type

    def go(self,is_done):
        while True:
            if not is_done and self.bunshin_type == 'learning':
                self.environment.run()
            if is_done and self.bunshin_type == 'learning':
                time.sleep(1)