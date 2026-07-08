# Sistema de Gestión de Estacionamiento

Trabajo Final Integrador de Programación en Python.

## Integrantes

* González, Valentina.
* Menéndez, Ignacio Manuel.
* Pareja Bruno, María del Pilar.

## Comisión

*Comisión:* 1.4

---

# Descripción del sistema

Este proyecto consiste en un sistema de gestión de estacionamiento desarrollado en Python para ejecutarse desde la consola.

El sistema permite:

* Registrar el ingreso de vehículos.
* Registrar el egreso de vehículos.
* Controlar la capacidad disponible del estacionamiento.
* Calcular el importe a pagar según el tiempo de permanencia.
* Mostrar los vehículos que permanecen estacionados.
* Generar estadísticas diarias del estacionamiento.
* Registrar automáticamente la fecha y hora de ingreso y egreso.
* Conservar la información entre ejecuciones mediante archivos de texto.

El sistema funciona mediante un menú interactivo por consola, donde el usuario selecciona la operación que desea realizar.

---

# Estructura del proyecto

text
proyecto_python/
│
├── estacionamiento/
│   ├── main.py
│   ├── funciones.py
│   ├── vehiculos.txt
│   ├── estadisticas.txt
│   └── registro_estacionamiento.txt
│
├── .gitignore
└── README.md


* *main.py:* contiene el menú principal y controla la ejecución del programa.
* *funciones.py:* contiene toda la lógica del sistema.
* *vehiculos.txt:* almacena los vehículos que permanecen estacionados.
* *estadisticas.txt:* almacena las estadísticas diarias del sistema.
* *registro_estacionamiento.txt:* registra los ingresos y egresos con fecha y hora.

> Los archivos de datos se crean automáticamente la primera vez que se utiliza el sistema.

---

# Instrucciones de uso

## Requisitos

* Tener instalado Python 3.
* Descargar o clonar este repositorio.

## Ejecución del programa

1. Abrir una terminal o consola.
2. Ubicarse en la carpeta del proyecto.
3. Ingresar a la carpeta estacionamiento.
4. Ejecutar:

bash
python main.py


En algunos sistemas puede ser necesario utilizar:

bash
python3 main.py


---

# Cómo utilizar el sistema

Al iniciar el programa se mostrará el siguiente menú:

text
===== ESTACIONAMIENTO =====

1. Ingresar vehículo
2. Registrar egreso
3. Ver vehículos estacionados
4. Ver espacios disponibles
5. Ver estadísticas
6. Salir


Seleccione la opción correspondiente.

---

## Opción 1 - Ingresar vehículo

Permite registrar el ingreso de un vehículo.

El sistema solicitará únicamente:

* Patente.

La fecha y la hora de ingreso se registran automáticamente utilizando el reloj del sistema.

Si el vehículo ya se encuentra registrado o el estacionamiento alcanzó su capacidad máxima, se mostrará un mensaje de error.

---

## Opción 2 - Registrar egreso

Permite registrar la salida de un vehículo.

El sistema solicitará únicamente:

* Patente.

La fecha y la hora de salida se registran automáticamente.

Luego calculará:

* Tiempo de permanencia.
* Importe a pagar.
* Actualización de las estadísticas del día.

*El importe se calcula a razón de $1000 por hora de permanencia (con un mínimo de una hora).*

---

## Opción 3 - Ver vehículos estacionados

Muestra todas las patentes de los vehículos que permanecen estacionados junto con la fecha y hora de ingreso.

---

## Opción 4 - Ver espacios disponibles

Informa:

* Capacidad total del estacionamiento.
* Cantidad de lugares ocupados.
* Cantidad de lugares disponibles.

---

## Opción 5 - Ver estadísticas

Muestra las estadísticas organizadas por fecha:

* Vehículos atendidos por día.
* Recaudación diaria.
* Tiempo promedio de permanencia por día.

---

## Opción 6 - Salir

Finaliza la ejecución del programa.

Toda la información queda almacenada automáticamente para que esté disponible la próxima vez que se ejecute el sistema.

---

# Persistencia de datos

El sistema guarda automáticamente la información utilizando archivos de texto.

Se almacenan:

* Vehículos actualmente estacionados.
* Estadísticas diarias.
* Registro histórico de ingresos y egresos.

De esta manera, al cerrar y volver a abrir el programa, la información no se pierde.

---

# Validaciones implementadas

El sistema verifica que:

* No se exceda la capacidad máxima de 50 vehículos.
* No se registre una patente que ya se encuentra estacionada.
* La patente exista al momento de registrar un egreso.
* La opción seleccionada en el menú sea válida.

---

# Tecnologías utilizadas

* Python 3
* Git
* GitHub

---

# Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó ChatGPT como herramienta de apoyo para:

* Resolver dudas sobre la sintaxis y conceptos de Python.
* Explicar el funcionamiento de estructuras de datos y funciones.
* Colaborar en la detección y corrección de errores.
* Asistir en la elaboración de la documentación del proyecto.

La implementación, las decisiones de desarrollo y la versión final del proyecto fueron realizadas por los integrantes del grupo.
