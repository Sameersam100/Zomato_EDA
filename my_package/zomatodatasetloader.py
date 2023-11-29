import pandas as pd

class ZomatoDatasetLoader:
    """
    A class to load and retrieve the Zomato dataset.

    This class provides methods to load the Zomato dataset from a CSV file into a pandas DataFrame and retrieve it for analysis.

    Attributes
    ----------
    file_path : str
        The file path to the Zomato dataset CSV file.
    zomato_dataset : pandas.DataFrame or None
        The loaded Zomato dataset, or None if the dataset hasn't been loaded yet.

    Methods
    -------
    load_dataset():
        Loads the Zomato dataset from the CSV file and stores it in zomato_dataset attribute.
    get_dataset():
        Returns the loaded Zomato dataset if available, otherwise returns an error message.
    """

    def __init__(self, file_path):
        """
        Constructs all the necessary attributes for the ZomatoDatasetLoader object.

        Parameters
        ----------
            file_path : str
                The file path to the Zomato dataset CSV file.
        """
        self.file_path = file_path
        self.zomato_dataset = None

    def load_dataset(self):
        """
        Load the Zomato dataset.

        Attempts to read the Zomato dataset CSV file and store it in the zomato_dataset attribute.
        Handles FileNotFoundError if the file is not found at the given path.

        Returns
        -------
        pandas.DataFrame or str
            The loaded Zomato dataset DataFrame, or an error message if the file is not found.
        """
        try:
            self.zomato_dataset = pd.read_csv(self.file_path, encoding='ISO-8859-1')
            return self.zomato_dataset
        except FileNotFoundError:
            return f"Error: File not found at {self.file_path}"

    def get_dataset(self):
        """
        Retrieve the loaded Zomato dataset.

        Returns the Zomato dataset if it has been loaded. If the dataset is not loaded, returns an error message.

        Returns
        -------
        pandas.DataFrame or str
            The loaded Zomato dataset DataFrame, or an error message if the dataset is not loaded.
        """
        if self.zomato_dataset is not None:
            return self.zomato_dataset
        else:
            return "Error: Zomato dataset not loaded. Use load_dataset() method first."
