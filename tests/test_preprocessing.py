
import unittest
import pandas as pd
from src.data_preprocessing import handle_missing_values

class TestDataPreprocessing(unittest.TestCase):
    def test_handle_missing_values(self):
        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, None]})
        df_filled = handle_missing_values(df)
        self.assertFalse(df_filled['A'].isnull().any())
        self.assertFalse(df_filled['B'].isnull().any())

if __name__ == '__main__':
    unittest.main()
