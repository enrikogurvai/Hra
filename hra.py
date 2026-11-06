import random

# --- VSTUPY PRE HRÁČOV ---
print("--- HRÁČ 1 ---")
meno_1 = input("Zadaj svoje meno (Hráč 1): ")
trieda_vyber_1 = int(input("Zadaj číslo pre výber svojej triedy - 1. Paladin | 2. Shadow | 3. Knight | 4. Mafian Boss | 5. Mage | 6. Detective: "))
rasa_vyber_1 = int(input("Zadaj číslo pre výber svojej rasy - 1. Strongman | 2. Robot | 3. Upír: "))

print("\n" + "="*50 + "\n")

print("--- HRÁČ 2 ---")
meno_2 = input("Zadaj svoje meno (Hráč 2): ")
trieda_vyber_2 = int(input("Zadaj číslo pre výber svojej triedy - 1. Paladin | 2. Shadow | 3. Knight | 4. Mafian Boss | 5. Mage | 6. Detective: "))
rasa_vyber_2 = int(input("Zadaj číslo pre výber svojej rasy - 1. Strongman | 2. Robot | 3. Upír: "))

# Funkcia na výpočet reálneho damage s ohľadom na armor (10 armor = 10% resist)
def aplikuj_armor(raw_dmg, defender_armor):
    realdmg = raw_dmg * (1 - (defender_armor / 100))
    return round(max(0.0, realdmg), 2)

# Funkcia na nastavenie triedy
def nastav_triedu(cislo_triedy):
    if cislo_triedy == 1: return "Paladin", 7, 120, 50, 17
    elif cislo_triedy == 2: return "Shadow", 15, 90, 50, 12
    elif cislo_triedy == 3: return "Knight", 12, 100, 35, 17
    elif cislo_triedy == 4: return "Mafian Boss", 15, 100, 30, 10
    elif cislo_triedy == 5: return "Mage", 2, 85, 75, 7
    elif cislo_triedy == 6: return "Detective", 15, 100, 35, 10
    else: return "Paladin", 7, 120, 50, 15

# Funkcia na nastavenie rasy
def nastav_rasu(dmg, hp, arm, cislo_rasy):
    if cislo_rasy == 1: dmg *= 1.10; hp *= 1.05
    elif cislo_rasy == 2: dmg *= 1.15; hp *= 0.9; arm *= 1.25
    elif cislo_rasy == 3: dmg *= 1.20; hp *= 1.10; arm *= 0.85
    return round(dmg, 2), round(hp, 2), round(arm, 2)

# Inicializácia Hráča 1
t1, dmg1, hp1, mana1, arm1 = nastav_triedu(trieda_vyber_1)
dmg1, hp1, arm1 = nastav_rasu(dmg1, hp1, arm1, rasa_vyber_1)
hrac_1 = {"meno": meno_1, "trieda": t1, "hp": hp1, "mana": mana1, "armor": arm1, "damage": dmg1, "stun": False}

# Inicializácia Hráča 2
t2, dmg2, hp2, mana2, arm2 = nastav_triedu(trieda_vyber_2)
dmg2, hp2, arm2 = nastav_rasu(dmg2, hp2, arm2, rasa_vyber_2)
hrac_2 = {"meno": meno_2, "trieda": t2, "hp": hp2, "mana": mana2, "armor": arm2, "damage": dmg2, "stun": False}

print("\n" + "="*50)
print(f"Hráč 1: {hrac_1['meno']} ({hrac_1['trieda']}) | HP: {hrac_1['hp']} | Mana: {hrac_1['mana']} | Armor: {hrac_1['armor']}")
print(f"Hráč 2: {hrac_2['meno']} ({hrac_2['trieda']}) | HP: {hrac_2['hp']} | Mana: {hrac_2['mana']} | Armor: {hrac_2['armor']}")
print("="*50 + "\n")


# ==========================================
# 🔮 JEDNOTLIVÉ SPELLY (Pôvodné názvy, doplnené 5 akcií: Útok, Regen Many, Regen HP, Stun, Ultimátka)
# ==========================================

