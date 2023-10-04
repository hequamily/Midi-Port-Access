import mido

def process_midi_message(message):
    # Process MIDI messages here
    print(message)

def main():
    # Set up MIDI input
    input_name = 'Your MIDI Keyboard' 
    with mido.open_input(input_name) as port:
        print(f"Using MIDI input: {port}")

        # Main loop
        while True:
            for message in port.iter_pending():
                process_midi_message(message)

if __name__ == '__main__':
    main()
