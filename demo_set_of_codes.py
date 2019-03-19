import numpy as np
import matplotlib.pyplot as plt
import librosa
import sounddevice as sd
import os


# fig, ax = plt.subplots()
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)


all_weights=np.load('set_of_will_samples/all_weights.npy')
n_emo=all_weights.shape[1]

emo_cat = ['WILL_BAD',  'WILL_HAPPY',  'WILL_LOUD',  'WILL_NEUTRAL',  'WILL_OLD',  'WILL_PROXI',  'WILL_SAD']
neu_cat=3
# pca_result=np.load('random_will_samples/pca_result.npy')



def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

    angle=event.xdata
    r=event.ydata
    some_pt = np.array([event.xdata, event.ydata])
    print(some_pt)

    # choose the category: line closest to the angle detected
    cat=int(round(angle/(2*np.pi)*(n_emo-1)))
    if cat>=neu_cat: cat=cat+1
    cat=np.mod(cat,n_emo)
    print(cat)

    # select the lines of weights corresponding to that category
    lines=np.where(all_weights[:, cat] > 0)[0]
    print(lines)
    print(all_weights[lines,:])

    # intensity of the category defined by r
    idx=find_nearest(all_weights[lines,cat], r)
    print(lines[idx])
    print(all_weights[lines[idx]])

    # load and play
    y, fs = librosa.load(os.path.join('set_of_will_samples', str(lines[idx])+".wav"))
    sd.play(y,fs)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

angles=2*np.pi/(n_emo-1)*np.arange(n_emo-1)

for i,a in enumerate(angles):
    x1, y1 = [0, a], [0, 1]
    if i >= neu_cat: i = i + 1
    line,=ax.plot(x1, y1, marker = 'o', label=emo_cat[i])
    # line.set_label('Label via method')
    ax.legend()

plt.show()

