import random

# Inputy
meno = input("Zadaj svoje meno: ")
trieda_vyber = int(input("Zadaj číslo pre výber svojej triedy - 1. Paladin | 2. Shadow | 3. Knight | 4. Mafian Boss | 5. Mage | 6. Detective: "))
rasa_vyber = int(input("Zadaj číslo pre výber svojej rasy - 1. Strongman | 2. Robot | 3. Upír: "))

# Premenné - Staty hráča
trieda = ""
rasa = ""
zakladne_hp = 100.0
zakladna_mana = 35.0
zakladny_armor = 10.0
zakladny_damage = 10.0

# Premenné - Herné mechaniky
zacina = 1 
som_stunnuty = False

# Premenné - AI (Nepriateľ)
AI_trieda = "Nepriateľ 1"
AI_hp = 100.0
AI_mana = 35.0
AI_armor = 10.0
AI_dmg = 10.0
AI_je_stunnute = False

# Logika - Výber triedy
def vyber_triedu(cislo_triedy):
    global trieda, zakladny_damage, zakladne_hp, zakladna_mana, zakladny_armor

    if cislo_triedy == 1:
        trieda = "Paladin"
        zakladny_damage = 7
        zakladne_hp = 120
        zakladna_mana = 50
        zakladny_armor = 15
    elif cislo_triedy == 2:
        trieda = "Shadow"
        zakladny_damage = 15
        zakladne_hp = 80
        zakladna_mana = 50
        zakladny_armor = 10
    elif cislo_triedy == 3:
        trieda = "Knight"
        zakladny_damage = 12
        zakladne_hp = 100
        zakladna_mana = 25
        zakladny_armor = 20
    elif cislo_triedy == 4:
        trieda = "Mafian Boss"
        zakladny_damage = 15
        zakladne_hp = 100
        zakladna_mana = 30
        zakladny_armor = 10
    elif cislo_triedy == 5:
        trieda = "Mage"
        zakladny_damage = 2
        zakladne_hp = 80
        zakladna_mana = 100
        zakladny_armor = 5
    elif cislo_triedy == 6:
        trieda = "Detective"
        zakladny_damage = 15
        zakladne_hp = 100
        zakladna_mana = 35
        zakladny_armor = 10
    else:
        print("Zadané číslo nemá triedu!")

    print(f"Vybral si si triedu: {trieda}")

def vyber_rasu(cislo_rasy):
    global rasa, zakladny_damage, zakladne_hp, zakladna_mana, zakladny_armor

    if cislo_rasy == 1:
        rasa = "Strongman"
        zakladny_damage *= 1.10
        zakladne_hp *= 1.05
    elif cislo_rasy == 2:
        rasa = "Robot"
        zakladny_damage *= 1.15
        zakladne_hp *= 0.9
        zakladny_armor *= 1.25
    elif cislo_rasy == 3:
        rasa = "Upír"
        zakladny_damage *= 1.20
        zakladne_hp *= 1.10
        zakladny_armor *= 0.85
    else:
        print("Zadané číslo je nesprávne pri vyberaní rasy. Predvolená rasa: Ľudská.")
        rasa = "Človek"

    zakladny_damage = round(zakladny_damage, 2)
    zakladne_hp = round(zakladne_hp, 2)
    zakladny_armor = round(zakladny_armor, 2)

    print(f"Vybral si si rasu: {rasa}")
    print(f"Tvoje staty sú -> HP: {zakladne_hp}, Mana: {zakladna_mana}, Damage: {zakladny_damage}, Armor: {zakladny_armor}")

# --- SPELLY ---

# Paladin Spelly
def divine_strike():
    global AI_hp, zakladna_mana
    AI_hp -= 7
    print(f"-> Paladin použil Divine Strike: Urobil 7 damage nepriateľovi!")

def sacred_grace():
    global zakladne_hp, zakladna_mana
    zakladne_hp += 25
    zakladna_mana -= 15
    print(f"-> Paladin použil Sacred Grace: Vyliečil si 25 HP! (Mana -15)")

def divine_shield():
    global zakladny_armor, zakladna_mana
    zakladny_armor += 3
    zakladna_mana -= 15
    print(f"-> Paladin použil Divine Shield: Armor zvýšený o 3! (Mana -15)")

def celestial_judgement():
    global AI_je_stunnute, AI_hp, zakladna_mana
    AI_je_stunnute = True
    AI_hp -= 5
    zakladna_mana -= 20
    print(f"-> Paladin použil Celestial Judgment: Urobil 5 damage a OMNIESTNIL nepriateľa (Stun)! (Mana -20)")


