import Individual
import gc


class Population:

    # コンストラクタ
    def __init__(self):

        self.ind = []       #現世代個体群
        self.nextind = []   #次世代個体群

        for i in range(0, Individual.POP_SIZE):

            #現世代個体群を生成
            self.x = Individual.Individual()
            self.ind.append(self.x.chrom)

            #次世代個体群を生成
            self.y = Individual.Individual()
            self.nextind.append(self.y.chrom)

    # デストラクタ
    def __del__(ind,nextind):

        for i in range(0, Individual.POP_SIZE):
            del ind[i]
            del nextind[i]
        # メモリを解放
        gc.collect()