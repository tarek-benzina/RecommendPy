"""Creates a model based on the ItemMeanModel, and computes the mean rating for each item
by adding a new method called get that returns an ItemMeanModel based on the computed means

Raises:
    TypeError -- Raises an error if the input (ratings) is not a pandas dataframe

Returns:
    ItemMeanModel -- Model with the items ids and their mean ratings
"""
from item_mean_model import ItemMeanModel
import pandas as pd
class ItemMeanModelProvider(ItemMeanModel):
    def __init__(self,ratings_data):
        self.ratings_data=ratings_data
    @property
    def ratings_data(self):
        return self.__ratings_data
    @ratings_data.setter
    def ratings_data(self,ratings_data):
        if not isinstance(ratings_data,pd.DataFrame):
            raise TypeError("unkown data type")
        else:
            self.__ratings_data=ratings_data
    def __compute_mean(self):
        means_df = self.ratings_data.groupby(["itemID"])["rating"].mean()
        return means_df.to_dict()
    def get(self):
        return ItemMeanModel(self.__compute_mean())
