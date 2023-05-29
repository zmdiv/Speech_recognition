pip install openai-whisper

import whisper


def audio_to_text(model='base'):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe('path_to_mp3_file')

    with open(f'transcripted_{model}.txt', 'w') as file:
        file.write(result['text'])


def main():
    models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}

    for k, v in models.items():
        print(f'{k}:{v}')

    model = int(input('Choose a model to apply, enter the number from 1 to 5: '))

    if model not in models.keys():
        raise KeyError(f'The {model} is not available, please enter the number from 1 to 5')

    print('The process is on... please wait')
    speech_recognition(model=models[model])


if __name__ == '__main__':
    main()
