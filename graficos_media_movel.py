import matplotlib.pyplot as plt

posicoes = []

while True:
    entrada = input()
    if entrada == "0":
        break
    a, b = entrada.split(".")
    c, d = b.split("E")

    posicao = round(float(str(a) + str(".") + str(c)) * 10 ** (int(d)), 5)
    posicoes.append(posicao)

numero_de_pontos = len(posicoes)
tempo = float(input("Tempo: "))


def obter_media(conjunto, passo):
    global tempo
    saida = []

    for i in range(len(conjunto)):
        if i >= passo:
            soma = 0
            for k in range(passo):
                soma += conjunto[i - k]
            saida.append(round(soma / passo, 5))
    return saida


posicoes_media = obter_media(posicoes, 10)


def fazer_grafico(conjuntos, t):
    lista_graficos = []
    for conj in conjuntos:
        lista_pontos = []
        for i in range(len(conj[0])):
            x, y = t * i / len(conj[0]), conj[0][i]
            lista_pontos.append((x, y))

        xs, ys = zip(*lista_pontos)
        lista_graficos.append((xs, ys, conj[1], conj[2]))

    for k in lista_graficos:
        plt.scatter(k[0], k[1], s=5, color=k[2], label=k[3])
        plt.plot(k[0], k[1], linestyle="dashed", color=k[2], alpha=0.6)

    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m), Velocidade(m/s) e Aceleração(m/s^2)")
    plt.legend()
    plt.grid(True)
    plt.show()


def obter_derivada(conjunto, t):
    derivada = []
    for i in range(len(conjunto) - 1):
        t1 = t * i / len(conjunto)
        t2 = t * (i + 1) / len(conjunto)
        f1 = conjunto[i]
        f2 = conjunto[i + 1]
        v = (f2 - f1) / (t2 - t1)
        derivada.append(v)
    return derivada


velocidade = obter_derivada(posicoes_media, tempo)
velocidade = obter_media(velocidade, 5)
aceleracao = obter_derivada(velocidade, tempo)
aceleracao = obter_media(aceleracao, 20)
fazer_grafico(
    [
        [posicoes_media, "red", "Posição (m)"],
        [velocidade, "blue", "Velocidade (m/s)"],
        [aceleracao, "black", "Acelerração (m/s2)"],
    ],
    tempo,
)
