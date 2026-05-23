# Este Dockerfile es para una aplicación FastAPI que se ejecutará en un contenedor Docker. 
# Utiliza la imagen base de Python 3.13-slim para mantener el tamaño del contenedor lo más 
# pequeño posible. El Dockerfile copia los archivos necesarios, instala las dependencias y 
# expone el puerto 8000 para que la aplicación sea accesible desde fuera del contenedor.

FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias necesarias para la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto 8000 para que la aplicación sea accesible desde fuera del contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI utilizando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]