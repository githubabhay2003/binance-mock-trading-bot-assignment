import random
import time

class MockBinanceClient:
    def create_order(self, symbol, side, type, quantity, price=None, stopPrice=None):

        order_id = random.randint(1000000, 9999999)
        print(f"\n📡 [MOCK] Sending {side} {type} order for {quantity} {symbol}")
        time.sleep(1)  # Simulate network delay

        return {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "status": "FILLED",
            "type": type.upper(),
            "side": side.upper(),
            "price": price or "market",
            "stopPrice": stopPrice,
            "executedQty": quantity,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

