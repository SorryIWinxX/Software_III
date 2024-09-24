# Etapa 1: Construcción
# Usa la imagen base de OpenJDK 21
FROM openjdk:21-jdk-slim

# Define el directorio de trabajo
WORKDIR /app

# Instala Gradle
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://services.gradle.org/distributions/gradle-7.6-bin.zip -P /tmp && \
    unzip /tmp/gradle-7.6-bin.zip -d /opt && \
    ln -s /opt/gradle-7.6/bin/gradle /usr/bin/gradle && \
    rm /tmp/gradle-7.6-bin.zip

# Copia los archivos de tu aplicación
COPY . .

# Comando para construir tu aplicación
CMD ["gradle", "build", "--no-daemon"]