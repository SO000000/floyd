import Individual
import gc


class Population:

    # コンストラクタ
    def __init__(self):

        self.ind = []  # 現世代個体群
        self.nextind = []  # 次世代個体群

        for i in range(0, Individual.POP_SIZE):

            # 現世代個体群を生成
            self.x = Individual.Individual()
            self.ind.append(self.x.chrom)

            # 次世代個体群を生成
            self.y = Individual.Individual()
            self.nextind.append(self.y.chrom)

    # デストラクタ
    def __del__(ind, nextind):

        for i in range(0, Individual.POP_SIZE):
            del ind[i]
            del nextind[i]
        # メモリを解放
        gc.collect()

    #全ての個体を評価して，適応度順に並び変える
    def evaluete(self):
        for i in range(0, Individual.POP_SIZE):
            self.ind[i].fitness = Individual.evaluate(self.ind[i])
        Population.sort(0, Individual.POP_SIZE - 1)

    # ind[lb]~ind[ub]をクイックソートで並び替える
    # lb: 並びかえの対象要素の添字の下限
    # ub: 並びかえの対象要素の添字の上限
    def sort(ind,lb,ub):
        if (lb + ub) / 2:
            k = (lb + ub) / 2
            pivot = ind[k].fitness
            i = lb
            j = ub
        while True:
            while ind[i].fitness < pivot:
                i += 1
            while ind[j].fitness > pivot:
                j -= 1
            if i <= j:
                ind[i],ind[j] = ind[j],ind[i]
                i += 1
                j += 1
            if i <= j:
                break

    # 世代交代をする
    def alternate(self):
        for i in range(Individual.ELITE):
            for j in range(Individual.N):
                Individual.nextInd[i].chrom[j] = Individual.ind[i].chrom[j]

        for i in range(Individual.POP_SIZE):
            p1 = Population.rankingSelect1()
            p2 = Population.rankingSelect2()

        for i in range(Individual.POP_SIZE):
            Individual.nextInd[i] = Individual.mutate()

        Individual.ind,Individual.nextInd = Individual.nextInd,Individual.ind

        Population.evaluete()