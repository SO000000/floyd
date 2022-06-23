import random
import numpy as np

# 定数の定義
GEN_MAX = 1000  # 世代交代数
POP_SIZE = 1000  # 個体群のサイズ
ELITE = 1  # エリート保存戦略で残す個体の数
MUTATE_PROB = 0.01  # 突然変異確率
N = 64  # 集合の要素となる最大数の平方根
TOURNAMENT_SIZE = 30  # トーナメントサイズ

# 0以上1未満の実数Ï乱数
RAND_01 = random.random()

class Individual:
    #コンストラクタ
    def __init__(self):
        chrom = [] #染色体
        for i in range(0,N):
            chrom[i] = random.randint(0,1)
        fitness = 0.0 #適応度
