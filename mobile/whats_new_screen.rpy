default persistent.previous_whats_new = None

screen whats_new(data=""):
    style_prefix "whats_new"
    variant "mobile"

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

    on "hide" action SetVariable("persistent.previous_whats_new", data)