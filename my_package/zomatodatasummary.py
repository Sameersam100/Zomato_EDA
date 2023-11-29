import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataSummary:
    """
    A class for providing a comprehensive summary of a dataset.

    This class includes various methods to display information about a dataset, aiding in understanding its structure, content, and potential issues before data cleaning, preprocessing, and exploratory data analysis.

    Attributes:
    ----------
    dataset : pandas.DataFrame
        The dataset to be summarized.

    Methods:
    -------
    display_head(n=5):
        Displays the first n rows of the dataset.

    display_shape():
        Shows the number of rows and columns in the dataset.

    display_info():
        Provides a concise summary of the dataset.

    display_descriptive_statistics():
        Shows descriptive statistics for numerical columns.

    display_missing_values():
        Indicates the number of missing values in each column.

    display_unique_values(column):
        Shows unique values in a specified column.

    display_data_types():
        Displays the data types of each column.

    plot_missing_values():
        Visualizes the distribution of missing values in the dataset.
    """

    def __init__(self, dataset):
        """
        Initializes the DataSummary with the specified dataset.
        """
        self.dataset = dataset

    def display_head(self, n=5):
        """
        Displays the first n rows of the dataset.
        """
        return self.dataset.head(n)

    def display_shape(self):
        """
        Displays the number of rows and columns in the dataset.
        """
        return self.dataset.shape

    def display_info(self):
        """
        Provides a concise summary of the dataset.
        """
        return self.dataset.info()

    def display_descriptive_statistics(self):
        """
        Shows descriptive statistics for numerical columns.
        """
        return self.dataset.describe()

    def display_missing_values(self):
        """
        Indicates the number of missing values in each column.
        """
        return self.dataset.isna().sum()

    def display_unique_values(self, column):
        """
        Shows unique values in a specified column.
        """
        return self.dataset[column].unique()

    def display_data_types(self):
        """
        Displays the data types of each column.
        """
        return self.dataset.dtypes

    def plot_missing_values(self):
        """
        Visualizes the distribution of missing values in the dataset.
        """
        plt.figure(figsize=(12, 6))
        sns.heatmap(self.dataset.isnull(), cbar=False, yticklabels=False, cmap='viridis')
        plt.title("Distribution of Missing Values")
        plt.show()
