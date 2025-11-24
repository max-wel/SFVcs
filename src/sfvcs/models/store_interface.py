from abc import ABC, abstractmethod

class StoreInterface(ABC):
    @abstractmethod
    def save_object(self, data):
        pass