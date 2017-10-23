import math
#import MusicTheory.Key
#https://ja.wikipedia.org/wiki/%E5%B9%B3%E5%9D%87%E5%BE%8B
#平均律
#1オクターブを指定数で等分した音律。
#12平均律が西洋音楽の基礎である。
#全部で3,4,5,6,7,12,15,17,19,22,24,31,34,41,53,72がある。
class EqualTemperament:
    Denominator = 12
    # 音名,key,note,pitch
    """
    1オクターブ上にあるKey値とオクターブ増減値を返す。: tuple(key,octave)
    例えば1オクターブ12音なら、0〜11の値を返す。超過した分はoctave増減値にする。
    引数valueは整数値。
    引数|返却
    ----|----
    value=-1|(11, -1)
    value=0|(0, 0)
    value=1|(1, 0)
    value=11|(11, 0)
    value=12|(0, 1)
    """
    @classmethod
    def Cycle(cls, value): return ((value % cls.Denominator), (value // cls.Denominator))


if __name__ == '__main__':
    # 12平均律
    EqualTemperament.Denominator = 12
    print('EqualTemperament.Denominator:', EqualTemperament.Denominator)
    for v in range((EqualTemperament.Denominator*3*-1), (EqualTemperament.Denominator*3+1)):
        print(v, EqualTemperament.Cycle(key))
    
    # 53平均律
    print()
    EqualTemperament.Denominator = 53
    print('EqualTemperament.Denominator:', EqualTemperament.Denominator)
    for v in range((EqualTemperament.Denominator*3*-1), (EqualTemperament.Denominator*3+1)):
        print(v, EqualTemperament.Cycle(key))
