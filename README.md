# 🧠 Binance Mock Trading Bot (Assignment)

A Python-based CLI trading bot that simulates Binance USDT-M Futures orders using mock responses. Designed to demonstrate knowledge of Binance API interactions, order handling, and robust input validation—all without real money or credentials.

---

## 🚀 Features

- 🔄 Simulates placing **Market**, **Limit**, and **Stop-Limit** orders
- 🔧 Supports both **BUY** and **SELL** sides
- 🖥 Command-line interface (CLI) for interactive user input
- ✅ Input validation and clean user prompts
- 📋 Mock responses for order placement with fake `orderId` and timestamps
- 🧪 Safe for testing (does **not** require Binance Testnet access)
- 📦 Clean, reusable Python modules with separation of concerns

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Interface:** CLI
- **Logging:** Console
- **Libraries:** Only standard Python libraries used (mocked Binance behavior)

---

## 📂 Project Structure

```bash
binance-mock-bot/
├── cli.py             # CLI prompts and user input validation
├── bot.py             # Core bot logic and order handling
├── mock_binance.py    # Mocks the Binance client behavior
├── main.py            # Entry point for the bot
├── .gitignore         # Ignores unnecessary files
└── README.md          # Project overview and instructions
```
## ⚙️ How to Run

**Clone the repository:**
- git clone https://github.com/githubabhay2003/binance-mock-trading-bot-assignment.git
- cd binance-mock-trading-bot-assignment

## Run the bot:
- python main.py
- Follow the prompts:
```text
📈 Enter trading pair (e.g., BTCUSDT): btcusdt
🟢 Order side (BUY/SELL): buy
📋 Order type (MARKET/LIMIT/STOP_LIMIT): stop_limit
🔢 Quantity to trade: 0.05
🛑 Stop price: 64000
💰 Limit price (after stop is triggered): 63500
🧪 Supported Order Types
```
## Type	Description
- **MARKET**	Immediate execution at market price
- **LIMIT**	Execution only at target price
- **STOP_LIMIT**	Triggered limit order (conditional)

## 📌 Notes
- This bot is mock-only — it does not interact with real or testnet Binance APIs.
- No API keys or authentication needed.
- Designed for assignment/testing/demo purposes.

## 📄 License
- This project is open-source under the MIT License.
- You may use, modify, and distribute it freely.

## ✍️ Author
👤 Abhay Kumar Saini
🔗 githubabhay2003
