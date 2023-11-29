import pandas as pd

class DataCleaning:
    """
    A class for performing basic data cleaning tasks on a dataset without using sklearn features.

    This class provides methods for handling missing values, removing duplicates, manually encoding categorical variables, and normalizing numerical features.

    Attributes:
    ----------
    dataset : pandas.DataFrame
        The dataset to be cleaned.

    Methods:
    -------
    handle_missing_values(strategy='mean'):
        Fills or drops missing values based on the specified strategy.

    remove_duplicates():
        Removes duplicate rows from the dataset.

    encode_categorical_variables(columns):
        Manually encodes the specified categorical columns.

    normalize_features(columns):
        Normalizes numerical features.
    """

    def __init__(self, dataset):
        """
        Initializes the DataCleaning with the specified dataset.
        """
        self.dataset = dataset

    def handle_missing_values(self, strategy='mean'):
        """
        Fills or drops missing values based on the specified strategy.
        """
        if strategy == 'drop':
            self.dataset.dropna(inplace=True)
        else:
            for col in self.dataset.select_dtypes(include=['float64', 'int64']).columns:
                if strategy == 'mean':
                    fill_value = self.dataset[col].mean()
                elif strategy == 'median':
                    fill_value = self.dataset[col].median()
                elif strategy == 'mode':
                    fill_value = self.dataset[col].mode()[0]
                self.dataset[col].fillna(fill_value, inplace=True)

    def remove_duplicates(self):
        """
        Removes duplicate rows from the dataset.
        """
        self.dataset.drop_duplicates(inplace=True)

    def encode_categorical_variables(self, columns):
        """
        Manually encodes the specified categorical columns.
        """
        for col in columns:
            dummies = pd.get_dummies(self.dataset[col], prefix=col)
            self.dataset = pd.concat([self.dataset, dummies], axis=1)
            self.dataset.drop(col, axis=1, inplace=True)

    def normalize_features(self, columns):
        """
        Normalizes numerical features.
        """
        for col in columns:
            self.dataset[col] = (self.dataset[col] - self.dataset[col].mean()) / self.dataset[col].std()