# Mage Spelly
def lighting_strike():
    global AI_hp, zakladna_mana
    AI_hp -= 20
    zakladna_mana -= 5
    print(f"-> Mage použil Lightning Strike: Urobil 20 damage nepriateľovi! (Mana -5)")

def mana_regen_boost():
    global zakladna_mana
    zakladna_mana = zakladna_mana - 5 + 30
    print(f"-> Mage použil Mana Regen Boost: Získal späť 30 many!")

def ground_zero():
    global AI_je_stunnute, zakladna_mana
    AI_je_stunnute = True
    zakladna_mana -= 20
    print(f"-> Mage použil Ground Zero: Omráčil nepriateľa (Stun)! (Mana -20)")

def obliteration():
    global AI_hp, zakladna_mana
    AI_hp -= 55
    zakladna_mana -= 50
    print(f"-> Mage použil Obliteration: Spôsobil masívnych 55 damage! (Mana -50)")


# Knight Spelly
def bloodlust():
    global AI_hp, zakladna_mana
    AI_hp -= 10
    zakladna_mana -= 5
    print(f"-> Knight použil Bloodlust: Zrezao nepriateľa za 10 damage! (Mana -5)")

def ironclad_defence():
    global zakladny_armor, zakladna_mana
    zakladny_armor += 5
    zakladna_mana -= 5
    print(f"-> Knight použil Ironclad Defense: Zvýšil armor o 5! (Mana -5)")

def blinding_steel():
    global AI_je_stunnute, zakladna_mana
    AI_je_stunnute = True
    zakladna_mana -= 5
    print(f"-> Knight použil Blinding Steel: Omráčil nepriateľa (Stun)! (Mana -5)")

def undying_warrior():
    global zakladne_hp, zakladna_mana
    zakladne_hp += 25
    zakladna_mana -= 10
    print(f"-> Knight použil Undying Warrior: Vyliečil si 25 HP! (Mana -10)")


# Shadow Spelly
def shadow_strike():
    global AI_hp, zakladna_mana
    AI_hp -= 10
    zakladna_mana += 5
    print(f"-> Shadow použil Shadow Strike: Urobil 10 damage a získal 5 many! (Mana +5)")

def black_smoke():
    global AI_je_stunnute, zakladna_mana
    AI_je_stunnute = True
    zakladna_mana -= 10
    print(f"-> Shadow použil Black Smoke: Omráčil nepriateľa (Stun)! (Mana -10)")

def teleport():
    global AI_dmg, zakladna_mana
    AI_dmg = 0
    zakladna_mana -= 5
    print(f"-> Shadow použil Teleport: Vyhol sa útoku (AI damage na toto kolo je 0)! (Mana -5)")

def backstab():
    global AI_hp, AI_je_stunnute, zakladna_mana
    AI_hp -= 25
    AI_je_stunnute = True
    zakladna_mana -= 25
    print(f"-> Shadow použil Backstab: Zasadil smrteľnú dýku za 25 damage a omráčil nepriateľa! (Mana -25)")


# Mafian Boss Spelly
def cokoladova_ferovka():
    global AI_hp, zakladny_damage, zakladna_mana
    AI_hp -= zakladny_damage
    zakladna_mana -= 5
    print(f"-> Mafian Boss použil Čokoládovú férovku: Urobil {zakladny_damage} damage! (Mana -5)")

def cls320cdi():
    global AI_dmg, zakladna_mana
    AI_dmg -= 3
    zakladna_mana -= 10
    print(f"-> Mafian Boss previedol CLS320CDi: Znížil damage nepriateľa o 3! (Mana -10)")

def kotlar_ability():
    global AI_hp, zakladne_hp, zakladna_mana
    AI_hp -= 15
    zakladne_hp += 15
    zakladna_mana -= 10
    print(f"-> Mafian Boss použil Kotlár ability: Urobil 15 damage a ukradol 15 HP pre seba! (Mana -10)")

def ultina_bakhtalospecial():
    global AI_hp, zakladna_mana
    AI_hp -= 50
    zakladna_mana -= 20
    print(f"-> Mafian Boss použil Bakhtalo Špeciál: Spôsobil obrovských 50 damage! (Mana -20)")


# Detective Spelly
def deadly_shot():
    global AI_hp, zakladna_mana
    AI_hp -= 50
    zakladna_mana -= 15
    print(f"-> Detective použil Deadly Shot: Presná trefa za 50 damage! (Mana -15)")

def pistol_attack():
    global AI_hp, zakladny_damage, zakladna_mana
    AI_hp -= zakladny_damage
    print(f"-> Detective použil Pistol Attack: Urobil {zakladny_damage} damage!")

