from bot import BasicBot
from cli import get_user_input

def main():
    print("\n🚀 Welcome to the Mock Binance Trading Bot\n")

    symbol, side, order_type, quantity, price, stop_price = get_user_input()

    bot = BasicBot()
    bot.place_order(symbol, side, order_type, quantity, price, stop_price)

if __name__ == "__main__":
    main()
