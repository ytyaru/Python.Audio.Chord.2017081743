import MusicTheory.EqualTemperament
import MusicTheory.scales.MajorScales
import MusicTheory.Scale
#import MusicTheory.tempo.TimeBase #ModuleNotFoundError: No module named 'MusicTheory.tempo.TimeBase'; 'MusicTheory.tempo' is not a package
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
import pathlib

et = MusicTheory.EqualTemperament.EqualTemperament()
scale = MusicTheory.Scale.Scale()
scale.Scale = MusicTheory.scales.MajorScales.MajorScales()
#print(scale.Scales)
for keyId in range(len(et.Ids)):
    scale.KeyId = keyId
    print(keyId, scale.Scales, et.Names[keyId], [et.Names[k] for k in scale.Scales])
    #スケールを表す楽譜に「調号」というのがある。ト音記号のすぐ後ろに`♯`や`♭`をいくつか配置して、キー(Key,調)が何であるか示す記法である。
    #この調号に従って、その調におけるスケールの構成音も`♯`や`♭`を付けることができる。どちらの表記にするか迷うことはない。
    #調号とその構成音における`♯`,`♭`付与ルールは、五度圏表によって作ることができる。
    #ただ、五度圏表の実装が面倒なので、とりいそぎ絶対値と#統一の表示だけとする。

#
#
#
wm = Wave.BaseWaveMaker.BaseWaveMaker()
sampler = Wave.Sampler.Sampler()

#timebase = MusicTheory.tempo.TimeBase()
#timebase.BPM = 120
#timebase.Metre=(4,4)
#nv = MusicTheory.tempo.NoteValue(timebase)
wf = Wave.WaveFile.WaveFile()
wf.BasePath = pathlib.PurePath('../res/scales/Major/')

wav = []
for keyId in range(len(et.Ids)):
    scale.KeyId = keyId
#    print(keyId, scale.Scales, et.Names[keyId], [et.Names[k] for k in scale.Scales])
    wav.clear()
    for f0 in scale.Frequencies:
        print('f0:', f0)
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.25)))
#        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
    wf.Write(b''.join(wav), filename=et.Names[keyId].replace('#','+')+'MajorScale')

