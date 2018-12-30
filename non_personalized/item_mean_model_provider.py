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
    def compute_mean(self):
        means_df = self.ratings_data.groupby(["itemID"])["rating"].mean()
        return means_df.to_dict()
    def get(self):
        return ItemMeanModel(self.compute_mean())
if __name__ == "__main__":
    ratings = pd.read_csv("data/ratings.csv")
    del ratings["timestamp"]
    ratings.columns=["userID","itemID","rating"]
    IMMP = ItemMeanModelProvider(ratings)
    print(IMMP.get().get_mean_rating(17))
