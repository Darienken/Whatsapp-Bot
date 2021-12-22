import bot_methods as bot

def func_to_search_chat(method):

    chat=method.search_chat("Nazareth")
    if chat == False:
        chat = method.search_by_bar("Nazareth")
    if chat:
        method.send_msg("https://www.w3schools.com/cssref/css_selectors.asp")
        chat="Mensaje Enviado"
    return chat

#nomenclatura

if __name__ == "__main__":
    app=bot.whatsbot("driver/chromedriver.exe")
    print(func_to_search_chat(app))