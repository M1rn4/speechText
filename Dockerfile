# EstaMblecer la imagen base
FROM ubuntu:latest
RUN apt update 

RUN apt install -y python3-pip

RUN apt update
# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "clonar.py"]
