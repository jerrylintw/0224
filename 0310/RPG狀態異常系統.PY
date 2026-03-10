#這是一個 RPG 狀態異常系統的實作，包含基底類別 Effect 和兩個子類別 Poison 與 Regen，以及一個 Character 類別來管理角色的 HP 和狀態效果。程式會讀取輸入指令來添加狀態效果或進行回合更新，並在每回合結束後顯示當前 HP。
import sys
#sys 模組用於讀取標準輸入，方便處理多行輸入指令。
# 1. 定義基底類別 Effect 
class Effect:
    def __init__(self, duration):
        self.duration = duration

    def apply(self, character):
        # 基底類別不改變數值，僅減少持續時間
        self.duration -= 1

# 2. Poison 繼承 Effect 
class Poison(Effect):
    def apply(self, character):
        character.hp -= 10
        self.duration -= 1

# 3. Regen 繼承 Effect 
class Regen(Effect):
    def apply(self, character):
        character.hp += 15
        self.duration -= 1

# 4. Character 類別 [cite: 354]
class Character:
    def __init__(self, hp):
        self.hp = hp
        self.effects = []

    def add_effect(self, effect):
        # 替角色增加狀態 [cite: 355]
        self.effects.append(effect)

    def next_turn(self):
        # 依序執行所有狀態的 apply 
        for effect in self.effects:
            effect.apply(self)
        
        # 移除 duration 為 0 的狀態 
        # 使用列表推導式安全過濾
        self.effects = [e for e in self.effects if e.duration > 0]
        print(f"Current HP: {self.hp}")

def solve_rpg_buff():
    # 使用 read().split() 處理輸入，確保穩健性
    input_data = sys.stdin.read().split()
    if not input_data: return

    hp = int(input_data[0])
    n = int(input_data[1])
    hero = Character(hp)
    
    curr = 2
    for _ in range(n):
        if curr >= len(input_data): break
        
        cmd = input_data[curr]
        if cmd == "add":
            effect_type = input_data[curr + 1]
            duration = int(input_data[curr + 2])
            
            if effect_type == "Poison":
                hero.add_effect(Poison(duration))
            elif effect_type == "Regen":
                hero.add_effect(Regen(duration))
            curr += 3
        elif cmd == "turn":
            hero.next_turn()
            curr += 1

if __name__ == "__main__":
    solve_rpg_buff()
    # 程式結束後會輸出當前 HP，並且在每回合結束後更新狀態效果。