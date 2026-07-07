# Sistema de Gestión de Estacionamiento

Trabajo Final Integrador de Programación en Python.

## Integrantes

- González, Valentina.
- Menéndez, Ignacio Manuel.
- Pareja Bruno, María del Pilar.

## Comisión

**Comisión:** 1.4

---

# Descripción del sistema

Este proyecto consiste en un sistema de gestión de estacionamiento desarrollado en Python para ejecutarse desde la consola.

El sistema permite:

- Registrar el ingreso de vehículos.
- Registrar el egreso de vehículos.
- Controlar la capacidad disponible del estacionamiento.
- Calcular el importe a pagar según las horas de permanencia.
- Mostrar los vehículos que permanecen estacionados.
- Generar estadísticas de uso del estacionamiento.

El sistema funciona mediante un menú interactivo por consola, donde el usuario selecciona la operación que desea realizar.

---

# Estructura del proyecto

```
proyecto_python/
│
├── estacionamiento/
│   ├── main.py
│   └── funciones.py
│
├── .gitignore
└── README.md
```

- **main.py:** contiene el menú principal y controla la ejecución del programa.
- **funciones.py:** contiene toda la lógica del sistema y las funciones utilizadas por el programa.

---

# Instrucciones de uso

## Requisitos

- Tener instalado Python 3.
- Descargar o clonar este repositorio en la computadora.

## Ejecución del programa

1. Abrir una terminal o consola.
2. Ubicarse en la carpeta donde se encuentra el proyecto.
3. Ingresar a la carpeta `estacionamiento`.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

---

# Cómo utilizar el sistema

Al iniciar el programa se mostrará el siguiente menú:

```
===== ESTACIONAMIENTO =====

1. Ingresar vehículo
2. Registrar egreso
3. Ver vehículos estacionados
4. Ver espacios disponibles
5. Ver estadísticas
6. Salir
```

Seleccione una opción ingresando el número correspondiente.

## Opción 1 - Ingresar vehículo

Permite registrar el ingreso de un vehículo al estacionamiento.

El sistema solicitará:

- Patente.
- Hora de ingreso (entre 0 y 23).

Si el vehículo ya se encuentra registrado o el estacionamiento alcanzó su capacidad máxima, se mostrará un mensaje de error.

---

## Opción 2 - Registrar egreso

Permite registrar la salida de un vehículo.

El sistema solicitará:

- Patente.
- Hora de salida (entre 0 y 23).

Luego calculará:

- Horas de permanencia.
- Importe a pagar.
- Actualización de las estadísticas del sistema.

**El importe se calcula a razón de $1000 por cada hora de permanencia.**

---

## Opción 3 - Ver vehículos estacionados

Muestra todas las patentes de los vehículos que permanecen estacionados en ese momento.

---

## Opción 4 - Ver espacios disponibles

Informa:

- Capacidad total del estacionamiento.
- Cantidad de lugares ocupados.
- Cantidad de lugares disponibles.

---

## Opción 5 - Ver estadísticas

Muestra:

- Total de vehículos atendidos.
- Recaudación total.
- Tiempo promedio de permanencia de los vehículos.

---

## Opción 6 - Salir

Finaliza la ejecución del programa.

---

# Validaciones implementadas

El sistema verifica que:

- No se exceda la capacidad máxima de 50 vehículos.
- No se registre una patente que ya se encuentra estacionada.
- La hora ingresada esté comprendida entre 0 y 23.
- La hora de salida no sea menor que la hora de ingreso.
- La patente exista al momento de registrar un egreso.
- La opción seleccionada en el menú sea válida.

---

# Tecnologías utilizadas

- Python 3
- Git
- GitHub

---

# Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó ChatGPT como herramienta de apoyo para:

- Resolver dudas sobre la sintaxis y conceptos de Python.
- Explicar el funcionamiento de estructuras de datos y funciones.
- Colaborar en la detección y corrección de errores.
- Asistir en la elaboración de la documentación del proyecto (README).

La implementación, las decisiones de desarrollo y la versión final del proyecto fueron realizadas por los integrantes del grupo.

---

# Licencia

Proyecto desarrollado con fines exclusivamente académicos para la materia **Programación en Python**.
