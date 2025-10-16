# ===============================
#   ROS 2 Jazzy - Reto Taller
# ===============================
FROM osrf/ros:jazzy-desktop

LABEL maintainer="tu_nombre <tu_correo@ejemplo.com>"

# 1. Instalar herramientas necesarias
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-pip \
    python3-matplotlib \
    nano \
 && rm -rf /var/lib/apt/lists/*

# 2. (Alternativa pip) – si se requiere instalar matplotlib por pip
# RUN pip install matplotlib --break-system-packages

# 3. Crear workspace
WORKDIR /root/ros2_ws/src

# 4. Copiar el paquete desde el host al contenedor
COPY sensor_program/ ./sensor_program/

# 5. Compilar el workspace
WORKDIR /root/ros2_ws
RUN . /opt/ros/jazzy/setup.sh && colcon build

# 6. Configurar el entorno ROS en bashrc
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc && \
    echo "source /root/ros2_ws/install/setup.bash" >> /root/.bashrc

# 7. Entry point oficial
ENTRYPOINT ["/ros_entrypoint.sh"]

# 8. Por defecto, abrir bash interactivo
CMD ["bash"]
