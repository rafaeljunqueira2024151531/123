import socket
import json
import threading
import inspect
import primos
import game_of_life

FUNCOES_REMOTAS = {
    "find_max_prime": primos.find_max_prime_parallel,
    "is_prime": primos.is_prime,
    "game_of_life": game_of_life.game_of_life_parallel,
}

def list_methods():
    """Retorna a lista de operações disponíveis no servidor."""
    metodos = []
    for nome, func in FUNCOES_REMOTAS.items():
        sig = inspect.signature(func)
        metodos.append({
            "nome": nome,
            "parametros": str(sig),
            "descricao": func.__doc__.strip() if func.__doc__ else "Sem descrição."
        })
    metodos.append({
        "nome": "list_methods",
        "parametros": "()",
        "descricao": "Lista todas as operações disponíveis no servidor."
    })
    return metodos

def lidar_com_cliente(conn, addr):
    """Gere a comunicação com um cliente específico."""
    print(f"[CONEXÃO] {addr}")
    try:
        data = conn.recv(1024 * 1024)
        if not data:
            return

        pedido = json.loads(data.decode('utf-8'))
        metodo_nome = pedido.get("method")
        params = pedido.get("params", {})

        if metodo_nome == "list_methods":
            resultado = list_methods()
            resposta = {"result": resultado}
        elif metodo_nome in FUNCOES_REMOTAS:
            try:
                func = FUNCOES_REMOTAS[metodo_nome]
                if isinstance(params, list):
                    resultado = func(*params)
                else:
                    resultado = func(**params)
                resposta = {"result": resultado}
            except Exception as e:
                resposta = {"error": f"Erro na execução: {str(e)}"}
        else:
            resposta = {"error": "Método não encontrado."}

    except json.JSONDecodeError:
        resposta = {"error": "Formato JSON inválido."}
    except Exception as e:
        resposta = {"error": f"Erro interno: {str(e)}"}
    finally:
        conn.sendall(json.dumps(resposta).encode('utf-8'))
        conn.close()

def iniciar_servidor(host='127.0.0.1', port=65432):
    """Inicia o socket TCP e escuta novas conexões."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, port))
        servidor.listen()
        print(f"[ON] Servidor RPC em {host}:{port}")

        while True:
            conn, addr = servidor.accept()
            thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    iniciar_servidor()