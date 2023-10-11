default persistent.previous_whats_new = None

screen whats_new(data=""):
    style_prefix "whats_new"

    python:
        title, button_text, button_link, description = re.findall(r'"(.*?)"', data, re.DOTALL)

    add "darker_80"

    button action Hide()

    button:
        background "whats_new/images/background.png"
        xysize renpy.load_surface("whats_new/images/background.png").get_size()
        align (0.5, 0.5)
        padding (50, 50)
        action Hide()

        textbutton "X":
            action Hide()
            xalign 1.0
            text_size 42

        vbox:
            yalign 1.0
            xsize 0.65
            spacing 5

            text title:
                style "whats_new_title"
            text description

        button:
            background "whats_new/images/button_background.png"
            hover_background "whats_new/images/button_background_hover.png"
            action OpenURL(button_link)
            align (1.0, 1.0)
            xysize (332, 124)

            text button_text:
                style "whats_new_button_text"
                align (0.5, 0.5)

    on "hide" action SetVariable("persistent.previous_whats_new", data)

style whats_new_title is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    size 40
    outlines [(0.5, "#000")]

style whats_new_text is text:
    font "fonts/Effra-Regular.ttf"
    size 22
    outlines [(0.1, "#000")]

style whats_new_button_text is text:
    font "fonts/BebasNeue-Regular.ttf"
    size 32
    yoffset 5