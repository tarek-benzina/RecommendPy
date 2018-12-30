import pandas as pd
from mean_item_based_recommender import MeanItemBasedRecommender

def main():
    ratings = pd.read_csv("data/ratings.csv")
    del ratings["timestamp"]
    ratings.columns=["userID","itemID","rating"]
    num_item_recommend = 10
    IMMP = MeanItemBasedRecommender(num_item_recommend, ratings)
    print(IMMP.n_highest())
if __name__ == "__main__":
    main()