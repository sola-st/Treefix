# Extracted from https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
    from marshmallow_dataclass import dataclass
    user = User("Danilo","50","RedBull",15,OrderStatus.CREATED)
    user_json = User.Schema().dumps(user)
    user_json_str = user_json.data

    json_str = '{"name":"Danilo", "orderId":"50", "productName":"RedBull", "quantity":15, "status":"Created"}'
    user, err = User.Schema().loads(json_str)
    print(user,flush=True)

class OrderStatus(Enum):
    CREATED = 'Created'
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    FAILED = 'Failed'

@dataclass
class User:
    def __init__(self, name, orderId, productName, quantity, status):
        self.name = name
        self.orderId = orderId
        self.productName = productName
        self.quantity = quantity
        self.status = status

    name: str
    orderId: str
    productName: str
    quantity: int
    status: OrderStatus

