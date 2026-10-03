from abc import ABC, abstractmethod


class AppContract(ABC):

    APP_NAME = "Sin nombre"

    @abstractmethod
    def run(self):
        pass