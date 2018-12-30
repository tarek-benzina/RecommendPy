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
