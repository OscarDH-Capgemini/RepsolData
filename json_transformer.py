import json
from datetime import datetime

# Archivo de entrada y salida
input_file = "REPSOL.json"
output_file = "REPSOL_optimized.json"

# Cargar el archivo JSON original
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Obtener columnas y datos
columns = data["columns"]
data_rows = data["data"]

# Crear la nueva estructura optimizada
optimized_data = []

for row in data_rows:
    # Convertir la lista en un diccionario basado en los nombres de las columnas
    row_dict = dict(zip(columns, row))
    
    # Modificar capacity (quitar "kW" y convertir a número)
    row_dict["capacity"] = int(row_dict["capacity"].replace("kW", ""))
    
    # Cambiar el prefijo en energy_source
    row_dict["energy_source"] = row_dict["energy_source"].replace("F01", "ES")
    
    # Calcular la duración del periodo de producción (nueva columna)
    start_date = datetime.strptime(row_dict["start_production_period"], "%d/%m/%Y")
    end_date = datetime.strptime(row_dict["end_production_period"], "%d/%m/%Y")
    row_dict["duration_production_period"] = (end_date - start_date).days
    
    # Añadir al nuevo formato
    optimized_data.append(row_dict)

# Guardar el JSON optimizado
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(optimized_data, file, indent=4, ensure_ascii=False)

print(f"Archivo optimizado guardado en: {output_file}")
