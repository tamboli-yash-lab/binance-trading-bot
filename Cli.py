import argparse
from bot.orders import OrderService
from bot.validators import validate_symbol, validate_quantity, validate_price


def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # ✅ Validation goes HERE
    try:
        validate_symbol(args.symbol)
        validate_quantity(args.qty)
        validate_price(args.price)
    except ValueError as e:
        print(f"❌ Validation Error: {e}")
        return

    order_service = OrderService()

    if args.type == "MARKET":
        response = order_service.place_market_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.qty
        )

    elif args.type == "LIMIT":
        if not args.price:
            print("❌ Price required for LIMIT order")
            return

        response = order_service.place_limit_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.qty,
            price=args.price
        )

    print("\n=== ORDER SUMMARY ===")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.qty}")

    print("\n=== RESPONSE ===")
    print(f"Order ID: {response['orderId']}")
    print(f"Status: {response['status']}")
    print(f"Executed Qty: {response['executedQty']}")

    print("\n✅ Order executed successfully")

if __name__ == "__main__":
    main()
