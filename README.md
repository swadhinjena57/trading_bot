# Binance Futures Testnet Trading Bot

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY / SELL
- CLI interface
- Logging
- Exception handling
- Input validation

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
BINANCE_API_KEY=YOUR_BINANCE_API_KEY
BINANCE_API_SECRET=YOUR_BINANCE_API_SECRET
```

Run MARKET

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Run LIMIT

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Assumptions

- Binance Futures Testnet account is active.
- Valid API credentials are configured.
- LIMIT orders require a price.