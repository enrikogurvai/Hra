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

# --- STATY HRÁČA 1 ---
trieda_1 = ""
rasa_1 = ""
hp_1 = 100.0
mana_1 = 35.0
armor_1 = 10.0
damage_1 = 10.0
stun_1 = False

# --- STATY HRÁČA 2 ---
trieda_2 = ""
rasa_2 = ""
hp_2 = 100.0
mana_2 = 35.0
armor_2 = 10.0
damage_2 = 10.0
stun_2 = False

# Funkcia na výpočet reálneho damage s ohľadom na armor (10 armor = 10% resist)
def aplikuj_armor(raw_dmg, defender_armor):
    # Vzorec: raw_dmg * (1 - (armor / 100))
    realdmg = raw_dmg * (1 - (defender_armor / 100))
    return round(max(0.0, realdmg), 2)

# Funkcia na nastavenie triedy
def nastav_triedu(cislo_triedy):
    t, dmg, hp, mana, arm = "", 10, 100, 35, 10
    
    if cislo_triedy == 1:
        t, dmg, hp, mana, arm = "Paladin", 7, 120, 50, 15
    elif cislo_triedy == 2:
        t, dmg, hp, mana, arm = "Shadow", 15, 80, 50, 10
    elif cislo_triedy == 3:
        t, dmg, hp, mana, arm = "Knight", 12, 100, 25, 20
    elif cislo_triedy == 4:
        t, dmg, hp, mana, arm = "Mafian Boss", 15, 100, 30, 10
    elif cislo_triedy == 5:
        t, dmg, hp, mana, arm = "Mage", 2, 80, 100, 5
    elif cislo_triedy == 6:
        t, dmg, hp, mana, arm = "Detective", 15, 100, 35, 10
    else:
        print("Neplatná trieda, predvolené na Paladin.")
        t, dmg, hp, mana, arm = "Paladin", 7, 120, 50, 15
        
    return t, dmg, hp, mana, arm

# Funkcia na nastavenie rasy
def nastav_rasu(t, dmg, hp, mana, arm, cislo_rasy):
    r = "Človek"
    if cislo_rasy == 1:
        r = "Strongman"
        dmg *= 1.10
        hp *= 1.05
    elif cislo_rasy == 2:
        r = "Robot"
        dmg *= 1.15
        hp *= 0.9
        arm *= 1.25
    elif cislo_rasy == 3:
        r = "Upír"
        dmg *= 1.20
        hp *= 1.10
        arm *= 0.85
        
    return r, round(dmg, 2), round(hp, 2), mana, round(arm, 2)

# Inicializácia Hráča 1
trieda_1, damage_1, hp_1, mana_1, armor_1 = nastav_triedu(trieda_vyber_1)
rasa_1, damage_1, hp_1, mana_1, armor_1 = nastav_rasu(trieda_1, damage_1, hp_1, mana_1, armor_1, rasa_vyber_1)

# Inicializácia Hráča 2
trieda_2, damage_2, hp_2, mana_2, armor_2 = nastav_triedu(trieda_vyber_2)
rasa_2, damage_2, hp_2, mana_2, armor_2 = nastav_rasu(trieda_2, damage_2, hp_2, mana_2, armor_2, rasa_vyber_2)

print("\n" + "="*50)
print(f"Hráč 1: {meno_1} ({trieda_1} - {rasa_1}) | HP: {hp_1} | Mana: {mana_1} | Armor: {armor_1}")
print(f"Hráč 2: {meno_2} ({trieda_2} - {rasa_2}) | HP: {hp_2} | Mana: {mana_2} | Armor: {armor_2}")
print("="*50 + "\n")

# Losovanie, kto začína
na_rade = random.randint(1, 2)
print(f"🎲 Losovanie: Na rade je -> {'Hráč 1 (' + meno_1 + ')' if na_rade == 1 else 'Hráč 2 (' + meno_2 + ')'}\n" + "-"*50)

