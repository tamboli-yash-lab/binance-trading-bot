def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")


def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price):
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")