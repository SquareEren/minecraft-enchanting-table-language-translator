import tkinter as tk

def create_minecraft_text(canvas, x, y):
    minecraft_text = "Minecraft Enchanting table Language Translator"
    canvas.create_text(x, y, text=minecraft_text, font=("Arial", 12), fill="#000000")

def minecraft_translate(word):
    symbol_set = "ᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹!¡∷ᓭℸ ̣⚍⍊∴ ̇/||⨅"
    translation = ""

    for char in word.lower():
        if char.isalpha() and 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            translation += symbol_set[index]
        else:
            translation += char

    return translation

def on_translate_button_click():
    kelime = kelime_entry.get("1.0", tk.END).strip()  # Kelimeyi al, boşlukları temizle
    cevirisi = minecraft_translate(kelime)
    sonuc_text.config(state=tk.NORMAL)  # state'i NORMAL yap
    sonuc_text.delete("1.0", tk.END)  # Önceki sonucu temizle
    sonuc_text.insert(tk.END, cevirisi)
    sonuc_text.config(state=tk.DISABLED)  # state'i DISABLED yap

# Tkinter penceresi oluştur
root = tk.Tk()
root.title("Minecraft Çevirici")

# Pencere boyutunu belirle (genişlik x yükseklik)
root.geometry("800x600")

# Canvas oluştur
canvas = tk.Canvas(root, width=400, height=100)
canvas.pack()

# Minecraft kelimesini yaz
create_minecraft_text(canvas, 200, 50)

# Frame oluştur
frame = tk.Frame(root)
frame.pack(pady=10)

# Kullanıcıdan çok satırlı giriş alacak Text bileşeni
kelime_entry = tk.Text(frame, height=15, width=30)  # height ve width parametreleriyle boyutu belirle
kelime_entry.grid(row=0, column=0, padx=5)

# Çeviri sonucunu gösterecek Text bileşeni
sonuc_text = tk.Text(frame, height=15, width=30, state=tk.DISABLED)  # height ve width parametreleriyle boyutu belirle, state'i DISABLED yap
sonuc_text.grid(row=0, column=1, padx=5)

# Çeviri butonu
translate_button = tk.Button(frame, text="Çevir", command=on_translate_button_click, width=10, height=2)
translate_button.grid(row=1, column=0, columnspan=2, pady=5)

# Pencereyi başlat
root.mainloop()
