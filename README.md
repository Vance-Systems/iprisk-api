# IPRisk - Residential Proxy, VPN & Tor Exit Node Detection API

> Real-time fraud scoring for visitor IP addresses detecting datacenters, commercial VPNs, and Tor exit relays.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/status-active%20%2F%20operational-emerald.svg)](https://vance-systems.github.io)
[![Documentation](https://img.shields.io/badge/docs-vance--systems.github.io-indigo.svg)](https://vance-systems.github.io/iprisk-api-guide.html)

## Endpoints

- `GET /v1/ip/risk` - Analyze IP address for proxy, VPN, and fraud risk
- `POST /v1/ip/batch` - Batch assess fraud risk for multiple IP addresses

## Quick Start (Python)

```bash
python server.py
```

## Docker Deployment

```bash
docker build -t iprisk-api .
docker run -p 8080:8080 iprisk-api
```

## Production Developer Guide

For detailed interactive API documentation, interactive cURL testers, and client SDKs, visit:
**[https://vance-systems.github.io/iprisk-api-guide.html](https://vance-systems.github.io/iprisk-api-guide.html)**

---
Developed autonomously by **[Vance Systems](https://vance-systems.github.io)**.
