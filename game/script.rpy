# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character('Yasunori', color="#f542e3")
define m = Character('Me', color="#f58442")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene sunset
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    m "\nМоя первая любовь пришла ко мне во время старшей школы..."

    m "Перевод в новую школу, новые знакомства.\n Нужно оправиться от прошлых травм и начать жизнь с чистого листа..."

    m "Впервые мы встретились на перекличке... Шли дни, наше общение становилось все более теплым..."

menu:

    "Попытаться сблизиться":
        jump relathionship

    "Держать дистанцию":
        jump solo

label relathionship:
    m "Меня захлестнул поток чувств к ней... Я дорожил каждым воспоминанием.."
    jump continue
    # This ends the game.
label solo:
    m "И как это будет выглядеть?"
    m "Я не могу так"
    jump continue

label continue:
    m "Прошло уже достаточно времени, но я все еще помню об этих днях"
    return