# --- HLAVNÁ HERNÁ SLUČKA (MULTIPLAYER) ---
while hp_1 > 0 and hp_2 > 0:
    
    # ==========================================
    # 👤 TAH HRÁČA 1
    # ==========================================
    if na_rade == 1:
        if stun_1:
            print(f"\n⚠️ {meno_1}, si OMRÁČENÝ (Stunnutý) a nemôžeš konať!")
            stun_1 = False
        else:
            while True:
                print(f"\n👉 Na rade je {meno_1} ({trieda_1}) | HP: {hp_1} | Mana: {mana_1} | Armor: {armor_1}")
                spraveny_tah = False
                
                if trieda_1 == "Paladin":
                    akcia = int(input("Vyber akciu: 1. Divine Strike (Mana: 0) | 2. Sacred Grace (Mana: 15) | 3. Divine Shield (Mana: 15) | 4. Celestial Judgment (Mana: 20): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(7, armor_2); hp_2 -= dmg; print(f"-> Divine Strike: Zostrelil {dmg} HP (Armor zredukoval poškodenie)!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_1 >= 15: hp_1 += 25; mana_1 -= 15; print("-> Sacred Grace: +25 HP!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_1 >= 15: armor_1 += 3; mana_1 -= 15; print("-> Divine Shield: +3 Armor!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_1 >= 20: 
                            dmg = aplikuj_armor(5, armor_2); hp_2 -= dmg; stun_2 = True; mana_1 -= 20
                            print(f"-> Celestial Judgment: {dmg} damage a STUN pre Hráča 2!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                        
                elif trieda_1 == "Shadow":
                    akcia = int(input("Vyber akciu: 1. Shadow Strike (Mana: +5) | 2. Black Smoke (Mana: 10) | 3. Teleport (Mana: 5) | 4. Backstab (Mana: 25): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(10, armor_2); hp_2 -= dmg; mana_1 += 5
                        print(f"-> Shadow Strike: {dmg} damage, +5 many!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_1 >= 10: stun_2 = True; mana_1 -= 10; print("-> Black Smoke: STUN pre Hráča 2!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_1 >= 5: mana_1 -= 5; print("-> Teleport pripravený!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_1 >= 25: 
                            dmg = aplikuj_armor(25, armor_2); hp_2 -= dmg; stun_2 = True; mana_1 -= 25
                            print(f"-> Backstab: {dmg} damage a STUN!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_1 == "Knight":
                    akcia = int(input("Vyber akciu: 1. Bloodlust (Mana: 0) | 2. Ironclad Defense (Mana: 5) | 3. Blinding Steel (Mana: 5) | 4. Undying Warrior (Mana: 10): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(10, armor_2); hp_2 -= dmg; print(f"-> Bloodlust: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_1 >= 5: armor_1 += 5; mana_1 -= 5; print("-> Ironclad Defense: +5 Armor!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_1 >= 5: stun_2 = True; mana_1 -= 5; print("-> Blinding Steel: STUN pre Hráča 2!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_1 >= 10: hp_1 += 25; mana_1 -= 10; print("-> Undying Warrior: +25 HP!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_1 == "Mafian Boss":
                    akcia = int(input("Vyber akciu: 1. Čokoládova férovka (Mana: 0) | 2. CLS320CDi (Mana: 10) | 3. Kotlár (Mana: 10) | 4. Bakhtalo Špeciál (Mana: 20): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(damage_1, armor_2); hp_2 -= dmg; print(f"-> Čokoládova férovka: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_1 >= 10: damage_2 = max(0.0, damage_2 - 3); mana_1 -= 10; print("-> CLS320CDi: Znížený damage Hráča 2 o 3!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_1 >= 10: 
                            dmg = aplikuj_armor(15, armor_2); hp_2 -= dmg; hp_1 += 15; mana_1 -= 10
                            print(f"-> Kotlár: {dmg} damage Hráčovi 2, +15 HP tebe!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_1 >= 20: 
                            dmg = aplikuj_armor(50, armor_2); hp_2 -= dmg; mana_1 -= 20
                            print(f"-> Bakhtalo Špeciál: {dmg} damage!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_1 == "Mage":
                    akcia = int(input("Vyber akciu: 1. Lightning Strike (Mana: 0) | 2. Mana Regen Boost (Mana: 5) | 3. Ground Zero (Mana: 20) | 4. Obliteration (Mana: 50): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(20, armor_2); hp_2 -= dmg; print(f"-> Lightning Strike: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_1 >= 5: mana_1 = mana_1 - 5 + 30; print("-> Mana Regen Boost: +30 many!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_1 >= 20: stun_2 = True; mana_1 -= 20; print("-> Ground Zero: STUN pre Hráča 2!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_1 >= 50: 
                            dmg = aplikuj_armor(55, armor_2); hp_2 -= dmg; mana_1 -= 50
                            print(f"-> Obliteration: Masívnych {dmg} damage!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_1 == "Detective":
                    akcia = int(input("Vyber akciu: 1. Pistol Attack (Mana: 0) | 2. Handcuffs (Mana: 5) | 3. Adrenaline Shot (Mana: 5) | 4. Deadly Shot (Mana: 15): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(damage_1, armor_2); hp_2 -= dmg; print(f"-> Pistol Attack: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_1 >= 5: 
                            dmg = aplikuj_armor(5, armor_2); hp_2 -= dmg; stun_2 = True; mana_1 -= 5
                            print(f"-> Handcuffs: {dmg} damage a STUN!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_1 >= 5: hp_1 += 25; mana_1 -= 5; print("-> Adrenaline Shot: +25 HP!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_1 >= 15: 
                            dmg = aplikuj_armor(50, armor_2); hp_2 -= dmg; mana_1 -= 15
                            print(f"-> Deadly Shot: {dmg} damage!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                if spraveny_tah:
                    break

        # Ošetrenie statov
        hp_1 = round(max(0.0, hp_1), 2)
        hp_2 = round(max(0.0, hp_2), 2)
        mana_1 = round(max(0.0, mana_1), 2)

        print(f"\n📊 Stav po ťahu ({meno_1}) -> {meno_1} HP: {hp_1} | {meno_2} HP: {hp_2}")
        print("-" * 50)

        if hp_2 <= 0:
            break

        na_rade = 2  # Prepnutie na Hráča 2

    # ==========================================
    # 👤 TAH HRÁČA 2
    # ==========================================
    elif na_rade == 2:
        if stun_2:
            print(f"\n⚠️ {meno_2}, si OMRÁČENÝ (Stunnutý) a nemôžeš konať!")
            stun_2 = False
        else:
            while True:
                print(f"\n👉 Na rade je {meno_2} ({trieda_2}) | HP: {hp_2} | Mana: {mana_2} | Armor: {armor_2}")
                spraveny_tah = False
                
                if trieda_2 == "Paladin":
                    akcia = int(input("Vyber akciu: 1. Divine Strike (Mana: 0) | 2. Sacred Grace (Mana: 15) | 3. Divine Shield (Mana: 15) | 4. Celestial Judgment (Mana: 20): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(7, armor_1); hp_1 -= dmg; print(f"-> Divine Strike: Zostrelil {dmg} HP!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_2 >= 15: hp_2 += 25; mana_2 -= 15; print("-> Sacred Grace: +25 HP!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_2 >= 15: armor_2 += 3; mana_2 -= 15; print("-> Divine Shield: +3 Armor!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_2 >= 20: 
                            dmg = aplikuj_armor(5, armor_1); hp_1 -= dmg; stun_1 = True; mana_2 -= 20
                            print(f"-> Celestial Judgment: {dmg} damage a STUN pre Hráča 1!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                        
                elif trieda_2 == "Shadow":
                    akcia = int(input("Vyber akciu: 1. Shadow Strike (Mana: +5) | 2. Black Smoke (Mana: 10) | 3. Teleport (Mana: 5) | 4. Backstab (Mana: 25): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(10, armor_1); hp_1 -= dmg; mana_2 += 5
                        print(f"-> Shadow Strike: {dmg} damage, +5 many!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_2 >= 10: stun_1 = True; mana_2 -= 10; print("-> Black Smoke: STUN pre Hráča 1!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_2 >= 5: mana_2 -= 5; print("-> Teleport pripravený!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_2 >= 25: 
                            dmg = aplikuj_armor(25, armor_1); hp_1 -= dmg; stun_1 = True; mana_2 -= 25
                            print(f"-> Backstab: {dmg} damage a STUN!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_2 == "Knight":
                    akcia = int(input("Vyber akciu: 1. Bloodlust (Mana: 0) | 2. Ironclad Defense (Mana: 5) | 3. Blinding Steel (Mana: 5) | 4. Undying Warrior (Mana: 10): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(10, armor_1); hp_1 -= dmg; print(f"-> Bloodlust: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_2 >= 5: armor_2 += 5; mana_2 -= 5; print("-> Ironclad Defense: +5 Armor!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_2 >= 5: stun_1 = True; mana_2 -= 5; print("-> Blinding Steel: STUN pre Hráča 1!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_2 >= 10: hp_2 += 25; mana_2 -= 10; print("-> Undying Warrior: +25 HP!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_2 == "Mafian Boss":
                    akcia = int(input("Vyber akciu: 1. Čokoládova férovka (Mana: 0) | 2. CLS320CDi (Mana: 10) | 3. Kotlár (Mana: 10) | 4. Bakhtalo Špeciál (Mana: 20): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(damage_2, armor_1); hp_1 -= dmg; print(f"-> Čokoládova férovka: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_2 >= 10: damage_1 = max(0.0, damage_1 - 3); mana_2 -= 10; print("-> CLS320CDi: Znížený damage Hráča 1 o 3!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_2 >= 10: 
                            dmg = aplikuj_armor(15, armor_1); hp_1 -= dmg; hp_2 += 15; mana_2 -= 10
                            print(f"-> Kotlár: {dmg} damage Hráčovi 1, +15 HP tebe!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_2 >= 20: 
                            dmg = aplikuj_armor(50, armor_1); hp_1 -= dmg; mana_2 -= 20
                            print(f"-> Bakhtalo Špeciál: {dmg} damage!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_2 == "Mage":
                    akcia = int(input("Vyber akciu: 1. Lightning Strike (Mana: 0) | 2. Mana Regen Boost (Mana: 5) | 3. Ground Zero (Mana: 20) | 4. Obliteration (Mana: 50): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(20, armor_1); hp_1 -= dmg; print(f"-> Lightning Strike: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_2 >= 5: mana_2 = mana_2 - 5 + 30; print("-> Mana Regen Boost: +30 many!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_2 >= 20: stun_1 = True; mana_2 -= 20; print("-> Ground Zero: STUN pre Hráča 1!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_2 >= 50: 
                            dmg = aplikuj_armor(55, armor_1); hp_1 -= dmg; mana_2 -= 50
                            print(f"-> Obliteration: Masívnych {dmg} damage!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                elif trieda_2 == "Detective":
                    akcia = int(input("Vyber akciu: 1. Pistol Attack (Mana: 0) | 2. Handcuffs (Mana: 5) | 3. Adrenaline Shot (Mana: 5) | 4. Deadly Shot (Mana: 15): "))
                    if akcia == 1: 
                        dmg = aplikuj_armor(damage_2, armor_1); hp_1 -= dmg; print(f"-> Pistol Attack: {dmg} damage!"); spraveny_tah = True
                    elif akcia == 2: 
                        if mana_2 >= 5: 
                            dmg = aplikuj_armor(5, armor_1); hp_1 -= dmg; stun_1 = True; mana_2 -= 5
                            print(f"-> Handcuffs: {dmg} damage a STUN!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 3: 
                        if mana_2 >= 5: hp_2 += 25; mana_2 -= 5; print("-> Adrenaline Shot: +25 HP!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")
                    elif akcia == 4: 
                        if mana_2 >= 15: 
                            dmg = aplikuj_armor(50, armor_1); hp_1 -= dmg; mana_2 -= 15
                            print(f"-> Deadly Shot: {dmg} damage!"); spraveny_tah = True
                        else: print("❌ Nedostatok many!")

                if spraveny_tah:
                    break

        # Ošetrenie statov
        hp_1 = round(max(0.0, hp_1), 2)
        hp_2 = round(max(0.0, hp_2), 2)
        mana_2 = round(max(0.0, mana_2), 2)

        print(f"\n📊 Stav po ťahu ({meno_2}) -> {meno_1} HP: {hp_1} | {meno_2} HP: {hp_2}")
        print("-" * 50)

        if hp_1 <= 0:
            break

        na_rade = 1  # Prepnutie na Hráča 1

# --- VYHODNOTENIE HRY ---
if hp_1 <= 0:
    print(f"\n🏆 Hráč 2 ({meno_2}) vyhral súboj! Gratulujem!")
elif hp_2 <= 0:
    print(f"\n🏆 Hráč 1 ({meno_1}) vyhral súboj! Gratulujem!")
