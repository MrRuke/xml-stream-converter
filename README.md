# 🚀 High-Performance XML to CSV Converter

High-performance streaming converter designed for processing massive XML datasets (10GB+) with minimal memory footprint (O(1) RAM usage).

## ⚡ Key Features

* **Memory Efficient:** Uses `iterparse` (streaming) approach. Consumes <50MB RAM even when processing 50GB+ files.
* **Fast:** Optimized primarily for I/O bound operations.
* **User Friendly:** Includes GUI (Graphic User Interface) modes.
* **Progress Tracking:** Real-time progress bar with throughput speed (records/sec).

## 🛠 Tech Stack

* **Python 3.x**
* **xml.etree.ElementTree** (Standard Library) - for C-optimized XML parsing.
* **Tkinter** - for native OS file dialogs.
* **tqdm** - for CLI progress visualization.

## ✅ Testing
Unit tests are implemented using **pytest**.

[![Python Tests](https://github.com/MrRuke/xml-stream-converter/actions/workflows/python-tests.yml/badge.svg)](https://github.com/MrRuke/xml-stream-converter/actions/workflows/python-tests.yml)