# --- PALADIN ---
def spelly_paladin(akcia, utocnik, obranec):
    if akcia == 1: # Divine Strike (Základný útok - Mana: 0)
        dmg = aplikuj_armor(10, obranec["armor"])
        obranec["hp"] -= dmg
        print(f"-> Divine Strike: Zostrelil {dmg} HP! (Mana: 0)")
        return True
    elif akcia == 2: # Divine Shield -> Upravené na Regen Many (Mana: 0)
        utocnik["mana"] += 25
        print("-> Divine Shield (Regen Many): Získal si 25 many! (Mana +25)")
        return True
    elif akcia == 3: # Sacred Grace (Regen HP - Mana: 15)
        if utocnik["mana"] >= 15:
            utocnik["hp"] += 25
            utocnik["mana"] -= 15
            print("-> Sacred Grace: Vyliečil si 25 HP! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 4: # Celestial Judgment (Stun - Mana: 15)
        if utocnik["mana"] >= 15:
            dmg = aplikuj_armor(8, obranec["armor"])
            obranec["hp"] -= dmg
            obranec["stun"] = True
            utocnik["mana"] -= 15
            print(f"-> Celestial Judgment: {dmg} damage a STUN pre súpera! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 5: # NOVÁ ULTIMÁTKA (Veľký damage + Armor buff pre tanka - Mana: 25)
        if utocnik["mana"] >= 25:
            dmg = aplikuj_armor(45, obranec["armor"])
            obranec["hp"] -= dmg
            utocnik["armor"] += 5
            utocnik["mana"] -= 25
            print(f"-> Svätý Hnev (Ulti): Masívnych {dmg} damage a +5 Armor! (Mana -25)")
            return True
        print("❌ Nedostatok many!")
    return False

# --- SHADOW ---
def spelly_shadow(akcia, utocnik, obranec):
    if akcia == 1: # Shadow Strike (Základný útok - Mana: 0)
        dmg = aplikuj_armor(12, obranec["armor"])
        obranec["hp"] -= dmg
        print(f"-> Shadow Strike: Zostrelil {dmg} HP! (Mana: 0)")
        return True
    elif akcia == 2: # Teleport -> Upravené na Regen Many (Mana: 0)
        utocnik["mana"] += 25
        print("-> Teleport (Regen Many): Načerpal si tieňovú energiu (+25 many)!")
        return True
    elif akcia == 3: # Black Smoke -> Upravené na Regen HP (Mana: 15)
        if utocnik["mana"] >= 15:
            utocnik["hp"] += 25
            utocnik["mana"] -= 15
            print("-> Black Smoke (Regen HP): Vyliečil si 25 HP! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 4: # Backstab -> Upravené na Stun (Mana: 15)
        if utocnik["mana"] >= 15:
            dmg = aplikuj_armor(10, obranec["armor"])
            obranec["hp"] -= dmg
            obranec["stun"] = True
            utocnik["mana"] -= 15
            print(f"-> Backstab (Stun): {dmg} damage a omráčil súpera! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 5: # NOVÁ ULTIMÁTKA (Veľký damage - Mana: 30)
        if utocnik["mana"] >= 30:
            dmg = aplikuj_armor(50, obranec["armor"])
            obranec["hp"] -= dmg
            utocnik["mana"] -= 30
            print(f"-> Tieňová Smrť (Ulti): Masívnych {dmg} damage zo zálohy! (Mana -30)")
            return True
        print("❌ Nedostatok many!")
    return False

# --- KNIGHT ---
def spelly_knight(akcia, utocnik, obranec):
    if akcia == 1: # Bloodlust (Základný útok - Mana: 0)
        dmg = aplikuj_armor(11, obranec["armor"])
        obranec["hp"] -= dmg
        print(f"-> Bloodlust: Zostrelil {dmg} HP! (Mana: 0)")
        return True
    elif akcia == 2: # Ironclad Defense -> Upravené na Regen Many (Mana: 0)
        utocnik["mana"] += 25
        print("-> Ironclad Defense (Regen Many): Získal si 25 many! (Mana +25)")
        return True
    elif akcia == 3: # Undying Warrior (Regen HP - Mana: 15)
        if utocnik["mana"] >= 15:
            utocnik["hp"] += 25
            utocnik["mana"] -= 15
            print("-> Undying Warrior: Vyliečil si 25 HP! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 4: # Blinding Steel (Stun - Mana: 15)
        if utocnik["mana"] >= 15:
            dmg = aplikuj_armor(8, obranec["armor"])
            obranec["hp"] -= dmg
            obranec["stun"] = True
            utocnik["mana"] -= 15
            print(f"-> Blinding Steel: {dmg} damage a OMRÁČENIE súpera! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 5: # NOVÁ ULTIMÁTKA (Veľký damage + Armor buff pre tanka - Mana: 25)
        if utocnik["mana"] >= 25:
            dmg = aplikuj_armor(45, obranec["armor"])
            obranec["hp"] -= dmg
            utocnik["armor"] += 6
            utocnik["mana"] -= 25
            print(f"-> Rytierska Pýcha (Ulti): Zasadil {dmg} damage a získal +6 Armor! (Mana -25)")
            return True
        print("❌ Nedostatok many!")
    return False

# --- MAFIAN BOSS ---
def spelly_mafian(akcia, utocnik, obranec):
    if akcia == 1: # Čokoládova férovka (Základný útok - Mana: 0)
        dmg = aplikuj_armor(utocnik["damage"], obranec["armor"])
        obranec["hp"] -= dmg
        print(f"-> Čokoládova férovka: Urobil {dmg} damage! (Mana: 0)")
        return True
    elif akcia == 2: # CLS320CDi -> Upravené na Regen Many (Mana: 0)
        utocnik["mana"] += 25
        print("-> CLS320CDi (Regen Many): Natankovaný plný plyn a +25 many!")
        return True
    elif akcia == 3: # Kotlár (Regen HP - Mana: 15)
        if utocnik["mana"] >= 15:
            utocnik["hp"] += 25
            utocnik["mana"] -= 15
            print("-> Kotlár: Vyliečil si 25 HP! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 4: # CLS320CDi / Debuff -> Upravené na Stun (Mana: 15)
        if utocnik["mana"] >= 15:
            dmg = aplikuj_armor(10, obranec["armor"])
            obranec["hp"] -= dmg
            obranec["stun"] = True
            utocnik["mana"] -= 15
            print(f"-> Mafian Stun: {dmg} damage a omráčil súpera! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 5: # Bakhtalo Špeciál (Ultimátka - Mana: 30)
        if utocnik["mana"] >= 30:
            dmg = aplikuj_armor(50, obranec["armor"])
            obranec["hp"] -= dmg
            utocnik["mana"] -= 30
            print(f"-> Bakhtalo Špeciál (Ulti): Masívnych {dmg} damage! (Mana -30)")
            return True
        print("❌ Nedostatok many!")
    return False

# --- MAGE ---
def spelly_mage(akcia, utocnik, obranec):
    if akcia == 1: # Lightning Strike (Základný útok - Mana: 0)
        dmg = aplikuj_armor(12, obranec["armor"])
        obranec["hp"] -= dmg
        print(f"-> Lightning Strike: Zostrelil {dmg} HP! (Mana: 0)")
        return True
    elif akcia == 2: # Mana Regen Boost (Regen Many - Mana: 0)
        utocnik["mana"] += 30
        print("-> Mana Regen Boost: Získal si späť 30 many! (Mana +30)")
        return True
    elif akcia == 3: # Arcane Heal / Pôvodný doplnok -> Upravené na Regen HP (Mana: 15)
        if utocnik["mana"] >= 15:
            utocnik["hp"] += 25
            utocnik["mana"] -= 15
            print("-> Arcane Regen (Regen HP): Vyliečil si 25 HP! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 4: # Ground Zero (Stun - Mana: 20)
        if utocnik["mana"] >= 20:
            dmg = aplikuj_armor(10, obranec["armor"])
            obranec["hp"] -= dmg
            obranec["stun"] = True
            utocnik["mana"] -= 20
            print(f"-> Ground Zero: {dmg} damage a OMRÁČENIE súpera! (Mana -20)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 5: # Obliteration (Ultimátka - Mana: 45)
        if utocnik["mana"] >= 45:
            dmg = aplikuj_armor(55, obranec["armor"])
            obranec["hp"] -= dmg
            utocnik["mana"] -= 45
            print(f"-> Obliteration (Ulti): Brutálnych {dmg} damage kúzlo! (Mana -45)")
            return True
        print("❌ Nedostatok many!")
    return False

# --- DETECTIVE ---
def spelly_detective(akcia, utocnik, obranec):
    if akcia == 1: # Pistol Attack (Základný útok - Mana: 0)
        dmg = aplikuj_armor(utocnik["damage"], obranec["armor"])
        obranec["hp"] -= dmg
        print(f"-> Pistol Attack: Urobil {dmg} damage! (Mana: 0)")
        return True
    elif akcia == 2: # Investigation -> Upravené na Regen Many (Mana: 0)
        utocnik["mana"] += 25
        print("-> Investigation (Regen Many): Našiel si stopy a získal 25 many!")
        return True
    elif akcia == 3: # Adrenaline Shot (Regen HP - Mana: 15)
        if utocnik["mana"] >= 15:
            utocnik["hp"] += 25
            utocnik["mana"] -= 15
            print("-> Adrenaline Shot: Vyliečil si 25 HP! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 4: # Handcuffs (Stun - Mana: 15)
        if utocnik["mana"] >= 15:
            dmg = aplikuj_armor(8, obranec["armor"])
            obranec["hp"] -= dmg
            obranec["stun"] = True
            utocnik["mana"] -= 15
            print(f"-> Handcuffs: {dmg} damage a nasadil putá (STUN)! (Mana -15)")
            return True
        print("❌ Nedostatok many!")
    elif akcia == 5: # Deadly Shot (Ultimátka - Mana: 30)
        if utocnik["mana"] >= 30:
            dmg = aplikuj_armor(50, obranec["armor"])
            obranec["hp"] -= dmg
            utocnik["mana"] -= 30
            print(f"-> Deadly Shot (Ulti): Presná trefa za {dmg} damage! (Mana -30)")
            return True
        print("❌ Nedostatok many!")
    return False

# Hlavná smerovacia funkcia pre spelly podľa triedy
def vykonaj_spell(trieda, akcia, utocnik, obranec):
    if trieda == "Paladin": return spelly_paladin(akcia, utocnik, obranec)
    elif trieda == "Shadow": return spelly_shadow(akcia, utocnik, obranec)
    elif trieda == "Knight": return spelly_knight(akcia, utocnik, obranec)
    elif trieda == "Mafian Boss": return spelly_mafian(akcia, utocnik, obranec)
    elif trieda == "Mage": return spelly_mage(akcia, utocnik, obranec)
    elif trieda == "Detective": return spelly_detective(akcia, utocnik, obranec)
    return False


# ==========================================
# 🎮 HLAVNÁ HERNÁ SLUČKA
# ==========================================
na_rade = random.randint(1, 2)
print(f"🎲 Losovanie: Na rade je -> {'Hráč 1 (' + hrac_1['meno'] + ')' if na_rade == 1 else 'Hráč 2 (' + hrac_2['meno'] + ')'}\n" + "-"*50)

while hrac_1["hp"] > 0 and hrac_2["hp"] > 0:
    
    # Určenie kto je útočník a kto obranec v tomto kole
    if na_rade == 1:
        utocnik, obranec = hrac_1, hrac_2
    else:
        utocnik, obranec = hrac_2, hrac_1

    # Kontrola Stunu
    if utocnik["stun"]:
        print(f"\n⚠️ {utocnik['meno']}, si OMRÁČENÝ (Stunnutý) a nemôžeš konať!")
        utocnik["stun"] = False
    else:
        while True:
            print(f"\n👉 Na rade je {utocnik['meno']} ({utocnik['trieda']}) | HP: {utocnik['hp']} | Mana: {utocnik['mana']} | Armor: {utocnik['armor']}")
            
            # Ponuka možností (5 akcií pre každú triedu so zachovanými názvami)
            if utocnik["trieda"] == "Paladin":
                akcia = int(input("Vyber akciu:\n 1. Divine Strike (0 many)\n 2. Divine Shield / Regen Many (0 many)\n 3. Sacred Grace / Regen HP (15 many)\n 4. Celestial Judgment / Stun (15 many)\n 5. Svätý Hnev / Ultimátka (25 many)\n-> Zadaj číslo (1-5): "))
            elif utocnik["trieda"] == "Shadow":
                akcia = int(input("Vyber akciu:\n 1. Shadow Strike (0 many)\n 2. Teleport / Regen Many (0 many)\n 3. Black Smoke / Regen HP (15 many)\n 4. Backstab / Stun (15 many)\n 5. Tieňová Smrť / Ultimátka (30 many)\n-> Zadaj číslo (1-5): "))
            elif utocnik["trieda"] == "Knight":
                akcia = int(input("Vyber akciu:\n 1. Bloodlust (0 many)\n 2. Ironclad Defense / Regen Many (0 many)\n 3. Undying Warrior / Regen HP (15 many)\n 4. Blinding Steel / Stun (15 many)\n 5. Rytierska Pýcha / Ultimátka (25 many)\n-> Zadaj číslo (1-5): "))
            elif utocnik["trieda"] == "Mafian Boss":
                akcia = int(input("Vyber akciu:\n 1. Čokoládova férovka (0 many)\n 2. CLS320CDi / Regen Many (0 many)\n 3. Kotlár / Regen HP (15 many)\n 4. Mafian Stun / Stun (15 many)\n 5. Bakhtalo Špeciál / Ultimátka (30 many)\n-> Zadaj číslo (1-5): "))
            elif utocnik["trieda"] == "Mage":
                akcia = int(input("Vyber akciu:\n 1. Lightning Strike (0 many)\n 2. Mana Regen Boost / Regen Many (0 many)\n 3. Arcane Regen / Regen HP (15 many)\n 4. Ground Zero / Stun (20 many)\n 5. Obliteration / Ultimátka (45 many)\n-> Zadaj číslo (1-5): "))
            elif utocnik["trieda"] == "Detective":
                akcia = int(input("Vyber akciu:\n 1. Pistol Attack (0 many)\n 2. Investigation / Regen Many (0 many)\n 3. Adrenaline Shot / Regen HP (15 many)\n 4. Handcuffs / Stun (15 many)\n 5. Deadly Shot / Ultimátka (30 many)\n-> Zadaj číslo (1-5): "))

            if 1 <= akcia <= 5:
                uspech = vykonaj_spell(utocnik["trieda"], akcia, utocnik, obranec)
                if uspech:
                    break
            else:
                print("❌ Neplatná voľba, vyber číslo od 1 do 5!")

    # Ošetrenie záporných hodnôt a zaokrúhlenie statov
    utocnik["hp"] = round(max(0.0, utocnik["hp"]), 2)
    obranec["hp"] = round(max(0.0, obranec["hp"]), 2)
    utocnik["mana"] = round(max(0.0, utocnik["mana"]), 2)

    print(f"\n📊 Stav po tvojom ťahu -> {hrac_1['meno']} HP: {hrac_1['hp']} | {hrac_2['meno']} HP: {hrac_2['hp']}")
    print("-" * 50)

    # Kontrola či niekto vyhral
    if obranec["hp"] <= 0:
        break

    # Prepnutie ťahu pre ďalšie kolo
    na_rade = 2 if na_rade == 1 else 1

# --- VYHODNOTENIE HRY ---
if hrac_1["hp"] <= 0:
    print(f"\n🏆 Hráč 2 ({hrac_2['meno']}) vyhral súboj! Gratulujem!")
elif hrac_2["hp"] <= 0:
    print(f"\n🏆 Hráč 1 ({hrac_1['meno']}) vyhral súboj! Gratulujem!")
