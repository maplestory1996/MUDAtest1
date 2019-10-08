def feature_extract_save(root_folder, feature):
    with open(root_folder + '/metadata/UrbanSound8K.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        target_dicts = {}
        for row in readCSV:
            file_name = row[0]
            class_id = row[6]
            target_dicts[file_name] = class_id
    for i in range(1, 11):
        fold_path = root_folder + '/audio/fold{}/'.format(i)
        # audio_names = glob.glob(fold + '*.wav')
        audio_names = [n for n in os.listdir(fold_path) if re.match(r'.*.wav', n)]
        X_f = [] # list for saving the features of all the sound files
        y = []   # list for saving the corresponding labels
        for audio_name in audio_names:
            x, sr = librosa.load(fold_path + audio_name, sr=44100)
            print(len(x), sr)
            if len(x) < clip_len:
                left_nums = np.random.randint(0, clip_len - len(x) + 1)
                # zero-padding
                x = np.concatenate((np.zeros(left_nums), x, np.zeros(clip_len - len(x) - left_nums)))
            else:
                x = x[:clip_len]
            # DA - 4
            x
            # FE
            if feature == 'mfb':
                X_f.append(librosa.feature.melspectrogram(x, sr, n_fft=1024, hop_length=1024, n_mels=128, fmin=0, fmax=22050))
            if feature == 'mfcc':
                X_f.append(librosa.feature.mfcc(x, sr, n_fft=1024, hop_length=1024, n_mels=128, fmin=0, fmax=22050))
            y.append(target_dicts[audio_name])
        np.savez_compressed(root_folder+'/features/fold{}/'.format(i)+feature, X_f=np.asarray(X_f), y=np.asarray(list(map(int, y))))
    print("Features have been successfully saved!")
