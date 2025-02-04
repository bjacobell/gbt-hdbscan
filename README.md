This repository contains my notebooks for a Breakthrough Listen project involving HDBSCAN for Green Bank Telescope data, 
titled "Anomaly Detection and RFI Classification with Unsupervised Learning in Narrowband Radio Technosignature Searches."
The acronym for the method is GLOBULAR (Grouping Low-frequency Observations By Unsupervised Learning After Reduction) clustering.
The pre-print is available here: https://arxiv.org/abs/2411.16556

We benchmark our method against the results of a 97-galaxy radio technosignature survey by Carmen Choza et al.: https://arxiv.org/abs/2312.03943

Our method builds on the following SETI code:
- Blimpy (Breakthrough Listen I/O Methods for Python): https://github.com/UCBerkeleySETI/blimpy
- turboSETI: https://github.com/UCBerkeleySETI/turbo_seti (tutorials by Elan Lavie available here: https://github.com/elanlavie/VoyagerTutorialRepository)
- setigen: https://github.com/bbrzycki/setigen

Most notebooks in this repository have short header documentation explaining their purpose. For quick reference:

- `parallel_param_pull.ipynb` calculates our 13 features for a data set of signals discovered by turboSETI (or a similar pipeline). It supersedes `parameter_pulling.ipynb` and `choza_iteration.ipynb`, which were scratch-work notebooks used to develop the feature list.
- `batch_hdbscan.ipynb`, `batch_hdbscan_choose_parameters.ipynb`, and `batch_hdbscan_iterative.ipynb` implement HDBSCAN in the batched configuration for improved runtime and clustering accuracy. `batch_hdbscan.ipynb` is primarily scratch work, while `batch_hdbscan_choose_parameters.ipynb` is used to choose hyperparameters for HDBSCAN, and `batch_hdbscan_iterative.ipynb` is primarily final code. Additionally, `hdbscanning.ipynb` is useful for testing HDBSCAN on a toy data set, and for feature importance analysis via random forests and Shapley values.
- `find_event_from_reduced_hits.ipynb` and `plot_event_from_reduced_hits.ipynb` implement the turboSETI FindEvent and PlotEvent routines for the post–GLOBULAR clustering hit set. (Read more in the turboSETI documentation here: https://turbo-seti.readthedocs.io/en/latest/)
- `plot_clustered_waterfalls_C23.ipynb` plots time-frequency snippets to help visualize clusters. It mostly supersedes `plot_clustered_waterfalls.ipynb`. `plot_small_batch_clusters.ipynb` uses a shorter version of this code to target specifically small clusters on a per-batch basis, i.e. before cross-batch matching.
- `param_analysis.ipynb` plots histograms to help analyze the feature space.
- `centroid_clustering_kmeans.ipynb` and `centroid_clustering_tsne.ipynb` contain scratch work related to our cross-batch cluster matching.
- `duplicate_check_examples.ipynb` demonstrates the duplicate hits in the Choza et al. (2024) data set and justifies their excision for this work. It supersedes `investigate_duplicates.ipynb`.
- `injection_script.ipynb` is for injecting synthetic signals with setigen. `RecoveryTest.py` is a modified version of a script by Carmen Choza and can also be used for this.
- `dat_deletion.ipynb` is for deleting non-anomalous hits from existing .dat files (after copying the files first).
- `blimpy_test.ipynb`, `turbo_seti_M31.ipynb`, and `test.ipynb` are intended as scratch-work notebooks. `blimpy_test.ipynb` is particularly useful for visualizing .h5 data, and `turbo_seti_M31.ipynb` for short turboSETI runs.
- `retrieve_anomalous_hits.ipynb` and `injection_visualization.ipynb` are mainly obsolete with their functionality accounted for in `parallel_param_pull.ipynb` and `turbo_seti_M31.ipynb`, respectively.
- `signal_bandwidth_testing.ipynb` and `shap_demo.ipynb` are toy-model notebooks for testing Bryan Brzycki's signal bandwidth helper functions and the SHAP package's Shapley value estimators, respectively. 
- `ata_remote_observation.ipynb`, `bliss_M31.ipynb`, and `tseti_script.py` are for incidental projects done alongside my GLOBULAR clustering work, not directly in pursuit of GLOBULAR clustering on the Choza et al. (2024) L-band data set, but with sufficiently relevant code that I leave them in this repository.

Comment-style documentation is present throughout, but not ubiquitous; the notebooks are not meant to constitute a library or a set of tutorials. 
If you're interested and need help finding a specific bit of code, feel free to reach out!
