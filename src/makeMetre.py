#!python3.6
#coding:utf-8
import time
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
import MusicTheory.EqualTemperament
import MusicTheory.Scale
import MusicTheory.tempo
import pathlib

def make_metre():
    wm = Wave.BaseWaveMaker.BaseWaveMaker()
    sampler = Wave.Sampler.Sampler()

    et = MusicTheory.EqualTemperament.EqualTemperament()
    scale = MusicTheory.Scale.Scale()
    timebase = MusicTheory.tempo.TimeBase()
    timebase.BPM = 120
    timebase.Metre=(4,4)
    nv = MusicTheory.tempo.NoteValue(timebase)
    wf = Wave.WaveFile.WaveFile()
    wf.BasePath = pathlib.PurePath('../res/metres/')

    p = Wave.Player.Player()
    p.Open()
    scale.Major(key='C')
    print(f'BPM={timebase.BPM} キー={scale.Key} 音階={scale.Scales}')
    
    print('========== 単純拍子 ==========')
    timebase.Metre=(2,2)
    print(f'拍子={timebase.Metre} 強弱')
    wav = []
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
    wf.Write(b''.join(wav), filename='2-2(Sw)')

    timebase.Metre=(2,2)
    print(f'拍子={timebase.Metre} 弱強')
    wav = []
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
    wf.Write(b''.join(wav), filename='2-2(wS)')

    timebase.Metre=(2,4)
    print(f'拍子={timebase.Metre} 強強弱弱')
    wav = []
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
    wf.Write(b''.join(wav), filename='2-4(Sw)')

    timebase.Metre=(2,4)
    print(f'拍子={timebase.Metre} 弱弱強強')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
    wf.Write(b''.join(wav), filename='2-4(wS)')

    timebase.Metre=(3,4)
    print(f'拍子={timebase.Metre}')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        # 4/4拍子だと以下のように3連符で表さねばならない(楽譜が複雑になる。それを解決するために拍子を設定する)
#        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(1, let=3))))
#        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(1, let=3))))
#        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(1, let=3))))
    wf.Write(b''.join(wav), filename='3-4(Sww)')

    timebase.Metre=(3,2)
    print(f'拍子={timebase.Metre}')
    wav = []
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(2))))
    wf.Write(b''.join(wav), filename='3-2(Sww)')

    timebase.Metre=(3,8)
    print(f'拍子={timebase.Metre}')
    wav = []
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
    wf.Write(b''.join(wav), filename='3-8(Sww)')

    timebase.Metre=(4,4)
    print(f'拍子={timebase.Metre} 強弱中弱')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='4-4(SwMw)')

    timebase.Metre=(4,4)
    print(f'拍子={timebase.Metre} 強弱弱弱')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='4-4(Swww)')

    print('========== 複合拍子 ==========')
    # 2拍子の発展
    # 6/8拍子 2拍子で各拍が3連符
    print('拍子=6/8')
    timebase.Metre=(6,8)
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
    wf.Write(b''.join(wav), filename='6-8(SwwMww)')

    # 6/4拍子 2拍子で各拍が3連符
    print('拍子=6/4')
#    timebase.Metre=(4,4)
    timebase.Metre=(6,4)
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='6-4(SwwMww)')

    # 3拍子の発展
    # 9/8拍子
    print('拍子=9/8')
    timebase.Metre=(9,8)
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
    wf.Write(b''.join(wav), filename='9-8(SwwMwwMww)')
    
    # 4拍子の発展
    # 12/8拍子
    timebase.Metre=(12,8)
    print(f'12/8拍子 強弱中弱')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.75, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
    wf.Write(b''.join(wav), filename='12-8(SwwmwwMwwmww)')

    timebase.Metre=(12,8)
    print(f'12/8拍子 強弱弱弱')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(8))))
    wf.Write(b''.join(wav), filename='12-8(Swwmwwmwwmww)')

    print('========== 変拍子 ==========')
    timebase.Metre=(5,4)
    print(f'5拍子 3拍子+2拍子  (3+2)/4  2拍子の中に3拍子と2拍子がある')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='5-4(SwwMw)')

    print(f'5拍子 2拍子+3拍子  (2+3)/4')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.7, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='5-4(SwMww)')

    print(f'純5拍子？ 強弱弱弱弱  5/4')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='5-4(Swwww)')

    print(f'7拍子 7/4  強弱弱弱弱弱弱')
    timebase.Metre=(4,4)
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.4, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='7-4(Swwwwww)')

    print(f'7拍子 (4+3)/4  2拍子の中に4,3拍子がある。')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.8, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='7-4(SwwwMww)')

    print(f'7拍子 (3+4)/4  2拍子の中に3,4拍子がある。')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.8, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.5, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='7-4(SwwMwww)')

    print(f'7拍子 (3+2+2)/4  3拍子の中に2,2,3拍子がある。')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.8, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.8, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='7-4(SwwMwMw)')

    print(f'7拍子 (2+2+3)/4  3拍子の中に2,2,3拍子がある。')
    wav.clear()
    for bar in range(4):
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.8, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.8, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
        wav.append(sampler.Sampling(wm.Sin(a=0.3, fs=8000, f0=scale.Frequencies[0]*2, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename='7-4(SwMwMww)')

    p.Close()


if __name__ == "__main__" :
    make_metre()
