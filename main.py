import subprocess
import pandas as pd
import os

# Detect if the CSV is on the same folder
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
if not csv_files:
  raise ValueError("No CSV files found in the current directory")
    
csv_file = csv_files[0] # Get the first CSV file
print(f"CSV file found: {csv_files}")

# Ejecucion del Test
print("Ejecutando test.py")
subprocess.run(["python", "test.py", csv_file])

input("Presiona Enter para salir...")