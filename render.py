from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
                 loader=PackageLoader('package', 'templates'),
                 autoescape=select_autoescape(['html', 'xml'])
                 )

template = env.get_template('index.html')

import datetime

x = datetime.datetime.now().strftime("%b %-d, %Y at %I:%M %p")


with open("site/index.html", "w") as of:
    of.write(template.render(updated=x))
