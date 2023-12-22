# speechToText
personal project for simple speech to text convertion inspired by [FUTO VoiceInput](https://gitlab.futo.org/alex/voiceinput) and team need for speech to text (polish) with build in en->pl translation.
---
Digging through voiceinput code directed me to [OpenAI Whisper](https://github.com/openai/whisper).
After further research of Python modules I picked up [sounddevice](https://github.com/spatialaudio/python-sounddevice/) and [soundfile](https://python-soundfile.readthedocs.io/en/0.11.0/) to record and save speech samples.
Whisper did all the heavy lifting. Medium model was needed for proper polish language recognition. Real time conversion was not valiable with medium model on the development PC.
Time spent: one day
