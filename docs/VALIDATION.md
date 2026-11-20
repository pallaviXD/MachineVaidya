# Validation Plan

MachineVaidya’s detection capabilities will be benchmarked against three publicly‑available datasets that are standard in the predictive‑maintenance community.

## Datasets
| Dataset | Source | Relevance |
|---|---|---|
| **CWRU Bearing Data Center** | Case Western Reserve University | Motor‑bearing faults with varying severity. |
| **NASA IMS (Intelligent Maintenance Systems) Bearing** | NASA Prognostics Center | Early‑stage bearing degradation, useful for lead‑time analysis. |
| **MIMII (Machine Identification Monitoring) Acoustic** | Kyoto University | Real‑world machine‑sound recordings, includes anomalous motor sounds. |

## Evaluation Metrics
* **Detection latency** – Time from fault onset to first alert (seconds).
* **False‑alarm rate** – Percentage of alerts raised during normal operation.
* **Precision / Recall** – On labelled segments where ground‑truth fault timestamps are provided.
* **Lead‑time** – How early the system signals a degradation trend before a catastrophic failure, measured where the dataset includes a failure endpoint.
* **Resource usage** – CPU, memory and power consumption on the companion device (Raspberry Pi or laptop).

## Experimental Procedure
1. **Data ingestion** – Convert each dataset’s raw sensor streams into the same feature set used by MachineVaidya (RMS, FFT band‑energy, etc.).
2. **Baseline training** – Use the first 5 minutes of each recording (assumed healthy) to fit the per‑machine baseline model.
3. **Online detection** – Run the Isolation Forest detector on a sliding window (1‑second step) and record alerts.
4. **Metric calculation** – Compare alert timestamps with ground‑truth fault intervals to compute latency, precision, recall and false‑alarm rate.
5. **Resource profiling** – Measure CPU and memory on the companion host during the run.

## Success Criteria (Phase 6)
| Metric | Target |
|---|---|
| Detection latency | ≤ 2 seconds |
| False‑alarm rate | ≤ 5 % |
| Precision (labelled faults) | ≥ 80 % |
| Recall (labelled faults) | ≥ 70 % |
| CPU usage on Raspberry Pi 4 | ≤ 30 % of a single core |

No results are available yet; the experiments will be executed after the hardware prototype is stable (Phase 5).
