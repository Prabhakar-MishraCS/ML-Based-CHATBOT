from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
from nltk import word_tokenize,sent_tokenize
import ssl

try:
    create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = create_unverified_https_context
#nltk.download()

app = Flask(__name__)

PrabhuBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(PrabhuBot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get/")
def get_bot_response():
    userText = request.args.get('msg')
    return str(PrabhuBot.get_response(userText))


if __name__ == "__main__":
    app.run()
