import pandas as pd
import os

class IOHandler:
    def load_csv(self, obj, filename="distance.csv"):
        if not os.path.exists(filename):
            print(f"Error: {filename} not found!")
            return False
        try:
            # index_col=0 treats the first column as city names
            df = pd.read_csv(filename, index_col=0)
            obj.load_matrix(df)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False