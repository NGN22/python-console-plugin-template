# Python Console Application Template

Template para construir aplicaciones de consola utilizando una arquitectura basada en plugins.

## Estructura

```text
apps/
├── contracts/
├── app01/
├── app02/
└── ...

core/
└── app_loader.py

main.py
```

## Crear una nueva aplicación

Crear una carpeta:

```text
apps/app06
```

Crear:

```text
apps/app06/__init__.py
apps/app06/main.py
```

Implementar:

```python
from apps.contracts.app_contract import AppContract


class App06(AppContract):

    APP_NAME = "Mi Aplicación"

    def run(self):
        print("Hola mundo")
```

La aplicación aparecerá automáticamente en el menú.

## Ejecutar

```bash
python main.py
```

## Requisitos

Python 3.13+