# Generador de Contraseñas Básico

Convierte cualquier texto en una contraseña segura y fácil de recordar.

Esta herramienta web, hecha con Python y Flask, toma la primera letra de cada palabra de tu texto (poema, frase, fragmento de libro, etc.) y genera una contraseña corta alternando mayúsculas/minúsculas.

## ¿Cómo funciona?
1. Escribe o pega tu texto en la página web.
2. Haz clic en "Generar contraseña".
3. Obtén una contraseña de hasta 12 caracteres, lista para usar.

## Instalación rápida
1. Clona el repositorio:
   ```
   git clone https://github.com/KalzKiw/textToPassword.git
   cd textToPassword
   ```
2. Instala dependencias:
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install flask
   ```
3. Ejecuta la app:
   ```
   python app/main.py
   ```
4. Abre tu navegador en `http://127.0.0.1:5000` (o usa tu IP local si quieres acceder desde otra máquina).

## Estructura del proyecto
- `app/main.py`: Lógica principal y servidor web.
- `app/templates/index.html`: Interfaz web para el usuario.

## Personalización
Puedes modificar la longitud, reglas o estilo de la contraseña editando `main.py`.


---
## Ejemplo de uso

![Ejemplo de la aplicación](./screenshot.png)

### Poema de Gloria Fuertes

```text
Pienso mesa y digo silla,
Compro pan y me lo dejo,
Lo que aprendo se me olvida,
Lo que pasa es que te quiero.

La trilla lo dice todo;
Y el mendigo en el alero,
El pez vuela por la sala
El toro sopla en el ruedo.

Entre Santander y Asturias
Pasa un río, pasa un ciervo,
Pasa un rebaño de santas,
Pasa un peso.

Entre mi sangre y el llanto
Hay un puente muy pequeño,
Y por él no pasa nada,
Lo que pasa es que te quiero.
```

La contraseña generada para este poema sería, por ejemplo: `PmYdScPyMIDI`
