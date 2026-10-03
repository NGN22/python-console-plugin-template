from apps.contracts.app_contract import AppContract


class App01(AppContract):

    APP_NAME = "Aplicación 01"

    def run(self):
        print("Ejecutando 01")