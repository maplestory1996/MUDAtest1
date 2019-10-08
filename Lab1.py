import muda
import jams
import six


noise_file = ['background_noise/150993__saphe__street-scene-1.wav',
              'background_noise/173955__saphe__street-scene-3.wav',
              'background_noise/207208__jormarp__high-street-of-gandia-valencia-spain.wav',
              'background_noise/268903__yonts__city-park-tel-aviv-israel.wav']
TS_param = [0.81, 0.93, 1.07, 1.23]
PS1_param = [-2, -1, 1, 2]
PS2_param = [-3.5, -2.5, 2.5, 3.5]
BG_Range = [0.1, 0.5]
JAMs = '7061-6-0-0.jams'
wavpath = '7061-6-0-0.wav'
j_orig = muda.load_jam_audio(JAMs, wavpath)
X = []
# 对比图
# for i in range(len(TS_param)):
#     TS = muda.deformers.TimeStretch(rate=TS_param[i])
#     out_jams = list(TS.transform(j_orig))
#     audio = out_jams[0].sandbox.muda._audio['y']
#     X.append(audio)
# for i in range(len(PS1_param)):
#     PS1 = muda.deformers.PitchShift(n_semitones=PS1_param[i])
#     out_jams = list(PS1.transform(j_orig))
#     audio = out_jams[0].sandbox.muda._audio['y']
#     X.append(audio)
# for i in range(len(PS2_param)):
#     PS2 = muda.deformers.PitchShift(n_semitones=PS2_param[i])
#     out_jams = list(PS2.transform(j_orig))
#     audio = out_jams[0].sandbox.muda._audio['y']
#     X.append(audio)
# for i in range(len(PS2_param)):
#     BG = muda.deformers.BackgroundNoise(n_samples=1, files=noise_file[i],
#                                         weight_min=BG_Range[0], weight_max=BG_Range[1])
#     out_jams = list(PS2.transform(j_orig))
#     audio = out_jams[0].sandbox.muda._audio['y']
#     X.append(audio)

drc = muda.deformers.DynamicRangeCompression(preset=['music standard', 'film standard',
                                                     'speech', 'radio'])

out_jams = list(drc.transform(j_orig))
print(drc)
list(A)
# A = drc.audio()
print(A)
