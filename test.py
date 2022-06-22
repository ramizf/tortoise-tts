from flask import Flask, render_template, request , send_file
from werkzeug.utils import secure_filename
import os

# import torch
# import torchaudio
# import torch.nn as nn
# import torch.nn.functional as F
# # import IPython
# from tortoise.api import TextToSpeech

app = Flask(__name__)
app.config["UPLOAD_PATH"] = "./tortoise/voices/custom/"
CUSTOM_VOICE_NAME = "custom"
#tts = TextToSpeech()
@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploaded', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            #f = request.files['file']
            #f.save(secure_filename(f.filename))
            f.save(os.path.join(app.config["UPLOAD_PATH"],f.filename))
        return render_template('upload.html',msg='Done!')
    return render_template('upload.html', 'Please Choose a file')

@app.route('/preset_and_text', methods=['POST', 'GET'])
def select():
    preset = request.form.get('preset')
    text = request.form['text']
    # voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
    # gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
    #                           preset=preset)
    # torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)
    # return render_template('upload.html')
    path = f'generated-{CUSTOM_VOICE_NAME}.wav'
    return send_file(path, as_attachment=True)


# @app.route('/input_text', methods=['POST', 'GET'])
# def input_text():
#     text = request.form['text']
#     return text

if __name__ == '__main__':
    app.run(debug=True)