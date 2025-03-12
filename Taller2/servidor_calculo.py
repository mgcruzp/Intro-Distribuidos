import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc

class ServidorCalculoServicer(calculadora_pb2_grpc.ServidorCalculoServicer):
    def DelegarOperacion(self, request, context):
        print(f"Recibida operación: {request.operacion} con operandos {request.operandos}")

        # Redirigir a servidores correspondientes
        if request.operacion in ["sumar", "restar", "multiplicar", "dividir"]:
            canal = grpc.insecure_channel('localhost:50051')
            stub = calculadora_pb2_grpc.ServidorAritmeticoStub(canal)
        elif request.operacion in ["potencia", "raiz"]:
            canal = grpc.insecure_channel('localhost:50052')
            stub = calculadora_pb2_grpc.ServidorAvanzadoStub(canal)
        else:
            return calculadora_pb2.Resultado(resultado=float('nan'))

        # Ejecutar la operación correspondiente
        metodo = getattr(stub, request.operacion.capitalize(), None)
        if metodo:
            return metodo(request)
        else:
            return calculadora_pb2.Resultado(resultado=float('nan'))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_ServidorCalculoServicer_to_server(ServidorCalculoServicer(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    print("Servidor de cálculo en ejecución en el puerto 50050")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
