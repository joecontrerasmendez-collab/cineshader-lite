#!/usr/bin/env python3
"""
Aplica la config de CineShader Lite sobre Newb X Legacy
"""
import os, shutil

# Buscar config.h dentro de newb-src
def find_config():
    candidates = [
        "newb-src/include/newb/config.h",
        "newb-src/include/newb/config.glsl",
        "newb-src/src/config.h",
        "newb-src/config.h",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    # Búsqueda recursiva
    for root, dirs, files in os.walk("newb-src"):
        for f in files:
            if f in ("config.h", "config.glsl"):
                return os.path.join(root, f)
    return None

config_path = find_config()

if not config_path:
    print("❌ No se encontró config.h en Newb X Legacy")
    print("Archivos disponibles:")
    for root, dirs, files in os.walk("newb-src"):
        for f in files:
            print(" ", os.path.join(root, f))
    exit(1)

print(f"✓ Config encontrada en: {config_path}")

# Backup del original
shutil.copy(config_path, config_path + ".original")

# Leer config original
with open(config_path, 'r') as f:
    content = f.read()

# Leer nuestros overrides
with open("cineshader_config.h", 'r') as f:
    overrides = f.read()

# Agregar overrides al final (usando #undef primero para evitar redefiniciones)
final = content + "\n\n" + overrides

with open(config_path, 'w') as f:
    f.write(final)

print("✓ CineShader config aplicada correctamente")
print("  - Agua transparente con reflejos")
print("  - Vegetación animada (viento)")
print("  - Iluminación cálida/naranja")
print("  - Niebla cinematográfica")
print("  - Sol circular")
print("  - Optimizado para Snapdragon 6xx")
