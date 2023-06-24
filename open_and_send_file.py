import os


def open_and_send_file(arg_path, chat_id, bot):
        with open(os.path.join(arg_path), 'rb') as file:
            bot.send_photo(chat_id, photo=file)
