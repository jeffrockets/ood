import fileinput
from typing import List, Tuple

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
RAW_TRADE_HEADER = ["trade_id", "trade_date", "time_of_trade", "portfolio", "exchange", "product", "product_type", "expiry_dt", "qty", "strike_price", "side"]
"""

from datetime import datetime, timedelta


RAW_TRADE_HEADER = ["trade_id", "trade_date", "time_of_trade", "portfolio",
                    "exchange", "product", "product_type", "expiry_dt",
                    "qty", "strike_price", "side"]


class Trade:
    def __init__(self, data):
        self.data = {att: None for att in RAW_TRADE_HEADER}
        self.data["date_time"] = None

        # TODO: store data in the table, i.e., self.data["product"] = "FB"
        # TODO: it's helpful to check if the input is a string, because input may be invalid

        # TODO: combine date and time
        # TODO: check if the input has the valid form (if you didn't pass some tests)
        # self.data["date_time"] = datetime.strptime(self.data["trade_date"] + self.data["time_of_trade"],
        #                                            "%Y-%m-%d%H:%M:%S")

        # TODO: change the form of CBOE, so every data has the same form, making the comparison easier
        # you can assume data["qty"] is int
        # if qty > 0, data["side"] = "BUY"
        # else, data["side"] = "SELL", data["qty"] = -qty

    def get(self, name):
        return self.data[name]


def is_runner(broker, electronic):
    """Return True if it's a pair of runner, else return False."""
    # TODO: check "portfolio"
    # TODO: check "product"
    # TODO: check "product_type"
    # TODO: check "side"
    # TODO: check "expiry_dt"
    # TODO: check "strike_price"

    # TODO: check "date_time", if one of them is None, return False
    # if electronic_time <= broker_time and broker_time <= electronic_time + timedelta(seconds=60):
    #     return True


class Solution:
    def __init__(self):
        # create a list to store brokers
        # create a list to store electronics
        self.broker_trade_list = []
        self.electronic_trade_list = []

    def process_raw_trade(self, raw_trade: List):
        # create one instance for one row input
        trade = Trade(raw_trade)
        if trade.get("portfolio") == "Broker":
            self.broker_trade_list.append(trade)
        else:
            self.electronic_trade_list.append(trade)

    def run(self) -> List[Tuple[str, str]]:
        broker_electronic_time_list = []
        for broker in self.broker_trade_list:
            for electronic in self.electronic_trade_list:
                if is_runner(broker, electronic):
                    # TODO: save (broker_id, electronic_id, electronic_trade_date_time) to the list
                    pass
        # TODO: sort the list according to the trade_date_time
        # hint: use sorted(..., key=lambda x: x[2])
        return # your result


if __name__ == '__main__':
    solution = Solution()
    for row in fileinput.input():
        raw_trade = list(row.strip().replace(" ", "").split(","))
        solution.process_raw_trade(raw_trade)

    print(solution.run())
