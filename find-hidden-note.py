import numpy as np
import matplotlib.pyplot as plt

SAMPLING_RATE = 44100 # samples per second
DURATION = 1
NUM_SAMPLES = SAMPLING_RATE * DURATION
NOISE_AMPLITUDE = 2.0
SIGNAL_AMPLITUDE = 0.5
FREQUENCY = 440 # A4

# generate the time (x) axis
t = np.linspace(0, DURATION, NUM_SAMPLES, endpoint=False)

# generate hidden A4 note at 440HZ (pure sine wave)
# 5G Signal example
signal_wave = SIGNAL_AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t)

dataset_x = [] # will hold signal data
dataset_y = [] # will hold labels (0 for noise & 1 for signal)

SAMPLES = 1000

# generate all samples of noise+signal
for s in range(SAMPLES):
    noise_array = np.random.randn(NUM_SAMPLES) * NOISE_AMPLITUDE
    if s < SAMPLES // 2: # first 500 iterations will add only noise to dataset labeled with 0
        dataset_x.append(noise_array)
        dataset_y.append(0)
    else:                # last 500 iterations will add only signals to dataset labeled with 1
        dataset_x.append(signal_wave)
        dataset_y.append(1)

noise_example = dataset_x[0]
signal_example = dataset_x[-1]

# Plot noise samples
# plt.plot(t[:200], noise_example[:200])
# plt.title("Noise")
# plt.xlabel("Time")
# plt.ylabel("Signal Data")
# plt.show()

# Plot noise + signal samples
# plt.plot(t[800:], signal_example[800:])
# plt.title("Signal")
# plt.xlabel("Time")
# plt.ylabel("Signal Data")
# plt.show()

# Convert signal from time domain to frequency domain with numpy's fft and abs value functions
# noise_frequency_domain = np.fft.fft(noise_example) # returns complex numbers (magnitude, phase info)
# noise_fft_magnitude = np.abs(noise_frequency_domain) # handles complex numbers
# Plot noise samples + FFT
# plt.plot(noise_fft_magnitude)
# plt.title("Noise + FFT")
# plt.xlabel("Frequency")
# plt.ylabel("Signal Data")
# plt.show()

# Convert signal from time domain to frequency domain with numpy's fft and abs value functions
# signal_frequency_domain = np.fft.fft(signal_example) # returns complex numbers (magnitude, phase info)
# signal_fft_magnitude = np.abs(signal_frequency_domain) # handles complex numbers
# Plot signal samples + FFT
# plt.plot(signal_fft_magnitude)
# plt.title("Signal + FFT")
# plt.xlabel("Time")
# plt.ylabel("Signal Data")
# plt.show()
