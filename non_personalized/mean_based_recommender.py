"""
The mean based recommender provides the possiblity to generate recommendations
based on the items mean ratings provided from the users 
"""
class ItemMeanModelProvider:
    """ This class provides a model to recommend items based on their mean ratings by the
    users. The model uses the number of items to recommends and provides the list of top 
    rated items based on their average ratings
    
    Raises:
        TypeError -- [description]
        ValueError -- [description]
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, num_top_rated):
        """[summary]
        
        Arguments:
            num_top_rated {[type]} -- [description]
        """

        self.num_top_rated=num_top_rated
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