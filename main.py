import random

print("🤖 IA SUPER PRO iniciada")
nom = input("Com et dius? ")

# emocions
respostes = {
    "felic": ["Que bé! 😄", "M'encanta!", "Segueix així!"],
    "trist": ["Ho sento 😢", "Ànims!", "Tot passarà ❤️"],
    "trista": ["Ho sento 😢", "Ànims!", "Tot passarà ❤️"],
    "enfadat": ["Respira 😤", "Calma"],
    "enfadada": ["Respira 😤", "Calma"],
    "cansat": ["Descansa 😴"],
    "cansada": ["Descansa 😴"],
    "estressat": ["Relaxa't 🧘"],
    "estressada": ["Relaxa't 🧘"],
    "avorrit": ["Fes algo divertit 😄"],
    "avorrida": ["Fes algo divertit 😄"],
    "nervios": ["Tranquil 😌"],
    "nerviosa": ["Tranquil 😌"],
    "emocionat": ["Que guai! 🎉"],
    "emocionada": ["Que guai! 🎉"],
    "sol": ["No estàs sol ❤️"],
    "sola": ["No estàs sol ❤️"],
    "confos": ["És normal 🤔"],
    "confosa": ["És normal 🤔"]
}

# memòria
def guardar(text):
    with open("memoria.txt", "a") as f:
        f.write(text + "\n")

# estadístiques
def comptar_emocions():
    comptador = {}
    try:
        with open("memoria.txt", "r") as f:
            for linia in f:
                for emocio in respostes:
                    if emocio in linia:
                        comptador[emocio] = comptador.get(emocio, 0) + 1
    except:
        pass
    return comptador

# mini joc
def joc():
    numero = random.randint(1, 5)
    intent = int(input("Endevina número (1-5): "))
    if intent == numero:
        print("🎉 Has guanyat!")
    else:
        print("😢 Has perdut, era", numero)

print("\nComandes: historial | stats | joc | adeu\n")

while True:
    text = input(f"{nom}: ").lower()

    guardar(nom + ": " + text)

    if text == "adeu":
        print("IA: Adeu! 👋")
        guardar("IA: Adeu!")
        break

    elif text == "historial":
        print("\n--- HISTORIAL ---")
        try:
            with open("memoria.txt", "r") as f:
                print(f.read())
        except:
            print("No hi ha dades")
        continue

    elif text == "stats":
        print("\n--- ESTADÍSTIQUES ---")
        stats = comptar_emocions()
        for e in stats:
            print(e, ":", stats[e])
        continue

    elif text == "joc":
        joc()
        continue

    elif text.startswith("aprendre "):
        nova = text.replace("aprendre ", "")
        respostes[nova] = ["Interessant 😄"]
        print("IA: He après una nova emoció!")
        continue

    elif "hola" in text:
        resposta = f"Hola {nom} 😄"

    elif "qui ets" in text:
        resposta = "Soc la teva IA SUPER PRO 🤖"

    else:
        resposta = None

        for clau in respostes:
            if clau in text:
                resposta = random.choice(respostes[clau])
                break

        if resposta is None:
            resposta = random.choice([
                "Interessant 🤔",
                "Explica'm més",
                "Entenc 😌",
                "Segueixo escoltant"
            ])

    print("IA:", resposta)
    guardar("IA: " + resposta)
