def get_user_input():
    symbol = input("📈 Enter trading pair (e.g., BTCUSDT): ").upper()
    
    side = input("🟢 Order side (BUY/SELL): ").upper()
    while side not in ["BUY", "SELL"]:
        print("❌ Invalid side. Please enter 'BUY' or 'SELL'.")
        side = input("🟢 Order side (BUY/SELL): ").upper()

    order_type = input("📋 Order type (MARKET/LIMIT/STOP_LIMIT): ").upper()
    while order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        print("❌ Invalid type. Please enter 'MARKET', 'LIMIT', or 'STOP_LIMIT'.")
        order_type = input("📋 Order type (MARKET/LIMIT/STOP_LIMIT): ").upper()

    quantity = input("🔢 Quantity to trade: ")
    while not quantity.replace('.', '', 1).isdigit():
        print("❌ Invalid number.")
        quantity = input("🔢 Quantity to trade: ")
    quantity = float(quantity)

    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = input("💰 Limit price: ")
        while not price.replace('.', '', 1).isdigit():
            print("❌ Invalid price.")
            price = input("💰 Limit price: ")
        price = float(price)

    elif order_type == "STOP_LIMIT":
        stop_price = input("🛑 Stop price: ")
        while not stop_price.replace('.', '', 1).isdigit():
            print("❌ Invalid stop price.")
            stop_price = input("🛑 Stop price: ")
        stop_price = float(stop_price)

        price = input("💰 Limit price (after stop is triggered): ")
        while not price.replace('.', '', 1).isdigit():
            print("❌ Invalid limit price.")
            price = input("💰 Limit price (after stop is triggered): ")
        price = float(price)

    return symbol, side, order_type, quantity, price, stop_price
