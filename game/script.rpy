# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define strange_girl = Character('...',color="#f542e3")
define main_girl = Character('Ясунори', color="#f542e3")
define player_name = "???"



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
    

    play music "prologue.ogg"
    """
    Сны – это загадочное и захватывающее приключение, которое сопровождает человека на протяжение всей жизни,

    Их природа доподлинно не известна, они могут отражать наше эмоциональное состояние и переживания, бережно обрабатывая их во время отдыха организма.

    В этих загадочных мирах можно любить, бояться, сопереживать или все вместе, но что, если они таят в себе нечто большее? 
    """
    player_name """
    Непроглядная тьма, безмятежность и спокойствие. Так обычно видятся мной сны за последние десять лет

    Будто что-то щелкнуло внутри и я перестал видеть истории своего прошлого и фантастического будущего

    Как все надоело, сколько мне еще лежать так?
    
    Подумалось мне, но внезапно вдали послышался голос, я не мог разобрать слов, постепенно он становился все более отчетливее
    """
    menu:

        "Подойти ближе":
            jump right_answer
        "Остаться":
            jump false_answer
label right_answer:
    strange_girl "как ... тебя ... зовут?"
    $ player_name = renpy.input("", default="", length = 15)
    $ player_name = player_name.strip() or "Me"
    "Мы еще увидимся, [player_name]"
    player_name "Я очнулся."
    jump chapter1
label false_answer:
    "Ты решил остаться"
    return

label chapter1:

    #новый фон
    #новое музло




    