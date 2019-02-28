from pyAudioAnalysis import audioTrainTest as aT
import os
from pathlib import Path


class EmotionsDetector:

    def train(self, audio_files_path, output_path, model_name):

        afp = Path(audio_files_path)
        op = Path(output_path)
        model = str(op / model_name)

        if not os.path.exists(afp):
            print('The audio files path does not exist')
            return

        if not os.path.exists(op):
            os.mkdir(op)
            return

        return aT.featureAndTrainRegression(audio_files_path, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm",
                                            model, True)

    def get_emotions(self, audio_file_path, model_path, model_name):

        afp = Path(audio_file_path)
        model = Path(model_path) / model_name

        if not os.path.exists(Path(model_path)):
            print('Model folder does not exist')
            return

        if not os.path.exists(afp):
            print('File does not exist')
            return

        return aT.fileRegression(str(afp), str(model), 'svm')
