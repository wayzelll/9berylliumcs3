import sys 

zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",    
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

BASE_YEAR = 1900

try:
    birth_year = int(input("Enter your birth year: "))
    
    if birth_year < BASE_YEAR:
        print(f"Invalid year, should not be earlier than {BASE_YEAR}")
        sys.exit()
        
    index = (birth_year - BASE_YEAR) % 12
    sign = zodiac_signs[index]
    
    print(f"Your Chinese Zodiac Sign is: {sign}")

except ValueError:
    print("Invalid input. Please enter a numeric year.")
    sys.exit()
