questions = (
    "Dünyada ən çox danışılan yerli dil hansıdır?",
    "Hansi rəng işığı ən çox əks etdirir?",
    "Everest zirvəsi hansı dağ silsiləsində yerləşir?",
    "İnsanda hansı orqan qanı təmizləyir?"
)

options = (
    ("A. İngilis", "B. Mandarin", "C. İspan", "D. Hind"),
    ("A. Qara", "B. Qırmızı", "C. Ağ", "D. Mavi"),
    ("A. And", "B. Alplar", "C. Qafqaz", "D. Himalay"),
    ("A. Ürək", "B. Böyrək", "C. Ağciyər", "D. Mədə")
)

answers = ("B", "C", "D", "B")
guesses = []
unique_guesses = set()

score = 0
question_num = 0

print("--- ÜMUMİ BİLGİ QUİZİ ---")

for question in questions:
    print("-------------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)
    
    guess = input("Cavabınızı daxil edin (A, B, C, D): ").upper()
    guesses.append(guess)
    unique_guesses.add(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("DOĞRUDUR!")
    else:
        print(f"SƏHVDİR! Düzgün cavab: {answers[question_num]}")
        
    question_num += 1

print("-------------------------")
print("        NƏTİCƏ           ")
print("-------------------------")

print("Düzgün cavablar: ", *answers)
print("Sizin cavablar: ", *guesses)

score_percent = int(score / len(questions) * 100)
print(f"\nSizin ümumi balınız: {score_percent}%")
print(f"İstifadə etdiyiniz unikal variantlar: {unique_guesses}")

