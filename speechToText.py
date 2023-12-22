# -*- coding: utf-8 -*-

import whisper

# load the model
model = whisper.load_model('medium')

# transcribe the recording

result = model.transcribe('recording.wav', fp16=False, language= 'pl')

# transcription with translation
# result = model.transcribe('recording.wav', fp16=False, language= 'pl', task = 'translate', initial_prompt = 'MBE, ARPES')

# save and print the result
with open('recording_text.txt', 'w') as file:
    file.write(f'{result["text"]}')
print(f'{result["text"]}')