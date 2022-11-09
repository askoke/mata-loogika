name = input("Sisestage oma nimi: ")
name = name.capitalize() 
allowed_speed = input("Sisestage lubatud kiirus (km/h): ")
actual_speed = input("Sisestage tegelik kiirus (km/h): ")

if allowed_speed < actual_speed:
    fine =(int(actual_speed) - int(allowed_speed)) * 3
    fine = min(192, fine)
    print(f"{name}, kiiruse ületamise eest on teie trahv {fine} eurot.")
else:
    print(f"{name}, te ei ole ületanud kiirust.")
