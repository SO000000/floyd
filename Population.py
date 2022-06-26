import Individual
import gc

class Population:
    
    #コンストラクタ
    def __init__(self):
        self.ind = []
        self.nextind = []
        for i in range(0,Individual.POP_SIZE):
            self.ind[i] = Individual()
            self.nextind[i] = Individual()

    #デストラクタ
    def __del__(self):

        self.ind = ind
        self.nextind = nextind

        for i in range(0,Individual.POP_SIZE):
            del self.ind[i]
            del self.nextind[i]
        #メモリを解放
        gc.collect()
