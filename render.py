
txt = open("package/templates/index.html", 'r').read()


import datetime

x = datetime.datetime.now().strftime("%b %-d, %Y at %I:%M %p")


with open("site/index.html", "w") as of:
    of.write(txt.replace("NOW", x))
