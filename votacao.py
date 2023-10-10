# Função para registrar os votos em um arquivo de texto
def registrar_votos():
    with open('votos.txt', 'a') as arquivo:
        for _ in range(5):
            voto = input("Digite o código do candidato (1 - Bart, 2 - Homer, 0 - nulo): ")
            arquivo.write(voto + '\n')

# Função para calcular os resultados
def calcular_resultados():
    votos = []
    with open('votos.txt', 'r') as arquivo:
        for linha in arquivo:
            votos.append(int(linha.strip()))

    total_votos = len(votos)
    votos_bart = votos.count(1)
    votos_homer = votos.count(2)
    votos_nulos = total_votos - votos_bart - votos_homer

    return {
        'Bart': votos_bart,
        'Homer': votos_homer,
        'Nulos': votos_nulos
    }

# Função para encontrar o candidato mais votado e menos votado
def encontrar_vencedor_e_perdedor(resultados):
    vencedor = max(resultados, key=resultados.get)
    perdedor = min(resultados, key=resultados.get)
    return vencedor, resultados[vencedor], perdedor, resultados[perdedor]

# Função principal
def main():
    registrar_votos()
    resultados = calcular_resultados()
    vencedor, votos_vencedor, perdedor, votos_perdedor = encontrar_vencedor_e_perdedor(resultados)

    print(f"Resultado da votação:")
    print(f"Candidato mais votado: {vencedor} com {votos_vencedor} votos")
    print(f"Candidato menos votado: {perdedor} com {votos_perdedor} votos")
    print(f"Votos nulos: {resultados['Nulos']}")

if __name__ == "__main__":
    main()