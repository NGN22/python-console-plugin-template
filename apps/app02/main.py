from apps.contracts.app_contract import AppContract

class App02(AppContract):

    APP_NAME = "Aplicacion 02"

    def run(self):
        print("Ejecutando 02")