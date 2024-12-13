import json
import time
import random
import os
import subprocess

# Ruta al archivo JSON en el repositorio local
JSON_FILE_PATH = "C:/Users/odelgado/RepsolData/REPSOL.json"
REPO_PATH = "C:/Users/odelgado/RepsolData"

# Función para generar una nueva entrada
def generate_new_entry(data):
    # Encuentra el mayor go_number actual
    last_go_number = max(int(entry["go_number"]) for entry in data)
    new_go_number = last_go_number + 1  # Incrementa en 1

    return {
        "go_number": str(new_go_number),  # Convierte de nuevo a string
        "issuing_body": str(random.randint(843702500, 843702599)),
        "energy_carrier": random.choice(["Gas", "Electricidad", "Hidrógeno"]),
        "type_of_gas": random.choice(["N/A", "Metano", "Hidrógeno Verde"]),
        "dissemination_level": "Autoconsumos",
        "original_holder": random.choice(["Energía Solar Barcelona", "Hidrogenera Madrid", "Red Gas Bilbao"]),
        "production_device": "843702522500000001",
        "capacity": str(random.randint(100, 1000)),
        "date_operational": "2025-01-01",
        "energy_source": random.choice(["Solar", "Hidrógeno", "Fósil"]),
        "mixture_of_inputs": 2,
        "type_of_installation": "Autoconsumos",
        "description_technology": random.choice(["Paneles solares fotovoltaicos", "Electrolizador"]),
        "production_device_location": random.choice(["Barcelona", "Bilbao", "Madrid", "Oviedo", "Sevilla", "Valencia"]),
        "purpose": "Generación Distribuida",
        "start_production_period": "2025-01-01",
        "end_production_period": "2035-01-01",
        "issuing_date": "2024-12-12"
    }


# Función para leer y sobrescribir el JSON
def update_json():
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)  # El JSON ya es una lista directamente
    
    new_entry = generate_new_entry()
    data.append(new_entry)  # Agrega la nueva entrada directamente a la lista
    
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
    print(f"Entrada añadida: {new_entry}")


# Función para hacer commit y push
def git_commit_and_push():
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", JSON_FILE_PATH], check=True)
    subprocess.run(["git", "commit", "-m", "Actualización automática del JSON"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Cambios subidos a GitHub.")

# Bucle principal
start_time = time.time()
while time.time() - start_time < 3600:  # Durante 1 hora
    update_json()  # Sobrescribir JSON con nueva entrada
    git_commit_and_push()  # Hacer push a GitHub
    time.sleep(20)  # Esperar 20 segundos
