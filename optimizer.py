import pandas as pd
import numpy as np

class TransportOptimizer:
    def __init__(self):
        self.locations = []
        self.distances = pd.DataFrame()

    def load_matrix(self, df):
        self.locations = df.index.tolist()
        self.distances = df.astype(float)
        # Ensure the diagonal (city to itself) is always zero
        for loc in self.locations:
            self.distances.at[loc, loc] = 0.0