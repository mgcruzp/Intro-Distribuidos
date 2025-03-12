import grpc
import calculadora_pb2
import calculadora_pb2_grpc

def run():
    canal = grpc.insecure_channel('localhost:50050') 
    stub = calculadora_pb2_grpc.ServidorCalculoStub(canal)

    while True:
        operacion = input("\nIngrese la operación (sumar, restar, multiplicar, dividir, potencia, raiz) o 'salir' para terminar: ").strip().lower()
        if operacion == "salir":
            print("Saliendo del cliente...")
            break

        try:
            operandos = list(map(float, input("Ingrese los números separados por espacio: ").split()))
            response = stub.DelegarOperacion(calculadora_pb2.Operacion(operacion=operacion, operandos=operandos))
            print(f"Resultado de {operacion}({operandos}): {response.resultado}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    run()
