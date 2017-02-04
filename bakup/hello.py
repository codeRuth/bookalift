"""Cloud Foundry test"""
from flask import Flask
import cf_deployment_tracker
import os
from telegram.ext import Updater

# Emit Bluemix deployment event
cf_deployment_tracker.track()

# app = Flask(__name__)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('PORT', 8080))


# @app.route('/')
# def hello_world():
#     return 'Hello World! I am running on port ' + str(port)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=port)
    print "hello"
    TOKEN = "319105749:AAHndfxb2dwkAIsnGmANl3KIJZSztzyVFas"
    updater = Updater(TOKEN)
    updater.start_webhook(listen="0.0.0.0", port=port, url_path=TOKEN)
    updater.bot.setWebhook("https://bookalift.mybluemix.net/" + TOKEN)
    print updater.bot.get_webhook_info
    updater.idle()
