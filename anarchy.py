import random
import shutil
tags = {
    "ZBJ": "Baja California",
    "ZMX": "Mexico",
    "ZLL": "Lowlands",
    "ZFR": "Quebec",
    "ZON": "Ontario",
    "ZPR": "Prairies",
    "ZBC": "British Columbia"
}

with open("localisation/english/anarchy_l_english.yml", 'w', encoding="utf-8") as file:
    file.write("\ufeffl_english:\n")

for tag in tags:
    name = tags[tag]
    with open(f"history/countries/{tag} - {name}.txt", 'w', encoding="utf-8") as file:
        file.write(f"capital = 1\nanarchy_tag_setup = yes\n")
    with open("localisation/english/anarchy_l_english.yml", 'a', encoding="utf-8") as file:
        file.write(f""" {tag}: "{name} Anarchy"
 {tag}_DEF: "the {name} Anarchy"
 {tag}_ADJ: "{name} Anarchy"
""")
    rc = random.randint(0, 20)
    gc = random.randint(0, 20)
    bc = random.randint(0, 20)
    with open("common/countries/colors.txt", 'a', encoding="utf-8") as file:
        file.write(f"""
{tag} = {{
\tcolor = rgb {{ {rc} {gc} {bc} }}
\tcolor_ui = rgb {{ {rc} {gc} {bc} }}
}}
""")
    shutil.copyfile("gfx/flags/blank.tga", f"gfx/flags/{tag}.tga")
    shutil.copyfile("gfx/flags/medium/blank.tga", f"gfx/flags/medium/{tag}.tga")
    shutil.copyfile("gfx/flags/small/blank.tga", f"gfx/flags/small/{tag}.tga")