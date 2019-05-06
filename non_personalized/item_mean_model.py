"""
The item_mean_model module provides a class ItemMeanModel to store the mean ratings model
"""

class ItemMeanModel:
    """The class containerizes the frozenset of mean ratings and provides methods to access it.
        
        Attributes:
            means {dict} -- python dictionary with keys are the item ids and values are the mean rating
    """
    
    def __init__(self, means):
        """ init_method
        Arguments:
            means {dict} -- python dictionary with keys are the item ids and values are the mean rating
        Attributes:
            means {dict} -- python dictionary with keys are the item ids and values are the mean rating
        """

        self.means=means
        self.__item_means=frozenset(means.items())
    @property
    def means(self):
        """getter of the attribute means
        
        Returns:
            dict -- dictionary with item id as keys and mean ratings as values
        """

        return self.__means
    @means.setter
    def means(self,means):
        if not isinstance(means,dict):
            raise TypeError("invalid type, needs to be a dictionary")
        else:
            self.__means=means
    def get_known_items(self):
        """get the ids of the known items which are the keys of the attribute means
        
        Returns:
            list -- list of integer with item ids
        """

        return dict(self.__item_means).keys()
    def has_item(self,item_id):
        """check if a given item_id is part of the known items
        
        Arguments:
            item_id {integer} -- an id of some item to check its existence
        
        Returns:
            boolean -- True if the item_id is part of the list of known item and False otherwise
        """

        return item_id in self.get_known_items()
    def get_mean_rating(self,item_id):
        """return the mean rating of some item_id if it is known by the model
        
        Arguments:
            item_id {integer} -- an item id
        
        Raises:
            ValueError -- if the item_id is unkown by the model
        
        Returns:
            float -- mean rating corresponding to the item_id
        """

        if self.has_item(item_id):
            return dict(self.__item_means)[item_id]
        else:
            raise ValueError("unkown item id")
