import pandas as pd
import pyarrow

def read_feather_and_save_copy(path_to_feather, copy_path):
    try:
        df = pd.read_feather(path_to_feather)
        print("Lecture réussie avec pd.read_feather")
        print(df.head())

        df.to_csv(copy_path, index=False, encoding='utf-8')
        print(f"Copie du DataFrame décodé sauvegardée dans : {copy_path}")

    except pyarrow.lib.ArrowInvalid as e:
        print(f"Erreur Arrow lors de la lecture Feather : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

path_to_feather = "/private/tmp/catalog"
copy_path = "/private/tmp/decoded_catalog.csv"

read_feather_and_save_copy(path_to_feather, copy_path)
