import pyttsx3

def text_to_speech(text, voice_type='female', rate=150, volume=1.0):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties for speech rate and volume
    engine.setProperty('rate', rate)  # Speed of speech (higher is faster)
    engine.setProperty('volume', volume)  # Volume (0.0 to 1.0)

    # Get the list of available voices
    voices = engine.getProperty('voices')

    # Select the voice based on the specified type
    if voice_type == 'female':
        engine.setProperty('voice', voices[1].id)  # Female voice (index might differ based on system)
    elif voice_type == 'male':
        engine.setProperty('voice', voices[0].id)  # Male voice (index might differ based on system)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def main():
    print("Text-To-Speech Converter Project by J Hannibal William")
    
    # Ask for the voice type
    print("Please choose a voice type:")
    print("1. Male")
    print("2. Female")
    
    voice_choice = input("Enter 1 or 2: ")

    if voice_choice == '1':
        voice_type = 'male'
    elif voice_choice == '2':
        voice_type = 'female'
    else:
        print("Invalid choice. Defaulting to male voice.")
        voice_type = 'male'

    # Ask for speech speed (rate)
    try:
        rate = int(input("Enter speech rate (default is 150, higher is faster): ") or 150)
    except ValueError:
        print("Invalid rate! Using default rate 150.")
        rate = 150

    # Ask for volume level (0.0 to 1.0)
    try:
        volume = float(input("Enter volume level (default is 1.0, range 0.0 to 1.0): ") or 1.0)
        if volume < 0.0 or volume > 1.0:
            print("Invalid volume! Using default volume 1.0.")
            volume = 1.0
    except ValueError:
        print("Invalid volume! Using default volume 1.0.")
        volume = 1.0

    # Get the text input from the user
    text = input("Enter the text you want to convert to speech: ")

    # Convert the text to speech with the selected options
    text_to_speech(text, voice_type, rate, volume)

if __name__ == "__main__":
    main()
