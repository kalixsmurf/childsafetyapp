import joblib
import numpy as np
import os
from python_speech_features import mfcc
import librosa

model = joblib.load("emotion_model.joblib")

def extract_feature(file_name, mfcc=True):
    try:
        # Load the audio file
        X, sample_rate = librosa.load(os.path.join(file_name), res_type='kaiser_fast')

        # Initialize result with MFCC features if enabled
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs)) if result.size else mfccs  # Initialize or stack

        return result
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")
        return None

# Main function to process the audio file and return the prediction
def main(jsonData):
    # Extract the path from JSON data
    file_path = jsonData.get("path")
    if not file_path or not os.path.exists(file_path):
        raise FileNotFoundError("The specified file path does not exist or is invalid.")

    # Extract features from the audio file
    feature = extract_feature(file_path) #Default True, so didn't provide the flag
    
    if feature is not None:
        # Ensure the feature is 2D for model prediction
        feature_2d = np.array([feature])  # Convert to 2D array

        # Make a prediction
        predictions = model.predict(feature_2d)
        return predictions[0]
    else:
        raise ValueError("Failed to extract features from the audio file.")
