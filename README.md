# PERSONAL DESKTOP PASSWORD MANAGER

# ⚙️Instalación y Configuración 

## 1. Clonar el Repositorio

Clona el repositorio desde GitHub:

```sh
git clone https://github.com/JorgePerezEC/desktop-password-manager.git
cd desktop-password-manager
cd code
```

## 2. Configurar el Entorno Virtual (OPCIONAL)

Se recomienda usar entorno virtual para gestionar las dependencias del proyecto.

```sh
python -m venv venv
```

### Activar el entorno virtual:

```sh
venv\Scripts\activate
```

## 3. Instalar Dependencias

Instala las dependencias necesarias usando requirements.txt:

```sh
pip install -r requirements.txt
```

## 4. Configurar la Base de Datos

Instala las dependencias necesarias usando requirements.txt:

```sh
python src/database/db.py
```

## 5. Ejecutar las Pruebas

Las pruebas están organizadas en la carpeta tests. Puedes ejecutar las pruebas con `pytest`:

```sh
pytest test/[nombre_del_archivo.py]
```

## Estructura de los Archivos de Prueba

- **`test_auth.py`**: Contiene pruebas para las funciones de autenticación (`create_user`, `login`, `logout`).
- **`test_encryption.py`**: Contiene pruebas para las funciones de encriptación de contraseñas.
- **`test_db.py`**: Contiene pruebas para las funciones relacionadas con la base de datos.


# ✅Instrucciones para Subir Cambios y Configurar Revisión 

## 1. Configurar tu Repositorio Local

Asegúrate de que tu repositorio local esté sincronizado con el repositorio remoto. Primero, realiza un `pull` para obtener la última versión del código:

```sh
git pull origin main
```

## 2. Crear una Nueva Rama

Es una buena práctica trabajar en una rama separada para que puedas probar y revisar tus cambios sin afectar el código principal. Crea una nueva rama para tus cambios:

```sh
git checkout -b test_feature
```

## 3. Realizar Cambios y Commit

Haz los cambios necesarios en tu código y luego realiza un commit para registrar estos cambios en tu rama:

```sh
git add .
git commit -m "Ejemplo de Descripción de los cambios realizados"
```

Asegúrate de proporcionar un mensaje de commit claro y descriptivo.

## 4. Subir la Rama al Repositorio Remoto

Sube tu rama al repositorio remoto para poder revisarla:

```sh
git push origin test_feature
```
