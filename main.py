import os
import time
import win32com.client
from extracting import extract_features, save_features_to_csv

### PREPARANDO PATHS, usa si no en local
def resolve_shortcut(lnk_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk_path)
    return shortcut.Targetpath

def main():
    tr = r"G:/Mi unidad/ML_P3/train_subset.lnk" # Carpeta de video
    tr_path = resolve_shortcut(tr) # Solo usa si tienes el acceso directo al drive de videos

    train_subset = [tr_path + '\\' +i for i in os.listdir(tr_path)]

    start = time.time()
    train_feats = extract_features(train_subset) # Usa ~2000 videos
    end = time.time()

    execution_time = end - start
    hours, remainder = divmod(int(execution_time), 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_time = f'{hours:02}:{minutes:02}:{seconds:02}'
    print(f'Execution time of feature extraction: {formatted_time}')
    
    save_features_to_csv(train_feats, 'training_features.csv') # Reemplaza el nombre para cada particion del train_subset

if __name__ == '__main__':
    main()