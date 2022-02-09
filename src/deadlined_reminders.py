from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from datetime import date
from dateutil.parser import parse
from datetime import datetime


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):


    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(Iterable, ABC):


    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):


    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text 

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat])