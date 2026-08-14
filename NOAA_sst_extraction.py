{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWmiS0zP3VScmIIYWOGg8w",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dsrividya1998-code/NASA-power-API-data-extraction/blob/main/NOAA_data_extraction_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VLbmFa0qrk5G",
        "outputId": "a10f2902-b62b-4592-c505-be7a5ba8bfb8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Tropical Cyclone WP012026: Live Sea Surface Temperature (SST) Quality Control\n",
            "\n",
            "Time: 2026-01-13T16:24:52 | Granule ID: 072654 | Location: [132.88, 7.39] | Development stage: DB | SST: 29.07 °C\n",
            "Time: 2026-01-14T04:51:07 | Granule ID: 072662 | Location: [131.22, 8.61] | Development stage: DB | SST: 29.19 °C\n",
            "Time: 2026-01-14T17:07:40 | Granule ID: 072669 | Location: [130.07, 9.18] | Development stage: TD | SST: 29.06 °C\n",
            "Time: 2026-01-16T04:39:40 | Granule ID: 072691 | Location: [128.1, 11.72] | Development stage: TS | SST: 28.32 °C\n",
            "Time: 2026-01-16T16:54:21 | Location [12.64, 125.8] | STATUS: Missing Data Flag (-999.0) Detected\n",
            "Time: 2026-01-17T05:23:33 | Granule ID: 072706 | Location: [124.92, 13.88] | Development stage: TS | SST: 28.30 °C\n",
            "Time: 2026-01-17T17:37:16 | Granule ID: 072713 | Location: [125.18, 14.19] | Development stage: TS | SST: 28.15 °C\n",
            "Time: 2026-01-19T05:12:00 | Granule ID: 072735 | Location: [127, 16.65] | Development stage: TS | SST: 27.46 °C\n",
            "Time: 2026-01-19T17:24:10 | Granule ID: 072742 | Location: [128.04, 17.02] | Development stage: TS | SST: 27.46 °C\n",
            "Time: 2026-01-20T04:16:45 | Granule ID: 072749 | Location: [129.87, 17.75] | Development stage: TS | SST: 27.22 °C\n",
            "Time: 2026-01-20T16:28:30 | Granule ID: 072756 | Location: [132.8, 17.25] | Development stage: TD | SST: 27.64 °C\n",
            "Time: 2026-01-21T04:59:03 | Granule ID: 072764 | Location: [133.86, 15.98] | Development stage: TD | SST: 27.99 °C\n",
            "Time: 2026-01-21T17:12:46 | Granule ID: 072771 | Location: [134.56, 13.72] | Development stage: TD | SST: 29.14 °C\n"
          ]
        }
      ],
      "source": [
        "# Import the requests library\n",
        "import requests\n",
        "\n",
        "# Raw data URL from the NOAA THREDDS server\n",
        "noaa_url = \"https://www.ncei.noaa.gov/data/tropical-cyclone-precipitation-infrared-microwave-environmental-dataset/access/2026/WP/01/TCPRIMED_v01r01-preliminary_WP012026_AMSR2_GCOMW1_s20260113162452_e20260121171246_c20260130.json\"\n",
        "\n",
        "# 1. Send the request to NOAA THREDDS server FIRST\n",
        "response = requests.get(noaa_url)\n",
        "\n",
        "# 2. Convert the JSON response into a Python dictionary\n",
        "noaa_data = response.json()\n",
        "\n",
        "# Print Sea Surface temperature values along with missing values\n",
        "print(\"Tropical Cyclone WP012026: Live Sea Surface Temperature (SST) Quality Control\\n\")\n",
        "\n",
        "# 3. NOW iterate through the downloaded JSON dictionary\n",
        "for filename, attributes in noaa_data.items():\n",
        "    timestamp = attributes[\"date_time_group\"]\n",
        "    granule_number = attributes[\"granule_number\"]\n",
        "    development_level = attributes[\"development_level\"]\n",
        "    sst = attributes[\"sst\"]                               # Sea Surface Temperature\n",
        "    storm_longitude = attributes[\"storm_longitude\"]\n",
        "    storm_latitude = attributes[\"storm_latitude\"]\n",
        "\n",
        "    # 4. Keep the check INDENTED inside the loop to check every single row (Automated Quality Control Check for the -999.0 anomaly)\n",
        "    if sst == -999.0:\n",
        "        print(f\"Time: {timestamp} | Location [{storm_latitude}, {storm_longitude}] | STATUS: Missing Data Flag (-999.0) Detected\")\n",
        "    else:\n",
        "        print(f\"Time: {timestamp} | Granule ID: {granule_number} | Location: [{storm_longitude}, {storm_latitude}] | Development stage: {development_level} | SST: {sst:.2f} °C\")"
      ]
    }
  ]
}
