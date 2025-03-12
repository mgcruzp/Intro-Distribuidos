import grpc
from concurrent import futures
import math
import calculadora_pb2
import calculadora_pb2_grpc

class ServidorAvanzadoServicer(calculadora_pb2_grpc.ServidorAvanzadoServicer):
    def Potencia(self, request, context):
        return calculadora_pb2.Resultado(resultado=math.pow(request.operandos[0], request.operandos[1]))

    def RaizCuadrada(self, request, context):
        return calculadora_pb2.Resultado(resultado=math.sqrt(request.operandos[0]))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_ServidorAvanzadoServicer_to_server(ServidorAvanzadoServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Servidor avanzado en el puerto 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
