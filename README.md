# Binance Futures Trading Bot (Testnet)

## 📌 Overview

This project is a CLI-based trading bot that interacts with Binance Futures Testnet.
It allows users to place MARKET and LIMIT orders with proper validation, logging, and structured code design.

---

## ⚙️ Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input
* Input validation
* Logging of API requests and responses
* Error handling

---

## 🛠️ Setup Instructions

### 1. Clone repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `config.py` file:

```
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
```

---

## ▶️ How to Run

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 50000
```

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── config.py
├── trading.log
├── README.md
```

---

## 🧪 Logs

All API requests and responses are logged in:

```
trading.log
```

---

## ⚠️ Assumptions

* Using Binance Futures Testnet
* Orders may not execute instantly on testnet
* API keys must have Futures permissions enabled

---

## ✅ Status

✔ Fully functional
✔ Meets assignment requirements
