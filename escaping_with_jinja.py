from jinja2 import Template


data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Артём')

print(msg)

link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

tm_2 = Template('{{ link | e }}')

msg_2 = tm_2.render(link=link)

print(msg_2)
