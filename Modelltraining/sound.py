import pyaudio
import numpy as np
import scipy.signal as signal

# Sampling-Rate und Dauer
rate = 44100
duration = 0.1  # Sekunden
n_samples = int(rate * duration)


# Erstellen eines Bandpassfilters mit einer Frequenzabstufung
def create_filter():
    nyquist = rate / 2.0
    low_cutoff = 30.0 / nyquist  # Frequenz bei 30Hz
    high_cutoff = 400.0 / nyquist  # Frequenz bei 400Hz

    # Design eines Bandpassfilters (passiert nur Frequenzen zwischen 30Hz und 400Hz)
    b, a = signal.butter(2, [low_cutoff, high_cutoff], btype='bandpass', analog=True)
    return b, a


# Initialisieren von PyAudio
p = pyaudio.PyAudio()

# Erstellen des Bandpassfilters
b, a = create_filter()


# Funktion für das Generieren von weißem Rauschen
def generate_noise():
    noise = np.random.uniform(-1, 1, n_samples)
    return noise


# Stream-Callback-Funktion
def callback(in_data, frame_count, time_info, status):
    noise = generate_noise()

    # Anwenden des Bandpassfilters auf das weiße Rauschen
    filtered_noise = signal.lfilter(b, a, noise)

    # Umwandeln des Arrays in Byte-Daten, die pyaudio versteht
    out_data = (filtered_noise * 32767).astype(np.int16).tobytes()

    return (out_data, pyaudio.paContinue)


# Alle verfügbaren Audio-Geräte auflisten
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']} - {device_info['maxOutputChannels']} channels")

# Beispiel: Ausgabe für die Auswahl eines Geräts
device_index = int(input("Wählen Sie das gewünschte Ausgabegerät (Indexnummer): "))


# Öffnen des Streams
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=rate,
                output=True,
                stream_callback=callback,
                output_device_index=device_index)

# Starten des Streams
stream.start_stream()

# Solange der Stream läuft, weiter rauschenden Sound abspielen
try:
    while stream.is_active():
        pass
except KeyboardInterrupt:
    print("Stream wird beendet...")
    stream.stop_stream()
    stream.close()
    p.terminate()
