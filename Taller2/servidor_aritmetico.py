import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc

class ServidorAritmeticoServicer(calculadora_pb2_grpc.ServidorAritmeticoServicer):
    def Sumar(self, request, context):
        return calculadora_pb2.Resultado(resultado=sum(request.operandos))

    def Restar(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.operandos[0] - sum(request.operandos[1:]))

    def Multiplicar(self, request, context):
        resultado = 1
        for num in request.operandos:
            resultado *= num
        return calculadora_pb2.Resultado(resultado=resultado)

    def Dividir(self, request, context):
        if request.operandos[1] == 0:
            return calculadora_pb2.Resultado(resultado=float('inf'))
        return calculadora_pb2.Resultado(resultado=request.operandos[0] / request.operandos[1])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_ServidorAritmeticoServicer_to_server(ServidorAritmeticoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor aritmético en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
