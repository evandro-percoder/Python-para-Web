# -*- coding: iso-8859-1 -*-

import wolframalpha
import wikipedia
import requests

app_id = "virtu@l_@ssitent"
client = wolframalpha.Client(app_id)

while True:
    raw_input = input('Make your question: \n -->> ')
    wikipedia.set_lang('pt')# configurar com o idioma desejado.
    print(wikipedia.summary(raw_input))
    print('\n================== ************ ==================')