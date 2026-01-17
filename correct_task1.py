def calculate_average_order_value(orders):
    total = 0.0
    count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            try:
                total += float(order["amount"])
                count += 1
            except (ValueError, TypeError, KeyError):
                continue
    if count == 0:
        return 0.0
    
    return total / count