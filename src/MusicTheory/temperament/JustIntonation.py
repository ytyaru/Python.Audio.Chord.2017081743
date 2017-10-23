#!python3.6
#coding:utf-8
#https://ja.wikipedia.org/wiki/%E7%B4%94%E6%AD%A3%E5%BE%8B
#http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/Genre/Tuning/tuning_just.html
#純正律(算出方法はメジャースケールの場合である)
class JustIntonation:
    def __init__(self):
        self.__DENOMINATOR = 7
        self.__BaseFrequency = 440 #基準となる音をA4(ラ)とし、周波数を440として算出する
        self.__Frequencies = [] #C,D,E,F,G,A,Bの7音の周波数
        self.__Rate = [1, 9/8, 5/4, 4/3, 3/2, 5/3, 15/8] #メジャースケールにおける7音の比率
        self.__calcFrequencies()
    @property
    def BaseFrequency(self): return self.__BaseFrequency
    @BaseFrequency.setter
    def BaseFrequency(self, v):
        if 0 < v:
            self.__BaseFrequency = v
            self.__calcFrequencies()
    @property
    def Frequencies(self): return self.__Frequencies
    def __calcFrequencies(self):
        self.Frequencies.clear()
        for rate in self.__Rate: self.Frequencies.append(self.__BaseFrequency * rate)

if __name__ == '__main__':
    ji = JustIntonation()
    print(ji.Frequencies)
    print('---------- 1オクターブ下 ----------')
    print([f/2 for f in ji.Frequencies])
    print('---------- 1オクターブ上 ----------')
    print([f*2 for f in ji.Frequencies])

