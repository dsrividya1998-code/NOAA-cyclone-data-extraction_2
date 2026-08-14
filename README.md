# NOAA Tropical cyclone dataset extraction and Quality Check for anomalies

## Overview
This repository contains a Python script designed to programmatically retrieve inspect tropical cyclone trajectory data from the National Oceanic and Atmospheric Administration (NOAA) OneStop data catalogue. Specifically, it targets the data stream for Storm WP012026 (Western North Pacific Basin, Storm 01, 2026).

## Features
* **Automated data retrieval:** Fetches the raw, machine-readable JSON data directly from NOAA THREDDS data server
* **Data Parsing:** Iterates through the hierarchical JSON structure to isolate key variables including timestamps, granule IDs, storm coordinates and development stages
* **Automated Quality Check (QC):** Implements an automatic logic loop to detect data anomalies, specially flagging the missing Sea Surface Temperature values natively recorded as `-999.0`

## Dataset Technical Details
* **Source:** TC-PRIMED (Tropical Cyclone PRecipitation, Infrared, Microwave, and Environmental Dataset).
* **Platform/Sensor:** GCOM-W1 satellite using the AMSR2 (Advanced Microwave Scanning Radiometer 2) instrument.
* **Target Variable:** Sea Surface Temperature (SST) measured in Celsius.

## Requirements
To run this script locally or in an environment like Google Colab, you need Python installed along with the `requests` library.

```bash
pip install requests
