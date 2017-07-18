from abc import ABCMeta, abstractmethod

__author__ = 'Lucas Kjaero'

class FeedReader:
    # Makes this an abstract class.
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_sentences(self):
        raise NotImplementedError

    @abstractmethod
    def get_articles(self):
        raise NotImplementedError
