from django.apps import apps

# Obtener todas las clases de modelo registradas en la aplicación 'miapp'
models = apps.get_models(app_label='app')

# Iterar sobre cada clase de modelo y obtener el nombre de la tabla
for model in models:
    table_name = model._meta.db_table
    print(table_name)