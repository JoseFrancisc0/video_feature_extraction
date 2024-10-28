import sys
import os

vf_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/josew/Desktop/Video_Extraction_test/video_features')) # Put library dir
sys.path.append(vf_root)

from video_features.models.r21d.extract_r21d import ExtractR21D
from multiprocessing import Pool
from omegaconf import OmegaConf
import numpy as np
import csv

def process_video(video_path, model_name, config_path):
    try:
        args = OmegaConf.load(config_path)
        args.model_name = model_name

        extractor = ExtractR21D(args)
        extractor.device = 'cuda'
        extractor.load_model()
        
        #print(f"Extracting features for {video_path}")
        feature_dict = extractor.extract(video_path)
        v = list(feature_dict.values())[0]
        
        if len(v) == 0:
            print(f"Error processing {video_path}: Empty feature vector")
            return None

        v_flat = v.mean(axis=0)
        return v_flat
    
    except Exception as e:
        print(f"Error processing {video_path}: {e}")
        return None

def extract_features(data):
    model_name = 'r2plus1d_18_16_kinetics'
    config_path = 'C:/Users/josew/Desktop/Video_Extraction_test/video_features/configs/r21d.yml' # Find path for this file
    num_processes = 2

    with Pool(processes=num_processes) as pool:
        results = pool.starmap(process_video, [(video_path, model_name, config_path) for video_path in data])

    output = [result for result in results if result is not None]
    return np.array(output)

def save_features_to_csv(features, file_name='video_features.csv'):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'feature_{i}' for i in range(features.shape[1])])
        writer.writerows(features)