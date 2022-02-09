from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    
    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due(self):
        pass