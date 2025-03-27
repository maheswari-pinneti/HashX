# ⚡ HashX – High-Performance 256-bit Hashing Algorithm  
<h2 align="center"> The simplest & fastest open-source hashing library!</h2>

---

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue.svg" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/github/stars/ProgrammerKR/HashX.svg?style=flat" />
  <img src="https://img.shields.io/github/forks/ProgrammerKR/HashX.svg?style=flat" />
  <img src="https://img.shields.io/github/downloads/ProgrammerKR/HashX/total" />
  <img src="https://img.shields.io/github/repo-size/ProgrammerKR/HashX" />
  <img src="https://img.shields.io/github/issues/ProgrammerKR/HashX" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" />
  <img src="https://img.shields.io/github/last-commit/ProgrammerKR/HashX" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20MacOS-lightgrey.svg" />
</p>

---

#### HashX is an ultra-fast, efficient, and **secure 256-bit hashing algorithm** designed for **data integrity verification, indexing, checksums, and non-cryptographic applications**.  

#### Built with **multi-threading, optimized bitwise operations, and an advanced mixing function**, HashX delivers exceptional **speed, collision resistance, and scalability**.  

## 🚀 Features & Enhancements  

✅ **High-Speed Processing** – Optimized bitwise operations and low-level transformations.  
✅ **Multi-Threaded Execution** – Parallel chunk processing for increased speed.  
✅ **256-bit Strong Hash Output** – Reduces collisions while maintaining efficiency.  
✅ **Advanced Mixing Function** – Inspired by MurmurHash3 for better diffusion.  
✅ **Bitwise Rotation Optimization** – Faster and more secure state transformations.  
✅ **Lightweight & Scalable** – Low memory usage, works on large data sets.  
✅ **Strong Avalanche Effect** – Small input changes drastically modify the hash.  
✅ **Cross-Platform & Extensible** – Works seamlessly in Python, with future support planned for C/Rust.  

----

## 📥 Installation  

Clone the repository:  
```bash
git clone https://github.com/ProgrammerKR/HashX.git
```
Navigate to the directory:  
```bash
cd HashX
```

## 🛠️ Usage  

### **Python Example**  
```python
from hashx import HashX

hasher = HashX()
print(hasher.hash("Hello, World!"))  # Example usage
```

### **Output**
```
3F2A9D7B89C4E6A5D12F1E4B67A3C9D5E8F7B2A6C3D1E0F4B6A2D9C7E3F5A8B1
```

## ⚙️ How It Works  

1. **Initialization** – Hash state consists of **4 unique parts**, seeded for strong uniqueness.  
2. **Chunk Processing** – Data is split into **64-bit blocks**, processed in **parallel threads**.  
3. **Bitwise Mixing & Rotation** – Advanced scrambling ensures strong randomness.  
4. **Finalization Rounds** – Enhanced diffusion eliminates weak patterns.  
5. **Output Generation** – 256-bit hexadecimal hash is returned.  

## 🔬 Benchmarking (Coming Soon)  

# 📊 HashX Benchmarking Report  

This document compares **HashX** with other popular hashing algorithms: **SHA-256, BLAKE3, and MurmurHash3**.  
The benchmark measures **speed (MB/s)**, **collision resistance**, and **avalanche effect**.  

## 🔬 Benchmarking Script (Python)  

Run the following script to test HashX performance:  

```python
import time
import hashlib
import blake3
import mmh3
from hashx import HashX

# Test Data (10MB)
data = b"A" * (10 * 1024 * 1024)

def benchmark_hashing(algorithm, func):
    start = time.time()
    func(data)
    end = time.time()
    speed = (len(data) / (end - start)) / (1024 * 1024)  # MB/s
    return speed

# Hashing functions
hashx = HashX()
tests = {
    "HashX": lambda d: hashx.hash(d),
    "SHA-256": lambda d: hashlib.sha256(d).hexdigest(),
    "BLAKE3": lambda d: blake3.blake3(d).hexdigest(),
    "MurmurHash3": lambda d: mmh3.hash_bytes(d)
}

# Run Benchmark
results = {name: benchmark_hashing(name, func) for name, func in tests.items()}

# Print Results
print("\n📊 Benchmark Results:")
for name, speed in results.items():
    print(f"{name}: {speed:.2f} MB/s")
```

## 🛠️ Future Plans  

- **C and Rust Implementation** for ultra-fast performance.  
- **GPU Acceleration** using CUDA/OpenCL.  
- **Cryptographic Security Mode** for password hashing.

📢 **Have questions or feedback?**  
- 💬 Join discussions [here](https://github.com/ProgrammerKR/HashX/discussions)  
- 🐛 Found a bug? Report [here](https://github.com/ProgrammerKR/HashX/issues)

## 🤝 Contributing  

Contributions are welcome! Feel free to fork the repo, submit issues, or create pull requests.  

## 📜 License  

This project is open-source and available under the **MIT License**.  

