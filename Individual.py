import random
import numpy as np

# 定数の定義
GEN_MAX = 1000  # 世代交代数
POP_SIZE = 1000  # 個体群のサイズ
ELITE = 1  # エリート保存戦略で残す個体の数
MUTATE_PROB = 0.01  # 突然変異確率
N = 64  # 集合の要素となる最大数の平方根
TOURNAMENT_SIZE = 30  # トーナメントサイズ

# 0以上1未満の実数乱数
RAND_01 = random.random()

class Individual:
    #コンストラクタ(クラスが呼び出されると実行される)
    def __init__(self):
        self.chrom = [] #染色体の配列
        for i in range(0,N):
            #0以上1以下の整数を生成
            x = random.randint(0,1)
            #生成した整数を染色体の配列に追加
            self.chrom.append(x)

#適応度を算出
def evaluate():
    fitness = 0.0
    # σ[i=1,N-1]{(chrom[i]*2-1)*(i-1)^1/2}
    for i in range(0,N):
        fitness += (Individual.chrom[i] * 2 - 1) * np.sqrt(float(i) + 1)
    fitness = np.abs(fitness)

#p1とp2から一点交叉で作った子にする
def crossover1(self):
    p1 = Individual() #親個体1
    p2 = Individual() #親個体2
    chrom = [] #子

    #0以上N-1以下の乱数を交叉点にする
    point = random.randint(0,N-1)
    #一点交叉をする
    for i in range(0,point):
        chrom[i] = p1.chrom[i]
    for i in range(point,N):
        chrom[i] = p2.chrom[i]
    

