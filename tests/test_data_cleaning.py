import pandas as pd
from scripts.data_cleaning import clean_data

def test_clean_data():
    """
    Test the clean_data function to ensure missing values are handled correctly.
    """
    # Sample dataset with missing values
    data = pd.DataFrame({"A": [1, None], "B": [2, 3]})

    # Apply the clean_data function
    cleaned_data = clean_data(data)

    # Check if all missing values are removed
    assert cleaned_data.isnull().sum().sum() == 0, "There are still missing values in the dataset!"
    assert len(cleaned_data) == 1, "Rows with missing values were not dropped correctly."
    print("Test passed!")