def handcuffs():
    global AI_je_stunnute, AI_hp, zakladna_mana
    AI_je_stunnute = True
    AI_hp -= 5
    zakladna_mana -= 5
    print(f"-> Detective nasadil Handcuffs: Dal 5 damage a omráčil nepriateľa (Stun)! (Mana -5)")

def adrenaline_shot():
    global zakladne_hp, zakladna_mana
    zakladne_hp += 25
    zakladna_mana -= 5
    print(f"-> Detective pichol Adrenaline Shot: Vyliečil si 25 HP! (Mana -5)")


# Spustenie výberu
vyber_triedu(trieda_vyber)
vyber_rasu(rasa_vyber)

zacina = random.randint(1, 2)
print(f"\nLosovanie: Kto začína? (1 = Hráč, 2 = AI) -> Padlo: {zacina}")
print(f"Bojuješ s triedou: {trieda}\n" + "-"*50)

# Hlavná herná slučka
# Hlavná herná slučka
while zakladne_hp > 0 and AI_hp > 0:
    # ---------------- HRÁČOV TAH ----------------
    if zacina == 1:
        if som_stunnuty:
            print(f"\n⚠️ {meno}, si OMRÁČENÝ (Stunnutý) a nemôžeš konať! Prebieha ťah AI...")
            som_stunnuty = False  # Stun vyprší po tomto kole
        else:
            # Hráč si vyberá akciu dokým nezadá platnú akciu, na ktorú má aj manu
            while True:
                print(f"\nTvoj ťah! (Tvoje HP: {zakladne_hp} | Mana: {zakladna_mana} | Armor: {zakladny_armor})")
                
                spraveny_tah = False

                if trieda == "Paladin":
                    akcia = int(input("Vyber akciu: 1. Divine Strike (Mana: 5) | 2. Sacred Grace (Mana: 15) | 3. Divine Shield (Mana: 15) | 4. Celestial Judgment (Mana: 20): "))
                    if akcia == 1:
                        if zakladna_mana >= 5: divine_strike(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 2:
                        if zakladna_mana >= 15: sacred_grace(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 15)!")
                    elif akcia == 3:
                        if zakladna_mana >= 15: divine_shield(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 15)!")
                    elif akcia == 4:
                        if zakladna_mana >= 20: celestial_judgement(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 20)!")
                    else: 
                        print("Neplatná voľba!")

                elif trieda == "Shadow":
                    akcia = int(input("Vyber akciu: 1. Shadow Strike (Mana: +5) | 2. Black Smoke (Mana: 10) | 3. Teleport (Mana: 5) | 4. Backstab (Mana: 25): "))
                    if akcia == 1:
                        shadow_strike(); spraveny_tah = True
                    elif akcia == 2:
                        if zakladna_mana >= 10: black_smoke(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 10)!")
                    elif akcia == 3:
                        if zakladna_mana >= 5: teleport(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 4:
                        if zakladna_mana >= 25: backstab(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 25)!")
                    else: 
                        print("Neplatná voľba!")

                elif trieda == "Knight":
                    akcia = int(input("Vyber akciu: 1. Bloodlust (Mana: 5) | 2. Ironclad Defense (Mana: 5) | 3. Blinding Steel (Mana: 5) | 4. Undying Warrior (Mana: 10): "))
                    if akcia == 1:
                        if zakladna_mana >= 5: bloodlust(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 2:
                        if zakladna_mana >= 5: ironclad_defence(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 3:
                        if zakladna_mana >= 5: blinding_steel(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 4:
                        if zakladna_mana >= 10: undying_warrior(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 10)!")
                    else: 
                        print("Neplatná voľba!")

                elif trieda == "Mafian Boss":
                    akcia = int(input("Vyber akciu: 1. Čokoládova férovka (Mana: 5) | 2. CLS320CDi (Mana: 10) | 3. Kotlár (Mana: 10) | 4. Bakhtalo Špeciál (Mana: 20): "))
                    if akcia == 1:
                        if zakladna_mana >= 5: cokoladova_ferovka(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 2:
                        if zakladna_mana >= 10: cls320cdi(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 10)!")
                    elif akcia == 3:
                        if zakladna_mana >= 10: kotlar_ability(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 10)!")
                    elif akcia == 4:
                        if zakladna_mana >= 20: ultina_bakhtalospecial(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 20)!")
                    else: 
                        print("Neplatná voľba!")

                elif trieda == "Mage":
                    akcia = int(input("Vyber akciu: 1. Lightning Strike (Mana: 5) | 2. Mana Regen Boost (Mana: 5) | 3. Ground Zero (Mana: 20) | 4. Obliteration (Mana: 50): "))
                    if akcia == 1:
                        if zakladna_mana >= 5: lighting_strike(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 2:
                        if zakladna_mana >= 5: mana_regen_boost(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 3:
                        if zakladna_mana >= 20: ground_zero(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 20)!")
                    elif akcia == 4:
                        if zakladna_mana >= 50: obliteration(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 50)!")
                    else: 
                        print("Neplatná voľba!")

                elif trieda == "Detective":
                    akcia = int(input("Vyber akciu: 1. Pistol Attack (Mana: 0) | 2. Handcuffs (Mana: 5) | 3. Adrenaline Shot (Mana: 5) | 4. Deadly Shot (Mana: 15): "))
                    if akcia == 1:
                        pistol_attack(); spraveny_tah = True
                    elif akcia == 2:
                        if zakladna_mana >= 5: handcuffs(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 3:
                        if zakladna_mana >= 5: adrenaline_shot(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 5)!")
                    elif akcia == 4:
                        if zakladna_mana >= 15: deadly_shot(); spraveny_tah = True
                        else: print("❌ Nemáš dostatok many (potrebuješ 15)!")
                    else: 
                        print("Neplatná voľba!")

                # Ak bol spell úspešne vykonaný, vyskočíme z vnútorného while True výberu
                if spraveny_tah:
                    break

        # Ošetrenie záporných hodnôt a zaokrúhlenie
        zakladne_hp = round(max(0.0, zakladne_hp), 2)
        AI_hp = round(max(0.0, AI_hp), 2)
        zakladna_mana = round(max(0.0, zakladna_mana), 2)

        # Výpis po tvojom ťahu
        print(f"\n📊 Stav po tvojom ťahu -> Tvoje HP: {zakladne_hp} | AI HP: {AI_hp} | Tvoja Mana: {zakladna_mana}")
        print("-" * 50)

        # Skontrolovanie, či AI nezomrelo
        if AI_hp <= 0:
            break

        zacina = 2  # Na rade je AI

    # ---------------- AI TAH ----------------
    elif zacina == 2:
        if AI_je_stunnute:
            print(f"\n⚠️ AI je OMRÁČENÉ (Stunnuté) a nemôže konať!")
            AI_je_stunnute = False  # Stun vyprší
        else:
            AI_akcia = random.randint(1, 4)
            
            if AI_akcia == 1:  # AI Útok
                realdmg = round(AI_dmg * (1 - (zakladny_armor / 100)), 2)
                zakladne_hp -= realdmg
                print(f"\n🤖 AI zaútočilo! Dalo ti {realdmg} damage (Armor zredukoval časť poškodenia).")
                
            elif AI_akcia == 2 and AI_mana >= 10:  # AI Heal
                AI_hp += 20
                AI_mana -= 10
                print(f"\n🤖 AI sa vyliečilo o 20 HP! (AI Mana -10)")
                
            elif AI_akcia == 3 and AI_mana >= 5:  # AI Stun útok
                realdmg = round(5 * (1 - (zakladny_armor / 100)), 2)
                zakladne_hp -= realdmg
                som_stunnuty = True
                AI_mana -= 5
                print(f"\n🤖 AI použilo Stun útok! Dalo ti {realdmg} damage a OMRÁČILO ťa!")
                
            elif AI_akcia == 4 and AI_mana >= 20:  # AI Ultina
                realdmg = round(50 * (1 - (zakladny_armor / 100)), 2)
                zakladne_hp -= realdmg
                AI_mana -= 20
                som_stunnuty = True
                print(f"\n🤖 AI použilo ULTIMÁTNY ÚTOK! Dalo ti brutálnych {realdmg} damage a omráčilo ťa!")
            else:
                realdmg = round(AI_dmg * (1 - (zakladny_armor / 100)), 2)
                zakladne_hp -= realdmg
                print(f"\n🤖 AI nemá dostatok many na špeciál, tak zaútočilo štandardne za {realdmg} damage.")

        zakladne_hp = round(max(0.0, zakladne_hp), 2)
        AI_hp = round(max(0.0, AI_hp), 2)
        
        print(f"📊 Stav po tahu AI -> Tvoje HP: {zakladne_hp} | AI HP: {AI_hp}")
        print("-" * 50)
        
        zacina = 1  # Na rade je opäť hráč

# Vyhodnotenie hry po skončení while loopu
if zakladne_hp <= 0:
    print(f"\n💀 Prehral si! AI ťa porazilo.")
elif AI_hp <= 0:
    print(f"\n🏆 Gratulujem {meno}! Úspešne si porazil nepriateľa a vyhral hru!")