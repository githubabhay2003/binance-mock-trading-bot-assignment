from mock_binance import MockBinanceClient
from utils import log_order, log_error, init_logs

class BasicBot:
    def __init__(self):
        init_logs()
        self.client = MockBinanceClient()

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):

        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )

            print("\n✅ Order placed successfully!")
            print("🔍 Order Details:")
            for key, value in order.items():
                print(f"  {key}: {value}")
            log_order(order)
        except Exception as e:
            print("\n❌ Error placing order:", str(e))
            log_error(str(e))
