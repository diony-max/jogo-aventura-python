import time
import random

def pausa():
    time.sleep(1)

def introducao():
    print("=" * 40)
    print(" BEM-VINDO À AVENTURA DOS NÍVEIS ")
    print("=" * 40)
    print("Você deve vencer desafios para avançar.")
    print("Boa sorte!\n")
    pausa()

def fase(numero, desafio):
    print(f"\n--- FASE {numero} ---")
    print(desafio)
    resposta = input("Digite sua escolha: ").lower()

    sucesso = random.choice([True, False])

    if sucesso:
        print("✅ Você venceu o desafio!")
        return True
    else:
        print("❌ Você falhou no desafio!")
        return False

def jogar():
    vidas = 3
    pontos = 0

    introducao()

    fases = [
        "Você encontrou uma porta misteriosa. Abrir ou voltar?",
        "Um inimigo apareceu. Lutar ou fugir?",
        "Um baú está no caminho. Abrir ou ignorar?"
    ]

    for i, desafio in enumerate(fases, start=1):
        venceu = fase(i, desafio)

        if venceu:
            pontos += 10
        else:
            vidas -= 1
            print(f"Vidas restantes: {vidas}")
            if vidas == 0:
                print("\n💀 GAME OVER 💀")
                print(f"Pontuação final: {pontos}")
                return

        pausa()

    print("\n🎉 PARABÉNS! VOCÊ FINALIZOU O JOGO 🎉")
    print(f"Pontuação final: {pontos}")

jogar()
