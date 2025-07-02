# 1. Usar una imagen base oficial de Python
FROM python:3.8-slim

# 2. Establecer variables de entorno
ENV PYTHONUNBUFFERED=1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# 5. Copiar todo el código del proyecto al contenedor
COPY . .

# ¡NUEVO! Ejecutar collectstatic
RUN python manage.py collectstatic --noinput

# 6. Exponer el puerto en el que correra la aplicacion
EXPOSE 8000

# 7. Comando para ejecutar la aplicacion
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tienda_project.wsgi:application"]