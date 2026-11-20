import os

assets_dir = r"C:\Users\PALLAVI M\Desktop\MachineVaidya\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. ARCHITECTURE DETAILED SVG
architecture_svg = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1200" y2="720" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#090B0D"/>
      <stop offset="100%" stop-color="#11161A"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#182026"/>
      <stop offset="100%" stop-color="#101519"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="subtleGlow">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="720" rx="16" fill="url(#bgGrad)" stroke="#1F2933" stroke-width="2"/>
  
  <!-- Grid overlay -->
  <g opacity="0.07" stroke="#94A3B8" stroke-width="1">
    <line x1="0" y1="80" x2="1200" y2="80"/>
    <line x1="0" y1="160" x2="1200" y2="160"/>
    <line x1="0" y1="240" x2="1200" y2="240"/>
    <line x1="0" y1="320" x2="1200" y2="320"/>
    <line x1="0" y1="400" x2="1200" y2="400"/>
    <line x1="0" y1="480" x2="1200" y2="480"/>
    <line x1="0" y1="560" x2="1200" y2="560"/>
    <line x1="0" y1="640" x2="1200" y2="640"/>
    <line x1="300" y1="0" x2="300" y2="720"/>
    <line x1="600" y1="0" x2="600" y2="720"/>
    <line x1="900" y1="0" x2="900" y2="720"/>
  </g>

  <!-- Title & Legend -->
  <text x="50" y="50" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700" letter-spacing="1">MACHINEVAIDYA · COMPLETE SYSTEM ARCHITECTURE &amp; DATA PIPELINE</text>
  <rect x="940" y="32" width="210" height="26" rx="13" fill="#1E293B" stroke="#334155"/>
  <circle cx="955" cy="45" r="4" fill="#10B981"/>
  <text x="968" y="49" fill="#94A3B8" font-family="sans-serif" font-size="11" font-weight="600">100% OFFLINE AIR-GAPPED</text>

  <!-- COLUMN 1: SENSOR ACQUISITION -->
  <rect x="40" y="80" width="240" height="600" rx="12" fill="url(#cardGrad)" stroke="#26333D" stroke-width="1.5"/>
  <rect x="40" y="80" width="240" height="42" rx="12" fill="#141B20"/>
  <text x="60" y="106" fill="#F59E0B" font-family="sans-serif" font-size="13" font-weight="700" letter-spacing="1">01 · SENSING &amp; HARVEST</text>

  <!-- Sensor item: Vibration -->
  <g transform="translate(56, 140)">
    <rect width="208" height="96" rx="8" fill="#0D1216" stroke="#26333D"/>
    <circle cx="24" cy="28" r="10" fill="#F59E0B" fill-opacity="0.15" stroke="#F59E0B"/>
    <text x="24" y="32" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">VIB</text>
    <text x="46" y="26" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">ADXL345 / Piezo</text>
    <text x="46" y="42" fill="#64748B" font-family="sans-serif" font-size="10">Tri-axial Acceleration · ±16g</text>
    <line x1="16" y1="56" x2="192" y2="56" stroke="#1E293B"/>
    <text x="16" y="74" fill="#94A3B8" font-family="monospace" font-size="9">Rate: 1.6 kHz · SPI / I2C</text>
    <text x="16" y="87" fill="#F59E0B" font-family="monospace" font-size="9">Target: Bearing / Misalignment</text>
  </g>

  <!-- Sensor item: Acoustic -->
  <g transform="translate(56, 250)">
    <rect width="208" height="96" rx="8" fill="#0D1216" stroke="#26333D"/>
    <circle cx="24" cy="28" r="10" fill="#38BDF8" fill-opacity="0.15" stroke="#38BDF8"/>
    <text x="24" y="32" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">MIC</text>
    <text x="46" y="26" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">INMP441 MEMS</text>
    <text x="46" y="42" fill="#64748B" font-family="sans-serif" font-size="10">High-SNR Acoustic Emission</text>
    <line x1="16" y1="56" x2="192" y2="56" stroke="#1E293B"/>
    <text x="16" y="74" fill="#94A3B8" font-family="monospace" font-size="9">Rate: 16-44.1 kHz · I2S Bus</text>
    <text x="16" y="87" fill="#38BDF8" font-family="monospace" font-size="9">Target: Gear Mesh / Friction</text>
  </g>

  <!-- Sensor item: Current -->
  <g transform="translate(56, 360)">
    <rect width="208" height="96" rx="8" fill="#0D1216" stroke="#26333D"/>
    <circle cx="24" cy="28" r="10" fill="#E2E8F0" fill-opacity="0.1" stroke="#94A3B8"/>
    <text x="24" y="32" fill="#E2E8F0" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">CUR</text>
    <text x="46" y="26" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">SCT-013 / Hall</text>
    <text x="46" y="42" fill="#64748B" font-family="sans-serif" font-size="10">Split-Core Non-Invasive CT</text>
    <line x1="16" y1="56" x2="192" y2="56" stroke="#1E293B"/>
    <text x="16" y="74" fill="#94A3B8" font-family="monospace" font-size="9">Rate: 1 kHz · ADC 12-bit</text>
    <text x="16" y="87" fill="#CBD5E1" font-family="monospace" font-size="9">Target: Stator / Overload</text>
  </g>

  <!-- Sensor item: Temperature -->
  <g transform="translate(56, 470)">
    <rect width="208" height="96" rx="8" fill="#0D1216" stroke="#26333D"/>
    <circle cx="24" cy="28" r="10" fill="#EF4444" fill-opacity="0.15" stroke="#EF4444"/>
    <text x="24" y="32" fill="#EF4444" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">TMP</text>
    <text x="46" y="26" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">DS18B20 Probe</text>
    <text x="46" y="42" fill="#64748B" font-family="sans-serif" font-size="10">Stainless Housing Contact</text>
    <line x1="16" y1="56" x2="192" y2="56" stroke="#1E293B"/>
    <text x="16" y="74" fill="#94A3B8" font-family="monospace" font-size="9">Rate: 1 Hz · 1-Wire Bus</text>
    <text x="16" y="87" fill="#EF4444" font-family="monospace" font-size="9">Target: Winding Heat / Seizure</text>
  </g>

  <rect x="56" y="584" width="208" height="74" rx="8" fill="#141B20" stroke="#334155" stroke-dasharray="3 3"/>
  <text x="160" y="612" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">CLIP-ON RETROFIT</text>
  <text x="160" y="628" fill="#94A3B8" font-family="sans-serif" font-size="10" text-anchor="middle">Zero factory re-wiring required</text>
  <text x="160" y="644" fill="#64748B" font-family="sans-serif" font-size="9" text-anchor="middle">Magnetic &amp; bolt clamp mounts</text>

  <!-- Connectors from Col 1 to Col 2 -->
  <path d="M 280 188 L 320 188" stroke="#F59E0B" stroke-width="2" stroke-linecap="round"/>
  <path d="M 280 298 L 320 298" stroke="#38BDF8" stroke-width="2" stroke-linecap="round"/>
  <path d="M 280 408 L 320 408" stroke="#94A3B8" stroke-width="2" stroke-linecap="round"/>
  <path d="M 280 518 L 320 518" stroke="#EF4444" stroke-width="2" stroke-linecap="round"/>

  <!-- COLUMN 2: ESP32 EDGE PRE-PROCESSING -->
  <rect x="320" y="80" width="250" height="600" rx="12" fill="url(#cardGrad)" stroke="#26333D" stroke-width="1.5"/>
  <rect x="320" y="80" width="250" height="42" rx="12" fill="#141B20"/>
  <text x="340" y="106" fill="#F59E0B" font-family="sans-serif" font-size="13" font-weight="700" letter-spacing="1">02 · ESP32 EDGE DSP</text>

  <g transform="translate(336, 140)">
    <rect width="218" height="80" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="26" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">Dual-Core Xtensa LX6</text>
    <text x="16" y="42" fill="#64748B" font-family="sans-serif" font-size="10">240 MHz · 520 KB SRAM · 4MB Flash</text>
    <line x1="16" y1="50" x2="202" y2="50" stroke="#1E293B"/>
    <text x="16" y="66" fill="#F59E0B" font-family="monospace" font-size="9">FreeRTOS Deterministic Tasks</text>
  </g>

  <!-- DSP Block 1: Buffer & Filter -->
  <g transform="translate(336, 235)">
    <rect width="218" height="95" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="700">CIRCULAR BUFFER &amp; FILTER</text>
    <text x="16" y="42" fill="#94A3B8" font-family="sans-serif" font-size="10">Hanning Windowing · 1024 pt</text>
    <text x="16" y="58" fill="#94A3B8" font-family="sans-serif" font-size="10">Bandpass: 10 Hz – 2.5 kHz</text>
    <text x="16" y="74" fill="#64748B" font-family="monospace" font-size="9">Low-latency DMA stream</text>
  </g>

  <!-- DSP Block 2: Fast Feature Extraction -->
  <g transform="translate(336, 345)">
    <rect width="218" height="150" rx="8" fill="#0D1216" stroke="#F59E0B" stroke-width="1.5" filter="url(#subtleGlow)"/>
    <text x="16" y="24" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="700">EDGE FEATURE EXTRACTION</text>
    <text x="16" y="44" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Time Domain: RMS, Peak, Crest</text>
    <text x="16" y="60" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Shape: Kurtosis, Skewness</text>
    <text x="16" y="76" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Spectral: 512-bin Radix-2 FFT</text>
    <text x="16" y="92" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Spectral Centroid &amp; Band Energy</text>
    <text x="16" y="108" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Motor Current Signature (MCSA)</text>
    <line x1="16" y1="120" x2="202" y2="120" stroke="#1E293B"/>
    <text x="16" y="136" fill="#F59E0B" font-family="monospace" font-size="9">Outputs 32-dim vector / sec</text>
  </g>

  <!-- DSP Block 3: Edge Packaging -->
  <g transform="translate(336, 510)">
    <rect width="218" height="148" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#E2E8F0" font-family="sans-serif" font-size="11" font-weight="700">LOCAL STREAM DISPATCH</text>
    <text x="16" y="44" fill="#94A3B8" font-family="sans-serif" font-size="10">Low-Energy BLE / Local Wi-Fi</text>
    <text x="16" y="62" fill="#94A3B8" font-family="sans-serif" font-size="10">Micro-SD Offline Fallback Buffer</text>
    <text x="16" y="80" fill="#64748B" font-family="sans-serif" font-size="10">Zero cloud transmission</text>
    <rect x="16" y="96" width="186" height="38" rx="6" fill="#141B20" stroke="#334155"/>
    <text x="109" y="114" fill="#10B981" font-family="monospace" font-size="10" font-weight="700" text-anchor="middle">PAYLOAD: ~120 Bytes/sec</text>
    <text x="109" y="127" fill="#64748B" font-family="sans-serif" font-size="8" text-anchor="middle">Ultra-light edge bandwidth</text>
  </g>

  <!-- Connectors from Col 2 to Col 3 -->
  <path d="M 570 420 L 610 420" stroke="#F59E0B" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="610,416 618,420 610,424" fill="#F59E0B"/>
  <text x="590" y="410" fill="#94A3B8" font-family="monospace" font-size="8" text-anchor="middle">WIFI / BLE</text>

  <!-- COLUMN 3: COMPANION HOST (AI & INFERENCE) -->
  <rect x="618" y="80" width="260" height="600" rx="12" fill="url(#cardGrad)" stroke="#26333D" stroke-width="1.5"/>
  <rect x="618" y="80" width="260" height="42" rx="12" fill="#141B20"/>
  <text x="638" y="106" fill="#F59E0B" font-family="sans-serif" font-size="13" font-weight="700" letter-spacing="1">03 · COMPANION AI NODE</text>

  <g transform="translate(634, 140)">
    <rect width="228" height="70" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">Local Gateway Runtime</text>
    <text x="16" y="40" fill="#64748B" font-family="sans-serif" font-size="10">Raspberry Pi 4 / Local Mini PC / Phone</text>
    <text x="16" y="56" fill="#10B981" font-family="monospace" font-size="9">Python 3.12 · FastAPI · SQLite</text>
  </g>

  <g transform="translate(634, 225)">
    <rect width="228" height="110" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="700">PER-MACHINE BASELINE MODEL</text>
    <text x="16" y="42" fill="#E2E8F0" font-family="sans-serif" font-size="10">• 15-Min Healthy Run Ingestion</text>
    <text x="16" y="58" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Operating State Clustering (Idle/Load)</text>
    <text x="16" y="74" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Mahalanobis / Covariance Matrix</text>
    <text x="16" y="92" fill="#F59E0B" font-family="monospace" font-size="9">Zero Pre-labeled Failure Data Needed</text>
  </g>

  <g transform="translate(634, 350)">
    <rect width="228" height="135" rx="8" fill="#0D1216" stroke="#F59E0B" stroke-width="1.5" filter="url(#subtleGlow)"/>
    <text x="16" y="24" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="700">UNSUPERVISED ANOMALY ENGINE</text>
    <text x="16" y="44" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Isolation Forest (iForest)</text>
    <text x="16" y="60" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Robust Covariance Estimator (Elliptic)</text>
    <text x="16" y="76" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Sliding-window Score Aggregation</text>
    <text x="16" y="92" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Future: Light 1D CNN Autoencoder</text>
    <line x1="16" y1="104" x2="212" y2="104" stroke="#1E293B"/>
    <text x="16" y="122" fill="#F59E0B" font-family="monospace" font-size="9">Calculates Anomaly Severity Index (0-100)</text>
  </g>

  <g transform="translate(634, 500)">
    <rect width="228" height="158" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="700">EXPLAINABILITY &amp; CONTEXT</text>
    <text x="16" y="44" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Feature Attribution / Tree Path</text>
    <text x="16" y="60" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Identifies Root Driver:</text>
    <text x="24" y="76" fill="#94A3B8" font-family="sans-serif" font-size="9">"High-Freq Vibration (+340%)"</text>
    <text x="24" y="90" fill="#94A3B8" font-family="sans-serif" font-size="9">"Current Unbalance (+18%)"</text>
    <line x1="16" y1="102" x2="212" y2="102" stroke="#1E293B"/>
    <text x="16" y="120" fill="#E2E8F0" font-family="sans-serif" font-size="10">Translates ML to Factory Language:</text>
    <text x="16" y="138" fill="#F59E0B" font-family="sans-serif" font-size="10" font-weight="600">"Bearing Friction Suspected"</text>
  </g>

  <!-- Connectors from Col 3 to Col 4 -->
  <path d="M 878 420 L 918 420" stroke="#F59E0B" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="918,416 926,420 918,424" fill="#F59E0B"/>
  <text x="898" y="410" fill="#94A3B8" font-family="monospace" font-size="8" text-anchor="middle">WS / REST</text>

  <!-- COLUMN 4: ACTION, UI & VOICE ALERTS -->
  <rect x="926" y="80" width="234" height="600" rx="12" fill="url(#cardGrad)" stroke="#26333D" stroke-width="1.5"/>
  <rect x="926" y="80" width="234" height="42" rx="12" fill="#141B20"/>
  <text x="946" y="106" fill="#F59E0B" font-family="sans-serif" font-size="13" font-weight="700" letter-spacing="1">04 · HUMAN-IN-LOOP ACTION</text>

  <g transform="translate(942, 140)">
    <rect width="202" height="100" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="600">PWA Mobile &amp; Desktop</text>
    <text x="16" y="42" fill="#64748B" font-family="sans-serif" font-size="10">No App Store install needed</text>
    <text x="16" y="58" fill="#94A3B8" font-family="sans-serif" font-size="10">Instant local dashboard on</text>
    <text x="16" y="72" fill="#94A3B8" font-family="sans-serif" font-size="10">shopfloor Wi-Fi</text>
    <text x="16" y="88" fill="#10B981" font-family="monospace" font-size="9">Latency &lt; 80ms</text>
  </g>

  <!-- Voice alerts block -->
  <g transform="translate(942, 255)">
    <rect width="202" height="120" rx="8" fill="#0D1216" stroke="#F59E0B" stroke-width="1.5" filter="url(#subtleGlow)"/>
    <text x="16" y="24" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="700">VERNACULAR AUDIO ALERTS</text>
    <text x="16" y="44" fill="#E2E8F0" font-family="sans-serif" font-size="10">Offline Local Speech Engine</text>
    <text x="16" y="62" fill="#38BDF8" font-family="sans-serif" font-size="10" font-weight="600">🔊 Kannada (ಕನ್ನಡ):</text>
    <text x="24" y="76" fill="#94A3B8" font-family="sans-serif" font-size="9">"ಮೋಟಾರ್ ಬೇರಿಂಗ್ ಪರೀಕ್ಷಿಸಿ"</text>
    <text x="16" y="92" fill="#F59E0B" font-family="sans-serif" font-size="10" font-weight="600">🔊 Hindi (हिंदी):</text>
    <text x="24" y="106" fill="#94A3B8" font-family="sans-serif" font-size="9">"मोटर बेयरिंग में असामान्य कंपन"</text>
  </g>

  <!-- Maintenance action block -->
  <g transform="translate(942, 390)">
    <rect width="202" height="135" rx="8" fill="#0D1216" stroke="#26333D"/>
    <text x="16" y="24" fill="#E2E8F0" font-family="sans-serif" font-size="11" font-weight="700">MAINTENANCE WORKFLOW</text>
    <text x="16" y="44" fill="#94A3B8" font-family="sans-serif" font-size="10">• Recommended window (e.g. 48h)</text>
    <text x="16" y="60" fill="#94A3B8" font-family="sans-serif" font-size="10">• Downtime cost estimator</text>
    <text x="16" y="76" fill="#94A3B8" font-family="sans-serif" font-size="10">• Spare part checklist</text>
    <line x1="16" y1="88" x2="186" y2="88" stroke="#1E293B"/>
    <text x="16" y="106" fill="#F59E0B" font-family="sans-serif" font-size="9" font-weight="600">NEVER AUTONOMOUS STOP</text>
    <text x="16" y="120" fill="#64748B" font-family="sans-serif" font-size="8">Owner holds final decision</text>
  </g>

  <g transform="translate(942, 540)">
    <rect width="202" height="118" rx="8" fill="#141B20" stroke="#334155"/>
    <text x="16" y="26" fill="#10B981" font-family="sans-serif" font-size="11" font-weight="700">SHOPFLOOR IMPACT</text>
    <text x="16" y="48" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Predict 3-5 days in advance</text>
    <text x="16" y="66" fill="#E2E8F0" font-family="sans-serif" font-size="10">• Avoid 12-24h lost shift</text>
    <text x="16" y="84" fill="#E2E8F0" font-family="sans-serif" font-size="10">• ₹15,000–50,000 saved / incident</text>
    <text x="16" y="102" fill="#F59E0B" font-family="sans-serif" font-size="9" font-weight="600">ROI achieved on 1st catch</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture-detailed.svg"), "w", encoding="utf-8") as f:
    f.write(architecture_svg)

