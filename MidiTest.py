import rtmidi

midi_in = rtmidi.MidiIn()

available_ports = midi_in.get_ports()

if available_ports:
    print("Available MIDI input ports:")
    for i, port_name in enumerate(available_ports):
        print(f"Port {i}: {port_name}")
else:
    print("No MIDI input ports found.")


import pygame
import rtmidi

# MIDI settings
MIDI_PORT_NAME = "--ENTER NAME OF MIDI DEVICE--"



# Pygame settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.Font(None, FONT_SIZE)

midi_in = rtmidi.MidiIn()

# Find the MIDI input port by name
available_ports = midi_in.get_ports()
port_index = None

for i, port_name in enumerate(available_ports):
    if MIDI_PORT_NAME in port_name:
        port_index = i
        break

if port_index is None:
    print(f"Could not find MIDI port: {MIDI_PORT_NAME}")
    exit()

# Open the MIDI input port
midi_in.open_port(port_index)

print(f"Connected to MIDI port: {MIDI_PORT_NAME}")

# Process MIDI messages
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    message = midi_in.get_message()

    if message:
        midi_event, _ = message

        # Display MIDI event
        print(f"MIDI Event: {midi_event}")

        # Render text
        text_surface = font.render(f"MIDI Event: {midi_event}", True, FONT_COLOR)

        # Clear the window
        window.fill((0, 0, 0))

        # Draw text in the center of the window
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(text_surface, text_rect)

        # Update the display
        pygame.display.update()
        pygame.display.flip()
