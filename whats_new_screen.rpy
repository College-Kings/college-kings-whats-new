init python:
    def get_file_contents(file_path: str):
        with open(file_path, "r") as f:
            return f.read()

default persistent.previous_whats_new = None

screen whats_new():
    style_prefix "whats_new"

    python:
        with open(os.path.join(config.gamedir, "whats_new", "whats-new.txt"), "r") as f:
            file_contents = f.read()

        matches = list(re.finditer('"', file_contents))
        title = file_contents[matches[0].end() : matches[1].start()]
        learn_more_link = file_contents[matches[2].end() : matches[3].start()]
        description = file_contents[matches[4].end() : matches[5].start()]

    add "darker_80"

    button action Hide()

    button:
        background "whats_new/images/background.png"
        xysize (1412, 776)
        align (0.5, 0.5)
        padding (100, 100)
        action Hide()

        textbutton "X":
            action Hide()
            xalign 1.0
            text_size 42

        vbox:
            yalign 1.0
            xsize 625
            spacing 10

            text title:
                style "whats_new_title"
            text description

        imagebutton:
            idle "whats_new/images/learn_more.png"
            action OpenURL(learn_more_link)
            align (1.0, 1.0)

    on "hide" action SetVariable("persistent.previous_whats_new", hash(file_contents))

style whats_new_title is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    size 40

style whats_new_text is text:
    font "fonts/Effra-Regular.ttf"
    size 23
