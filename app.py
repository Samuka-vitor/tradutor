# pyinstaller --onefile app.py #tem que ser o nome do arquivo

from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= "auto", target="pt")

if __name__ == "__main__":
    while True: 
        try:
           print("1 - traduzir texto.")
           print("2 - sair do programa.")

           opcao = input("Opção desejada: ")

           match opcao:
                case "1":
                   texto_original = input("Digite o texto a ser traduzido: ")
                   texto_traduzido = tradutor.translate(texto_original)
                   print("Texto traduzido")
                   print(f"\n{texto_traduzido}\n")
                   continue
               
                case "2":
                    break
               
                case _:
                    print("Opção inválida")     

        except Exception as e:
            print (f"Não foi possível traduzir o texto")
            continue

