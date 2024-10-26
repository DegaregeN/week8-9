
import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from src.model_training import evaluate_model

class TestModelTraining(unittest.TestCase):
    def setUp(self):
        # Load dataset
        self.df = pd.read_csv('../data/creditcard.csv')
        self.X = self.df.drop('Class', axis=1)
        self.y = self.df['Class']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier()

    def test_evaluate_model(self):
        self.model.fit(self.X_train, self.y_train)
        evaluate_model(self.model, self.X_test, self.y_test)

if __name__ == '__main__':
    unittest.main()




