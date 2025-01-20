class Resposta:
    def __init__(self, resposta_correta):
        self.resposta_correta = resposta_correta

    def verificar_resposta(self, escolha):
        if escolha.upper() not in ["A", "B", "C", "D", "E"]:
            print("Resposta inválida. Responda com (A), (B), (C), (D) ou (E).")
            return 
        elif escolha.upper() == self.resposta_correta.upper():
            print("Sua resposta está correta!")
            return True
        else:
            print("Sua resposta está incorreta!")
            return False


perguntas = [
    {
        'Pergunta': 'Em que lugar vivem mais cangurus do que pessoas?',
        'Opções': ["(A) Indonésia", "(B) Nova Zelândia", "(C) Austrália", "(D) Nova Guiné", "(E) África do Sul"],
        'Resposta': "C",
    },
    {
        'Pergunta': 'Quanto mede uma girafa?',
        'Opções': ["(A) Entre 5 e 6 metros", "(B) Entre 2 e 3 metros", "(C) Entre 1 e 2 metros", "(D) Entre 0 e 1 metros", "(E)Entre 4 e 5 metros"],
        'Resposta': "A",
    },
    {
        'Pergunta': 'De que são constituídos os diamantes?',
        'Opções': ["(A) Grafite", "(B) Carbono", "(C) Cobre", "(D) Titaneo","(E) Estanho"],
        'Resposta': "B",
    },
]

qtd_acertos = 0
print("BEM VINDO AO QUIZ")
answer_user = input("Quer começar? (S/N) ").strip().upper()

if answer_user != "S":
    quit()

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta["Opções"]
    for opcao in opcoes:
        print(opcao)
    print()

    escolha = input("Escolha uma opção: ").strip().upper()
    resposta = Resposta(pergunta['Resposta'])

    if resposta.verificar_resposta(escolha):
        qtd_acertos += 1

print(f"\nVocê acertou {qtd_acertos}/{len(perguntas)} perguntas.")
print("Quiz encerrado!")