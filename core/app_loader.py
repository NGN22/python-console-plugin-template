from pathlib import Path
import importlib
import inspect
from apps.contracts.app_contract import AppContract


class AppLoader:

    def __init__(self):
        self.apps = []
        self.errors = []
        self.discovered_apps = []

    def load(self):
        self.discover_apps()
        self.load_apps()

    #Descubrir carpetas appXX
    def discover_apps(self):
        apps_path = Path("apps")
        if not apps_path.exists():
            self.errors.append("No se encontró la carpeta apps")
            return
        for item in apps_path.iterdir():

            if item.is_dir() and item.name.startswith("app"):
                self.discovered_apps.append(item.name)




    def load_apps(self):
        for app_name in self.discovered_apps:
            module_name = f"apps.{app_name}.main"
            try:
                module = importlib.import_module(module_name)

            except Exception as error:
                self.errors.append(
                    f"Error importando {module_name}: {error}"
                )
                continue

            classes = inspect.getmembers(module, inspect.isclass)

            valid_classes = []
            for name, cls in classes:
                if self.validate_app(cls):
                    valid_classes.append(cls)


            if len(valid_classes) == 0:
                self.errors.append(
                    f"No se encontró una aplicación válida en {app_name}"
                )
                continue
            elif len(valid_classes) > 1:
                self.errors.append(
                    f"Multiples aplicaciones {app_name}"
                )
                continue

            app_class = valid_classes[0]
            try:
                app_instance = app_class()
            except Exception as error:
                self.errors.append(
                    f"Error instanciando {app_class.__name__}: {error}"
                )
                continue
            self.apps.append(app_instance)



    def validate_app(self, cls):
        return (
            issubclass(cls, AppContract) and cls is not AppContract
        )
