default persistent.previous_whats_new = None

screen whats_new():
    style_prefix "whats_new"

    python:
        whats_new_file_path = [file for file in renpy.list_files() if file == "whats_new/whats-new.txt"][0]

        with renpy.file(whats_new_file_path, "utf-8") as f:
            file_contents = f.read()

        matches = list(re.finditer('"', file_contents))
        title = file_contents[matches[0].end() : matches[1].start()]
        button_text = file_contents[matches[2].end() : matches[3].start()]
        button_link = file_contents[matches[4].end() : matches[5].start()]
        description = file_contents[matches[6].end() : matches[7].start()]

    add "darker_80"

    button action Hide()

    button:
        background "whats_new/images/background.png"
        xysize (1412, 776)
        align (0.5, 0.5)
        padding (75, 75)
        action Hide()

        textbutton "X":
            action Hide()
            xalign 1.0
            text_size 42

        vbox:
            yalign 1.0
            xsize 625
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

    on "hide" action SetVariable("persistent.previous_whats_new", file_contents)

style whats_new_title is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    size 40

style whats_new_text is text:
    font "fonts/Effra-Regular.ttf"
    size 18

style whats_new_button_text is text:
    font "fonts/BebasNeue-Regular.ttf"
    size 32
    yoffset 5