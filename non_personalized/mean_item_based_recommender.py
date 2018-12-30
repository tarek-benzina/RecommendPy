from item_mean_model_provider import ItemMeanModelProvider
import pandas as pd
"""
The mean based recommender provides the possiblity to generate recommendations
based on the items mean ratings provided from the users
"""
class MeanItemBasedRecommender(ItemMeanModelProvider):
    def __init__(self, num_top_rated,ratings_data):
        self.num_top_rated = num_top_rated
        self.ratings_data = ratings_data
    @property
    def num_top_rated(self):
        return self.__num_top_rated
    @num_top_rated.setter
    def num_top_rated(self, num_top_rated):
        if not isinstance(num_top_rated,int):
            raise TypeError("non valid type, should be an integer")
        elif num_top_rated <= 0:
            raise ValueError("invalid value, should be a positive integer")
        else:
            self.__num_top_rated = num_top_rated
    def n_highest(self):
        means = self.get().means
        means_df=pd.DataFrame.from_dict(means,orient="index")
        means_df.columns=["rating"]
        return means_df.nlargest(self.num_top_rated,"rating").index