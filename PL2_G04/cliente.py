import socket
import json
import ast


class ClienteRPC:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port

    def invocar_remoto(self, metodo, params={}):
        """Envia um pedido JSON-RPC ao servidor e processa a resposta."""
        pedido = {
            "method": metodo,
            "params": params
        }

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(json.dumps(pedido).encode('utf-8'))

                dados = s.recv(1024 * 1024)
                if not dados:
                    return {"error": "Sem resposta do servidor."}

                return json.loads(dados.decode('utf-8'))
        except ConnectionRefusedError:
            return {"error": "Servidor não encontrado. Certifique-se que o servidor.py está a correr."}
        except Exception as e:
            return {"error": str(e)}


def menu():
    """Interface de utilizador para interagir com o servidor RPC."""
    cliente = ClienteRPC()

    while True:
        print("\n--- MENU COMPUTAÇÃO PARALELA E DISTRIBUÍDA ---")
        print("1. Listar Operações Disponíveis")
        print("2. Verificar Primalidade")
        print("3. Procurar Maior Primo em Tempo Limitado")
        print("4. Simular Game of Life")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        elif opcao == "1":
            resposta = cliente.invocar_remoto("list_methods")
            if "result" in resposta:
                print("\nMétodos no servidor:")
                for m in resposta["result"]:
                    print(f"- {m['nome']}{m['parametros']}: {m['descricao']}")
            else:
                print("Erro:", resposta.get("error"))

        elif opcao == "2":
            n = int(input("Número (n): "))
            resposta = cliente.invocar_remoto("is_prime", {"n": n})
            print("Resultado:", "É Primo" if resposta.get("result") else "Não é Primo")

        elif opcao == "3":
            t = int(input("Tempo (segundos): "))
            w = int(input("Workers: "))
            print("A processar...")
            resposta = cliente.invocar_remoto("find_max_prime", {"timeout": t, "workers": w})
            print("Maior primo:", resposta.get("result"))

        elif opcao == "4":
            print("Introduza a grelha (ex: [[0,1,0],[0,0,1],[1,1,1]]):")
            grelha_str = input("> ")
            try:
                grelha = ast.literal_eval(grelha_str)
                gen = int(input("Gerações: "))
                w = int(input("Workers: "))

                print("A simular...")
                resposta = cliente.invocar_remoto("game_of_life", {
                    "grid": grelha,
                    "generations": gen,
                    "workers": w
                })

                if "result" in resposta:
                    print("Grelha Final:")
                    for linha in resposta["result"]:
                        print(linha)
                else:
                    print("Erro:", resposta.get("error"))
            except:
                print("Erro: Formato inválido.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()