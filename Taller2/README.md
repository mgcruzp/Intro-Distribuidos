# Sistema de Cálculo Distribuido con gRPC

Este proyecto implementa un **sistema distribuido de cálculo matemático** utilizando **gRPC**. Se compone de **cuatro servidores** y un **cliente**:

- **Servidor de Cálculo** (`servidor_calculo.py`) → Coordina las operaciones y distribuye las tareas.
- **Servidor Aritmético** (`servidor_aritmetico.py`) → Ejecuta sumas, restas, multiplicaciones y divisiones.
- **Servidor Avanzado** (`servidor_avanzado.py`) → Ejecuta potencias y raíces.
- **Servidor Auxiliar** (`servidor_auxiliar.py`) → Actúa como respaldo si los servidores fallan.
- **Cliente** (`cliente.py`) → Envía operaciones al servidor de cálculo.

---

##  **Requisitos**
Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- `grpcio` y `grpcio-tools`
- Un editor de código o terminal (VSCode, PyCharm, Ubuntu, etc.)

### **🔹 Instalar Dependencias**
Ejecuta el siguiente comando para instalar los paquetes necesarios:

```sh
pip3 install grpcio grpcio-tools
```

---

## ⚙️ **Generar Código gRPC**
Antes de ejecutar el sistema, es necesario **compilar el archivo `.proto`** para generar los archivos de código gRPC.

Ejecuta el siguiente comando dentro del directorio del proyecto:

```sh
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
```

Este comando generará:
- `calculadora_pb2.py`
- `calculadora_pb2_grpc.py`

**Estos archivos deben estar en el mismo directorio que los servidores y el cliente.**

---

## **Ejecutar los Servidores**
### ** En la Computadora de los Servidores (Ange)**
Ejecuta en **cuatro terminales diferentes**:

```sh
python3 servidor_calculo.py
python3 servidor_aritmetico.py
python3 servidor_avanzado.py
python3 servidor_auxiliar.py
```

 **Cada servidor se ejecuta en un puerto diferente:**
- `50050` → Servidor de Cálculo
- `50051` → Servidor Aritmético
- `50052` → Servidor Avanzado
- `50053` → Servidor Auxiliar

### ** En la Computadora del Cliente (Tú)**
Ejecuta:

```sh
python3 cliente.py
```

---

## 📡 **Cómo Usar el Cliente**
Una vez que el cliente esté corriendo, puedes **ingresar operaciones** en la terminal.

Ejemplo:
```
Ingrese la operación (sumar, restar, multiplicar, dividir, potencia, raiz) o 'salir' para terminar: sumar
Ingrese los números separados por espacio: 10 5
Resultado de sumar([10.0, 5.0]): 15.0
```

Ejemplo de **potencia**:
```
Ingrese la operación (sumar, restar, multiplicar, dividir, potencia, raiz) o 'salir' para terminar: potencia
Ingrese la base y el exponente separados por espacio (ejemplo: 2 3 para 2^3): 2 3
Resultado de potencia([2.0, 3.0]): 8.0
```

Ejemplo de **raíz**:
```
Ingrese la operación (sumar, restar, multiplicar, dividir, potencia, raiz) o 'salir' para terminar: raiz
Ingrese el radicando y el índice separados por espacio (ejemplo: 25 2 para raíz cuadrada de 25): 25 2
Resultado de raiz([25.0, 2.0]): 5.0
```

---

## **Tolerancia a Fallos**
- Si un servidor falla (`servidor_aritmetico.py` o `servidor_avanzado.py`), el **servidor auxiliar** (`servidor_auxiliar.py`) **asumirá sus funciones** automáticamente.
- El **servidor de cálculo** detectará fallos y redirigirá las operaciones al **servidor auxiliar**.
- Una vez que un servidor principal se recupere, el sistema **vuelve a la normalidad**.

---

## 📎 **Referencias**
- [gRPC Python Documentation](https://grpc.io/docs/languages/python/)
- [Protocol Buffers Documentation](https://developers.google.com/protocol-buffers/)

---

