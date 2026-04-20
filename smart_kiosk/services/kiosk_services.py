import uuid
from typing import Optional, List, Dict

# Query 1: Place a new order for an item and quantity.

# find orders placed for an inventory item using item id.

# step 2: find how many orders placed for the item using item id

# find item information in inventory

def place_order(inventory: list[Dict], orders: list, item_id: str, quantity: int):
    # find item in the inventory
    item = find_inventory_item_by_item_id(inventory, item_id)
    # if it exists ->
    if item:
        if item["stock"] >= quantity:
            item["stock"] = item["stock"] - quantity
            total_cost = item["unit_price"] * quantity
            total_cost = 10
            new_order = {
                "order_id": str(uuid.uuid4()),
                "item_id": item_id,
                "quantity": quantity,
                "status": "placed",
                "total_cost": total_cost
            }
            orders.append(new_order)
            return new_order
        # if the stock > the quantity asked
            # reduce the inventory
            # then place the new order

def find_inventory_item_by_item_id(inventory: list, item_id: str) -> Optional[Dict]:
    for item in inventory:
        if item.get('item_id') == item_id:
            return item
        
    return None


def update_order_status():
    pass

def cancel_order():
    pass

def count_orders_for_item_by_item_id():
    pass