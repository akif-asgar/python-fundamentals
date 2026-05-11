# Resturant Menu with Dictionary
menu = {
    "Pasta": 12.99,
    "Pizza": 9.99,
    "Salad": 7.99,
    "Burger": 10.99,
    "Soda": 1.99,
    "Coffee": 2.99,
    
}

print("Xoş gəlmisiniz! Menyu:")
for item, price in menu.items():
    print(f"{item}: {price:.2f} AZN")




basket =  []
total = 0

while True:
    
    order = input("Zəhmət olmasa, sifarişinizi daxil edin (bitirmək üçün 'exit' yazın): ").capitalize()
    
    if menu.get(order) == 'None': 
        
        print('Menyumuzda belə bir qida yoxdur')
        
        print("Menyu:")
        for item, price in menu.items():
             print(f"{item}: {price:.2f} AZN")
             
    else:
        
        if order == "Exit":
            
            print(f"Sizin sifarişləriniz {basket} və ümumi hesabınız: {total:.2f} AZN")
            print("Yenidən gözləyirik!")
            break
        
        basket.append(order)
        total += menu[order]
        print(f"{order} əlavə edildi. Cari hesabınız: {total:.2f} AZN")
        

        
        
        
        