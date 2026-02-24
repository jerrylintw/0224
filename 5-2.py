import sys

# 定義標準摩斯密碼字典
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

def solve():
    # 使用 sys.stdin 讀取所有輸入行，解決 EOF 問題
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        text = line.upper() # 題目要求大小寫視為相同 
        result = []
        
        for char in text:
            if char == ' ':
                result.append('+') # 單字間的空白輸出加號 
            elif char in MORSE_CODE_DICT:
                result.append(MORSE_CODE_DICT[char]) # 字母轉換為摩斯碼 [cite: 56]
            # 不在字典中的符號忽略不處理 
                
        # 字母編碼之間、加號前後，均以一個空白隔開 
        print(" ".join(result))

if __name__ == "__main__":
    solve()
    #56322