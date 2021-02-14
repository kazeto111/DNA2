#全てのタンデムリピートを返すとあまりに多すぎるためk>=2のタンデムリピートのみを列挙することにしました
from collections import OrderedDict
def readFasta_dict(InfileNameFN): #この関数はhttp://www.fish-evol.org/pythonJI.htmlを参考にしました
    Infile = open(InfileNameFN, "r")
    seqDictFN  = OrderedDict()
    for Line in Infile:
        Line = Line.rstrip("\n")
        if Line[0] == ">":
            Name            = Line
            seqDictFN[Name] = ""
        else:
            seqDictFN[Name] += Line
    Infile.close()
    return seqDictFN


def tandem(i, k, j, s): #配列sのインデックスiからi+jまでによるユニットがインデックスkから繰り返されているかを判定する関数
    for l in range(j+1):
        if k + l >= len(s):
            return False
        if s[i+l] != s[k+l]:
            return False
    return True
path = "/Users/futo/Downloads/tandem_repeats.fasta"
seqDict = readFasta_dict(path)
a = int(input()) # 入力した番号の配列を読み込みようにしました
for name, seq in seqDict.items():
    if name == ">" + str(a):
        s = list(seq) #1文字ごとのリストにする
unit_list = [] #ユニットを記録するリスト
num_list = [] #出現回数を記録するリスト
size = len(s)
flag = [[0] * size for i in range(size)]#すでにカウントされているタンデムリピートの二つ目以降のユニットの先頭をflag[i][j]=1で記録
for i in range (size):
    for j in range ((size-i)//2):
        k = i + j + 1
        while tandem(i, k, j, s):
            k += j + 1
        num = (k-i) // (j+1) #ユニットの繰り返し回数
        if num >= 2 and flag[i][j] != 1:
            unit = str(s[i])
            for l in range(1,j+1):
                unit += str(s[i+l])
            unit_list.append(unit)
            num_list.append(num)
            for m in range (num):
                flag[i + m * (j+1)][j] = 1
print("ユニット", "出現回数")
for i in range(len(unit_list)):
    print(unit_list[i], num_list[i])



