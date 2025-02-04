import numpy as np
import blimpy as bl
import matplotlib.pyplot as plt
import pandas as pd
import turbo_seti
from turbo_seti.find_doppler.find_doppler import FindDoppler
import glob
import os

### Script runs turboSETI FindDoppler search to generate .dat files for hit analysis.
### Does not incorporate FindEvent search.

DATADIR = '/datag/users/benjb/AGBT24B_999_13_copies/'

h5_list = sorted(glob.glob(os.path.join(DATADIR, '*.h5')))

beam_1_h5s = h5_list[::2]
beam_2_h5s = h5_list[1::2]
for i in range(10):
    print(beam_1_h5s[i])
    print(beam_2_h5s[i])
print(len(beam_1_h5s))
print(len(beam_2_h5s))

for i in range(len(beam_1_h5s)):

    print(f'{i+1} out of {len(beam_1_h5s)}')

    file1 = beam_1_h5s[i]
    file2 = beam_2_h5s[i]

    doppler = FindDoppler(file1,
                        max_drift = 4, # Max drift rate = 4 Hz/second
                        snr = 10,      # Minimum signal to noise ratio = 10:1
                        out_dir = DATADIR # This is where the turboSETI output files will be stored.
                        )
    doppler.search()
    doppler = FindDoppler(file2,
                        max_drift = 4, # Max drift rate = 4 Hz/second
                        snr = 10,      # Minimum signal to noise ratio = 10:1
                        out_dir = DATADIR # This is where the turboSETI output files will be stored.
                        )
    doppler.search()

    dat1 = file1[:-2] + 'dat'
    dat2 = file1[:-2] + 'dat'

    df1 = pd.read_table(dat1, sep='\s+', names=['Top_Hit_#','Drift_Rate','SNR','Uncorrected_Frequency','Corrected_Frequency',
                                            'Index', 'freq_start', 'freq_end', 'SEFD', 'SEFD_freq', 'Coarse_Channel_Number', 
                                            'Full_number_of_hits'], skiprows=9)
    df2 = pd.read_table(dat2, sep='\s+', names=['Top_Hit_#','Drift_Rate','SNR','Uncorrected_Frequency','Corrected_Frequency',
                                            'Index', 'freq_start', 'freq_end', 'SEFD', 'SEFD_freq', 'Coarse_Channel_Number', 
                                            'Full_number_of_hits'], skiprows=9)
    f1 = df1['Uncorrected_Frequency'].values
    d1 = df1['Drift_Rate'].values
    s1 = df1['SNR'].values
    f2 = df2['Uncorrected_Frequency'].values
    d2 = df2['Drift_Rate'].values
    s2 = df2['SNR'].values

    plt.hist(f1, bins=50, c='grey')
    plt.xlabel('frequency [MHz]')
    plt.title('beam 1 frequencies')
    plt.yscale('log')
    plt.savefig(DATADIR + 'beam_1_freqs_' + os.path.basename(file1)[:-2] + 'pdf', bbox_inches='tight')
    plt.clf()

    plt.hist(d1, bins=50, c='grey')
    plt.xlabel('drift rate [Hz/s]')
    plt.title('beam 1 drift rates')
    plt.yscale('log')
    plt.savefig(DATADIR + 'beam_1_drifts_' + os.path.basename(file1)[:-2] + 'pdf', bbox_inches='tight')
    plt.clf()

    plt.hist(f2, bins=50, c='grey')
    plt.xlabel('frequency [MHz]')
    plt.title('beam 2 frequencies')
    plt.yscale('log')
    plt.savefig(DATADIR + 'beam_2_freqs_' + os.path.basename(file2)[:-2] + 'pdf', bbox_inches='tight')
    plt.clf()

    plt.hist(d1, bins=50, c='grey')
    plt.xlabel('drift rate [Hz/s]')
    plt.title('beam 1 drift rates')
    plt.yscale('log')
    plt.savefig(DATADIR + 'beam_2_drifts_' + os.path.basename(file2)[:-2] + 'pdf', bbox_inches='tight')
    plt.clf()