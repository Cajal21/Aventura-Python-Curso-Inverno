import random
import os

def igreja():
    print(f"                                      .                                  ")
    print(f"                                    .' '.                                ")
    print(f"                                  .'  |  `.                              ")
    print(f"                                .'    |    `.                            ")
    print(f"                              .`---.._|_..---'.                          ")
    print(f"                               ||    |=|    ||                           ")
    print(f"                               ||_.-'|=|`-._||                           ")
    print(f"                               ||`-._|=|_.-'||                           ")
    print(f"                          _____||    |=|    ||__                         ")
    print(f"            ____________.'     `-.   |=|  .'_.'\/`.                      ")
    print(f"          .'       _  .' _______  `-.|_|.' .'\.'`./`.                    ")
    print(f"        .'     _   _.'      _   _        .'\.' `._`./`.                  ")
    print(f"      .' _       _.' __          __    .'\.'  ___`._`./`.                ")
    print(f"    .'        _ .'   _____           .'\.'         `._`./`.              ")
    print(f"  .'  _  _    .'       ______      .'\.'  __         `._`./`.            ")
    print(f".'`--...__ _.'            ______ .'\.'           __    `._`./`.          ")
    print(f" `--...__ .'   ____            .'\.'           _         `._`./`.        ")
    print(f" |      .`--...__            .'\.'     _               ____`._`./`.      ")
    print(f" | /`-._ `--...__`--...___ .'\.'              _______       _`._`./`.    ")
    print(f" | | ) ( |       `--...____\.'     _     _  .'      .`.        `._`./    ")
    print(f" | |)   (| /`-._             |            .'      .'   `.     _ |        ")
    print(f" | |(--| | | )( |  /`-._`--._|____       /      .'       `.     |        ")
    print(f" | | ) `.| |(  )|  | )( |    | _      _ /      /   .---.  `\    |        ")
    print(f" | `--._ | |/  \|  |(  )|`-  |         /`--.._/   /     \  ' _  |        ")
    print(f" | `-.   | |)-.(|  |/  \|    |       __|      |_  |`-   |  |  _ |        ")
    print(f" |    `-.| |) |(|  |)-.(|    |  ___  _ |  __  | __| \`- |  |    |        ")
    print(f" '-._    | `--._/  |) |(|    |      __ |      |   | |`- |  | _  |        ")
    print(f"     `-._| `--.    `--._/    |  ___    | _    |   | |`- |  |   '|        ")
    print(f"         |      `--._        |       _ |    ' |   |O|`- | _| _  |        ")
    print(f"         '--._         `--._ |         | _    |_  | |`- |. |  __|        ")
    print(f"              `--._          |       __|      |   | |`- |. | __ |        ")
    print(f"                   `--._     |__       |   _  |   | |`- |  |___ |        ") 
    print(f"                        `--._|_________|_     | _ |  `- |_ |____|        ")
    print(f"                               LG        '--._|___|     |__|             ") 

def funcaux():
    print("vish")
def boss_ambientacao():
    escolha = 1
    nome = funcaux
    os.system("cls")
    print(f"O guerreiro nome ouve uma badalada de um sino ao horizonte.")
    print(f"O que nome deveria fazer?")
    print(f"[1] Seguir o som do sino")
    print(f"[2] Seguir na direção oposta do sino")
    escolha = input()
    if escolha == '2':
        print("Você acaba indo na direção oposta, mas chega no sino de qualquer jeito, que sorte!...")
    print("Ao chegar, o guerreiro se depara com uma pequena igreja...\n\n")
    input("Pressione para continuar...")
    igreja()

boss_ambientacao()
  