print("Saved architecture-detailed.svg")

# 2. SIGNAL ANALYSIS SVG (Healthy vs Anomaly comparison with FFT, Kurtosis, and MCSA)
signal_svg = '''<svg width="1200" height="600" viewBox="0 0 1200 600" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardGrad2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#182026"/>
      <stop offset="100%" stop-color="#101519"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1200" height="600" rx="16" fill="#090B0D" stroke="#1F2933" stroke-width="2"/>
  
  <!-- Title -->
  <text x="50" y="48" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" letter-spacing="1">THE MACHINE'S SIGNATURE · TIME DOMAIN WAVEFORMS &amp; SPECTRAL DECOMPOSITION</text>
  <text x="50" y="70" fill="#94A3B8" font-family="sans-serif" font-size="12">Real-time transformation from raw sensor voltages to explainable anomaly markers</text>

  <!-- LEFT PANEL: HEALTHY SIGNATURE -->
  <rect x="40" y="90" width="545" height="470" rx="12" fill="url(#cardGrad2)" stroke="#1E293B" stroke-width="1.5"/>
  <rect x="40" y="90" width="545" height="38" rx="12" fill="#0F172A"/>
  <circle cx="62" cy="109" r="5" fill="#38BDF8"/>
  <text x="76" y="113" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1">STATE A: LEARNED HEALTHY BASELINE (NOMINAL RUN)</text>

  <!-- Healthy Waveform Box -->
  <g transform="translate(60, 140)">
    <rect width="505" height="130" rx="8" fill="#0B0F12" stroke="#1E293B"/>
    <text x="16" y="24" fill="#94A3B8" font-family="sans-serif" font-size="11" font-weight="600">Time-Domain Vibration (Tri-axial Accel)</text>
    <text x="350" y="24" fill="#10B981" font-family="monospace" font-size="10">RMS: 0.28g · Kurt: 2.94</text>
    <!-- Smooth periodic sine-like curve -->
    <path d="M 16 75 C 30 55, 45 95, 60 75 C 75 55, 90 95, 105 75 C 120 55, 135 95, 150 75 C 165 55, 180 95, 195 75 C 210 55, 225 95, 240 75 C 255 55, 270 95, 285 75 C 300 55, 315 95, 330 75 C 345 55, 360 95, 375 75 C 390 55, 405 95, 420 75 C 435 55, 450 95, 465 75 C 475 60, 485 85, 490 75" fill="none" stroke="#38BDF8" stroke-width="2"/>
    <text x="16" y="118" fill="#64748B" font-family="monospace" font-size="9">Uniform cyclic amplitude · Gaussian bell distribution (Kurtosis ≈ 3.0)</text>
  </g>

  <!-- Healthy FFT Box -->
  <g transform="translate(60, 285)">
    <rect width="505" height="150" rx="8" fill="#0B0F12" stroke="#1E293B"/>
    <text x="16" y="24" fill="#94A3B8" font-family="sans-serif" font-size="11" font-weight="600">FFT Frequency Spectrum (0 Hz – 2.5 kHz)</text>
    <text x="340" y="24" fill="#38BDF8" font-family="monospace" font-size="10">Fundamental: 1X (29.5 Hz)</text>
    <!-- Frequency spectrum bars -->
    <line x1="30" y1="120" x2="480" y2="120" stroke="#1E293B"/>
    <!-- Peak 1X running speed -->
    <line x1="70" y1="120" x2="70" y2="45" stroke="#38BDF8" stroke-width="4"/>
    <text x="70" y="40" fill="#38BDF8" font-family="monospace" font-size="9" text-anchor="middle">1X (29.5Hz)</text>
    <!-- Peak 2X -->
    <line x1="140" y1="120" x2="140" y2="85" stroke="#38BDF8" stroke-width="3"/>
    <text x="140" y="80" fill="#64748B" font-family="monospace" font-size="8" text-anchor="middle">2X</text>
    <!-- Grass/Noise floor bars -->
    <line x1="200" y1="120" x2="200" y2="114" stroke="#334155" stroke-width="2"/>
    <line x1="260" y1="120" x2="260" y2="112" stroke="#334155" stroke-width="2"/>
    <line x1="320" y1="120" x2="320" y2="115" stroke="#334155" stroke-width="2"/>
    <line x1="380" y1="120" x2="380" y2="113" stroke="#334155" stroke-width="2"/>
    <line x1="440" y1="120" x2="440" y2="116" stroke="#334155" stroke-width="2"/>
    <text x="16" y="140" fill="#64748B" font-family="monospace" font-size="9">Dominant energy confined to motor rotation shaft speed (1X / 2X)</text>
  </g>

  <!-- Healthy Status Card -->
  <g transform="translate(60, 450)">
    <rect width="505" height="90" rx="8" fill="#0B1319" stroke="#10B981" stroke-width="1"/>
    <circle cx="28" cy="28" r="8" fill="#10B981"/>
    <text x="46" y="32" fill="#E2E8F0" font-family="sans-serif" font-size="12" font-weight="700">HEALTH SCORE: 98/100 · STABLE BASELINE</text>
    <text x="16" y="58" fill="#94A3B8" font-family="sans-serif" font-size="10">Operating current: 6.8 A (Stable) · Temperature: 48°C (Equilibrium)</text>
    <text x="16" y="74" fill="#64748B" font-family="sans-serif" font-size="9">Zero anomalous high-frequency energy detected in bearing bandwidth.</text>
  </g>

  <!-- RIGHT PANEL: ANOMALY SIGNATURE -->
  <rect x="615" y="90" width="545" height="470" rx="12" fill="url(#cardGrad2)" stroke="#D97706" stroke-width="1.5"/>
  <rect x="615" y="90" width="545" height="38" rx="12" fill="#1C140A"/>
  <circle cx="637" cy="109" r="5" fill="#F59E0B"/>
  <text x="651" y="113" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1">STATE B: INCIPIENT BEARING FAULT (EARLY DEVIATION)</text>

  <!-- Anomaly Waveform Box -->
  <g transform="translate(635, 140)">
    <rect width="505" height="130" rx="8" fill="#0B0F12" stroke="#261E14"/>
    <text x="16" y="24" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="600">Time-Domain Vibration (Shock Impulses &amp; Jitter)</text>
    <text x="350" y="24" fill="#EF4444" font-family="monospace" font-size="10">RMS: 1.18g · Kurt: 6.82</text>
    <!-- Spiky wave -->
    <path d="M 16 75 L 35 60 L 45 92 L 60 70 L 75 110 L 85 30 L 95 105 L 115 72 L 135 60 L 150 85 L 165 20 L 175 115 L 190 70 L 210 65 L 230 88 L 245 15 L 255 125 L 270 75 L 290 60 L 310 90 L 325 25 L 335 120 L 350 72 L 375 62 L 395 90 L 410 18 L 420 125 L 440 70 L 465 65 L 490 75" fill="none" stroke="#EF4444" stroke-width="2"/>
    <text x="16" y="118" fill="#EF4444" font-family="monospace" font-size="9">Sharp non-Gaussian transients (Kurtosis &gt; 6.0) indicative of metal impact</text>
  </g>

  <!-- Anomaly FFT Box -->
  <g transform="translate(635, 285)">
    <rect width="505" height="150" rx="8" fill="#0B0F12" stroke="#261E14"/>
    <text x="16" y="24" fill="#F59E0B" font-family="sans-serif" font-size="11" font-weight="600">FFT Frequency Spectrum (Bearing Fault Peaks)</text>
    <text x="330" y="24" fill="#F59E0B" font-family="monospace" font-size="10">BPFO Fault Spikes @ 1.2 kHz</text>
    <!-- Frequency spectrum bars -->
    <line x1="30" y1="120" x2="480" y2="120" stroke="#1E293B"/>
    <!-- Peak 1X running speed -->
    <line x1="70" y1="120" x2="70" y2="55" stroke="#38BDF8" stroke-width="3"/>
    <text x="70" y="50" fill="#94A3B8" font-family="monospace" font-size="8" text-anchor="middle">1X</text>
    <!-- High frequency fault harmonics -->
    <line x1="280" y1="120" x2="280" y2="35" stroke="#EF4444" stroke-width="4"/>
    <text x="280" y="28" fill="#EF4444" font-family="monospace" font-size="9" font-weight="700" text-anchor="middle">BPFO (1.2 kHz)</text>
    <line x1="340" y1="120" x2="340" y2="55" stroke="#F59E0B" stroke-width="3"/>
    <text x="340" y="48" fill="#F59E0B" font-family="monospace" font-size="8" text-anchor="middle">2x BPFO</text>
    <line x1="400" y1="120" x2="400" y2="70" stroke="#F59E0B" stroke-width="3"/>
    <text x="400" y="64" fill="#F59E0B" font-family="monospace" font-size="8" text-anchor="middle">3x BPFO</text>
    <text x="16" y="140" fill="#F59E0B" font-family="monospace" font-size="9">Massive energy emergence (+410%) in 1.0–2.2 kHz bearing race band</text>
  </g>

  <!-- Anomaly Status Card -->
  <g transform="translate(635, 450)">
    <rect width="505" height="90" rx="8" fill="#1C140A" stroke="#F59E0B" stroke-width="1"/>
    <circle cx="28" cy="28" r="8" fill="#F59E0B"/>
    <text x="46" y="32" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="700">ALERT: HEALTH SCORE 68/100 · ANOMALY DETECTED</text>
    <text x="16" y="58" fill="#E2E8F0" font-family="sans-serif" font-size="10">Root Driver: High-frequency impact spikes · Current Draw: 8.4A (+23% load)</text>
    <text x="16" y="74" fill="#94A3B8" font-family="sans-serif" font-size="9">Recommended: Schedule grease re-lubrication within next 48 operating hours.</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "signal-analysis.svg"), "w", encoding="utf-8") as f:
    f.write(signal_svg)

print("Saved signal-analysis.svg")

# 3. DEMO WALKTHROUGH SVG (4-step visual demo sequence)
demo_svg = '''<svg width="1200" height="380" viewBox="0 0 1200 380" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="380" rx="16" fill="#090B0D" stroke="#1F2933" stroke-width="2"/>
  
  <text x="50" y="45" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" letter-spacing="1">FOUR-STEP END-TO-END DEMONSTRATION WORKFLOW</text>
  <text x="50" y="65" fill="#94A3B8" font-family="sans-serif" font-size="12">From motor clip-on to vernacular voice action without touching cloud servers</text>

  <!-- STEP 1 -->
  <g transform="translate(40, 95)">
    <rect width="260" height="250" rx="10" fill="#11161A" stroke="#26333D" stroke-width="1.5"/>
    <rect width="260" height="32" rx="10" fill="#182026"/>
    <text x="16" y="21" fill="#38BDF8" font-family="monospace" font-size="11" font-weight="700">STAGE 01 · LEARN</text>
    <circle cx="236" cy="16" r="6" fill="#10B981"/>
    
    <text x="16" y="55" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="600">Baseline Acquisition</text>
    <text x="16" y="75" fill="#94A3B8" font-family="sans-serif" font-size="11">Motor runs in nominal healthy state for 15 minutes.</text>
    
    <rect x="16" y="95" width="228" height="65" rx="6" fill="#090B0D" stroke="#1E293B"/>
    <path d="M 26 128 C 45 110, 65 145, 85 128 C 105 110, 125 145, 145 128 C 165 110, 185 145, 205 128" stroke="#38BDF8" stroke-width="2" fill="none"/>
    <text x="26" y="150" fill="#64748B" font-family="monospace" font-size="8">Healthy RMS &amp; FFT Matrix Built</text>

    <text x="16" y="185" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Auto-clusters idle vs load cycles</text>
    <text x="16" y="202" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Computes Mahalanobis covariance</text>
    <text x="16" y="219" fill="#10B981" font-family="monospace" font-size="9">Baseline locked locally in SQLite</text>
  </g>

  <!-- STEP 2 -->
  <g transform="translate(325, 95)">
    <rect width="260" height="250" rx="10" fill="#11161A" stroke="#26333D" stroke-width="1.5"/>
    <rect width="260" height="32" rx="10" fill="#182026"/>
    <text x="16" y="21" fill="#F59E0B" font-family="monospace" font-size="11" font-weight="700">STAGE 02 · PERTURB</text>
    <circle cx="236" cy="16" r="6" fill="#F59E0B"/>
    
    <text x="16" y="55" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="600">Controlled Fault Replay</text>
    <text x="16" y="75" fill="#94A3B8" font-family="sans-serif" font-size="11">Controlled bearing looseness or benchmark dataset injection.</text>
    
    <rect x="16" y="95" width="228" height="65" rx="6" fill="#090B0D" stroke="#1E293B"/>
    <path d="M 26 128 L 45 112 L 60 142 L 75 95 L 90 150 L 115 128 L 135 110 L 155 145 L 180 90 L 205 130" stroke="#F59E0B" stroke-width="2" fill="none"/>
    <text x="26" y="150" fill="#F59E0B" font-family="monospace" font-size="8">High-frequency impacts injected</text>

    <text x="16" y="185" fill="#CBD5E1" font-family="sans-serif" font-size="10">• CWRU outer-race bearing fault</text>
    <text x="16" y="202" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Acoustic friction signature</text>
    <text x="16" y="219" fill="#F59E0B" font-family="monospace" font-size="9">Sensor streams live into ESP32</text>
  </g>

  <!-- STEP 3 -->
  <g transform="translate(610, 95)">
    <rect width="260" height="250" rx="10" fill="#11161A" stroke="#26333D" stroke-width="1.5"/>
    <rect width="260" height="32" rx="10" fill="#182026"/>
    <text x="16" y="21" fill="#EF4444" font-family="monospace" font-size="11" font-weight="700">STAGE 03 · DETECT</text>
    <circle cx="236" cy="16" r="6" fill="#EF4444"/>
    
    <text x="16" y="55" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="600">Statistical Anomaly Trigger</text>
    <text x="16" y="75" fill="#94A3B8" font-family="sans-serif" font-size="11">Isolation Forest flags deviation from baseline within seconds.</text>
    
    <rect x="16" y="95" width="228" height="65" rx="6" fill="#090B0D" stroke="#1E293B"/>
    <text x="24" y="118" fill="#EF4444" font-family="sans-serif" font-size="11" font-weight="700">Score: 0.81 (Abnormal)</text>
    <text x="24" y="134" fill="#94A3B8" font-family="monospace" font-size="9">Path length shortened in iForest</text>
    <text x="24" y="148" fill="#38BDF8" font-family="monospace" font-size="8">Latency to detection: 1.4 seconds</text>

    <text x="16" y="185" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Feature attribution pinpoints 1.2kHz</text>
    <text x="16" y="202" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Severity index scaled to 74%</text>
    <text x="16" y="219" fill="#EF4444" font-family="monospace" font-size="9">No cloud round-trip required</text>
  </g>

  <!-- STEP 4 -->
  <g transform="translate(895, 95)">
    <rect width="265" height="250" rx="10" fill="#11161A" stroke="#26333D" stroke-width="1.5"/>
    <rect width="265" height="32" rx="10" fill="#182026"/>
    <text x="16" y="21" fill="#10B981" font-family="monospace" font-size="11" font-weight="700">STAGE 04 · ACT</text>
    <circle cx="241" cy="16" r="6" fill="#10B981"/>
    
    <text x="16" y="55" fill="#FFFFFF" font-family="sans-serif" font-size="13" font-weight="600">Explainable Maintenance</text>
    <text x="16" y="75" fill="#94A3B8" font-family="sans-serif" font-size="11">PWA triggers audio and generates technician checklist.</text>
    
    <rect x="16" y="95" width="233" height="65" rx="6" fill="#090B0D" stroke="#1E293B"/>
    <text x="24" y="118" fill="#F59E0B" font-family="sans-serif" font-size="10" font-weight="700">🔊 Kannada/Hindi Voice Warning</text>
    <text x="24" y="134" fill="#94A3B8" font-family="sans-serif" font-size="9">"Inspect bearing within 48h"</text>
    <text x="24" y="148" fill="#10B981" font-family="monospace" font-size="8">Human approval button armed</text>

    <text x="16" y="185" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Spares needed: Bearing #6205</text>
    <text x="16" y="202" fill="#CBD5E1" font-family="sans-serif" font-size="10">• Estimated repair downtime: 45 min</text>
    <text x="16" y="219" fill="#10B981" font-family="monospace" font-size="9">Prevents unscheduled catastrophic halt</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "demo-walkthrough.svg"), "w", encoding="utf-8") as f:
    f.write(demo_svg)

print("Saved demo-walkthrough.svg")
