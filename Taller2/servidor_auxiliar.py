import grpc
from concurrent import futures
import time
import math
import calculadora_pb2
import calculadora_pb2_grpc

class ServidorAuxiliarServicer(calculadora_pb2_grpc.ServidorAuxiliarServicer):
    def __init__(self):
        self.servidores = {
            "aritmetico": "localhost:50051",  # IP del Servidor Aritmético
            "avanzado": "localhost:50052"  # IP del Servidor Avanzado
        }
        self.estado_servidores = {
            "aritmetico": True,
            "avanzado": True
        }

    def EjecutarOperacion(self, request, context):
        print(f"[AUXILIAR] Ejecutando operación: {request.operacion} con operandos {request.operandos}")

        try:
            if request.operacion in ["sumar", "restar", "multiplicar", "dividir"]:
                resultado = self.operaciones_aritmeticas(request.operacion, request.operandos)
            elif request.operacion in ["potencia", "raiz"]:
                resultado = self.operaciones_avanzadas(request.operacion, request.operandos)
            else:
                return calculadora_pb2.Resultado(resultado=float('nan'))

            return calculadora_pb2.Resultado(resultado=resultado)

        except Exception as e:
            print(f"[AUXILIAR] Error en la operación: {e}")
            return calculadora_pb2.Resultado(resultado=float('nan'))

    def NotificarEstado(self, request, context):
        self.estado_servidores[request.servidor] = request.activo
        estado = "ACTIVO" if request.activo else "INACTIVO"
        print(f"[AUXILIAR] Estado actualizado: Servidor {request.servidor} está {estado}")
        return calculadora_pb2.Ack(mensaje="Estado actualizado correctamente")

    def operaciones_aritmeticas(self, operacion, operandos):
        if operacion == "sumar":
            return sum(operandos)
        elif operacion == "restar":
            return operandos[0] - sum(operandos[1:])
        elif operacion == "multiplicar":
            resultado = 1
            for num in operandos:
                resultado *= num
            return resultado
        elif operacion == "dividir":
            return operandos[0] / operandos[1] if operandos[1] != 0 else float('inf')

    def operaciones_avanzadas(self, operacion, operandos):
        if operacion == "potencia":
            return math.pow(operandos[0], operandos[1])
        elif operacion == "raiz":
            return math.pow(operandos[0], 1 / operandos[1])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_ServidorAuxiliarServicer_to_server(ServidorAuxiliarServicer(), server)
    server.add_insecure_port('[::]:50053')  # Puerto para el servidor auxiliar
    server.start()
    print("[AUXILIAR] Servidor auxiliar en ejecución en el puerto 50053")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()