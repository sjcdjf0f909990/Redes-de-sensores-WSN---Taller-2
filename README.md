# Taller 2 - Introducción a ROS 2 (WSN_T2)

**Autor:** Anthony Vinicio Domínguez Chacha  
**Fecha:** 15 de octubre de 2025  
**Materia:** Redes de Sensores  

---

## 📘 Descripción

Este proyecto implementa una **red de sensores simulada** en **ROS 2 (Jazzy)**, desplegada dentro de un contenedor **Docker**, con tres nodos principales:

- **sensor_node** → Publica temperaturas aleatorias.  
- **reader_node / reader_node2** → Reciben los datos publicados.  
- **plotter_node** → Genera una gráfica (`sensor_plot.png`) con los valores recibidos.

El entorno se construye automáticamente mediante un `Dockerfile`, basado en la imagen oficial `osrf/ros:jazzy-desktop`.

---

## ⚙️ Cómo ejecutar (resumen de pasos)

Sigue estos pasos dentro de la carpeta del proyecto:

```bash
# 1. Construir la imagen
docker build -t wsn-reto:latest .

# 2. Ejecutar el contenedor
docker run -it --name wsn_reto --rm wsn-reto:latest

# 3. Ejecutar los nodos dentro del contenedor

# Nodo publicador
ros2 run sensor_program sensor_node

# Nodo lector
ros2 run sensor_program reader_node

# Nodo graficador
ros2 run sensor_program plotter_node
