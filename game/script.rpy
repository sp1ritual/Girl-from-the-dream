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
    #
    #
    m "Холм, небо заливается нежно-персиковым закатом,"
    m "Лепестки кружатся в быстром танце, аккуратно застилая землю."
    m "А рядом эта девушка – воплощение женственности и элегантности."
    m 'У нее длинные и густые волосы, которые спадают на её плечи, словно шелк.'
    m 'Их цвет похож на темный солнечный луч – яркий медовый оттенок, который подчеркивает её изящную красоту.'
