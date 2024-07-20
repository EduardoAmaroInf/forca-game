def ler_palavra_secreta(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
      palavra = arquivo.readline().strip().lower()
  return palavra

def desenhar_forca(erros):
  partes_forca = [
      '''
         +---+
             |
             |
             |
            ===
      ''',
      '''
         +---+
         O   |
             |
             |
            ===
      ''',
      '''
         +---+
         O   |
         |   |
             |
            ===
      ''',
      '''
         +---+
         O   |
        /|   |
             |
            ===
      ''',
      '''
         +---+
         O   |
        /|\\  |
             |
            ===
      ''',
      '''
         +---+
         O   |
        /|\\  |
        /    |
            ===
      ''',
      '''
         +---+
         O   |
        /|\\  |
        / \\  |
            ===
      '''
  ]
  return partes_forca[erros]

def exibir_progresso(palavra_secreta, letras_corretas):
  progresso = ''
  for letra in palavra_secreta:
      if letra in letras_corretas:
          progresso += letra
      else:
          progresso += '_'
  return progresso

def main():
    nome_arquivo = 'word.txt'
    palavra_secreta = ler_palavra_secreta(nome_arquivo)
    letras_corretas = set()
    letras_erradas = set()
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao jogo da forca!")
    print(desenhar_forca(tentativas))

    while tentativas < tentativas_maximas:
        print("\nProgresso:", exibir_progresso(palavra_secreta, letras_corretas))
        print("Letras erradas:", ' '.join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.add(letra)
            if len(letras_corretas) == len(set(palavra_secreta)):
                print("\nParabéns! Você ganhou! A palavra era:", palavra_secreta)
                return
        else:
            letras_erradas.add(letra)
            tentativas += 1
            print("Letra incorreta! Restam", tentativas_maximas - tentativas, "tentativas.")
            print(desenhar_forca(tentativas))

    print("\nVocê perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    main()
