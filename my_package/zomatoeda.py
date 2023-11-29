import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class ExploratoryDataAnalysis:
    """
    A class for performing exploratory data analysis on a dataset using Matplotlib and Seaborn.

    This class provides methods for various EDA techniques including univariate and bivariate analysis, correlation analysis, and distribution checks.

    Attributes:
    ----------
    dataset : pandas.DataFrame
        The dataset to be analyzed.

    Methods:
    -------
    plot_histogram(column):
        Plots a histogram for a specified column.

    plot_boxplot(column):
        Plots a boxplot for a specified column.

    plot_scatter(x, y):
        Plots a scatter plot for two specified columns.

    plot_correlation_matrix():
        Plots a heatmap of the correlation matrix.

    plot_pairplot():
        Plots pairplot for the dataset.
    """

    def __init__(self, dataset):
        """
        Initializes the ExploratoryDataAnalysis with the specified dataset.
        """
        self.dataset = dataset

    def plot_histogram(self, column):
        """
        Plots a histogram for a specified column.
        """
        plt.figure(figsize=(8, 6))
        sns.histplot(self.dataset[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.show()

    def plot_boxplot(self, column):
        """
        Plots a boxplot for a specified column.
        """
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=self.dataset[column])
        plt.title(f'Boxplot of {column}')
        plt.show()

    def plot_scatter(self, x, y):
        """
        Plots a scatter plot for two specified columns.
        """
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=self.dataset[x], y=self.dataset[y])
        plt.title(f'Scatter Plot of {x} vs {y}')
        plt.show()

    def plot_correlation_matrix(self):
        """
        Plots a heatmap of the correlation matrix.
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.dataset.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()

    def plot_pairplot(self):
        """
        Plots pairplot for the dataset.
        """
        sns.pairplot(self.dataset)
        plt.show()
