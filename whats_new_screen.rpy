init python:
    def get_file_contents(file_path: str):
        with open(file_path, "r") as f:
            return f.read()

default persistent.previous_whats_new = None

screen whats_new():
    modal True
    style_prefix "whats_new"

    python:
        with open(os.path.join(config.gamedir, "whats_new", "whats-new.txt"), "r") as f:
            file_contents = f.read()

        title, learn_more_link, description = re.findall('".+"', file_contents)

    add "darker_80"

    frame:
        background Frame("gui/whats-new/background.webp")
        xysize (500, 758)
        align (0.5, 0.5)
        padding (20, 20)

        viewport:
            mousewheel True
            draggable True
            align (0.5, 0.5)

            vbox:
                spacing 10
                text "What's New:" xalign 0.5 bold True
                text description size 18

                if achievement.steam and achievement.steam.dlc_installed(1929620):
                    null height 50

                    text "Deluxe Content:"
                    text "How to get DLC content" bold True
                    text "1. Right click \"College Kings 2\" in your Steam Library and select \"Properties\".\n2. Under the \"Local Files\" tab, select \"Browse Local Files\".\n3. Within the local files, locate a folder called \"deluxe_content\."
                    textbutton "Or Click HERE":
                        action Function(open_deluxe_folder)

                    null height 25

    button action Hide()

    textbutton "Exit":
        action Hide()
        xpos 20
        yalign 1.0
        yoffset -20
        text_size 100
        text_bold True

    on "hide" action SetVariable("persistent.previous_whats_new", dialogue)

style whats_new_text is text