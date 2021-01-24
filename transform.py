import argparse
import csv
import datetime

class TradeHistory:
    def __init__(self, history):
        self.transaction_date = history[0]
        self.settlement_date = history[1]
        self.activity_description = history[2]
        self.description = history[3]
        self.symbol = history[4]
        self.quantity = history[5]
        self.price = history[6]
        self.currency = history[7]
        self.total_amount = history[8]

        self.transaction_date = datetime.datetime.strptime(
            self.transaction_date, 
            '%Y-%m-%d'
        ).strftime('%m/%d/%Y')
        self.settlement_date = datetime.datetime.strptime(
            self.settlement_date,
            '%Y-%m-%d'
        ).strftime('%m/%d/%Y')
    
    def __repr__(self) -> str:
        return f"[{self.symbol}] {self.activity_description} {self.quantity} shares at {self.currency}{self.price} on {self.settlement_date}"

def parse_bmo_trade_history(file):
    reader = csv.reader(file)
    next(reader); next(reader); next(reader)
    lines = [item for item in reader]
    trade_histories = [TradeHistory(line) for line in lines if line]
    return trade_histories

def main(input_file, output_file, commission=9.95):
    trade_histories = parse_bmo_trade_history(input_file)
    
    acb_output = [
        ["Date", "Security", "Transaction Type", "Amount", "Shares", "Commission", "Exchange Rate", "Total or Per Share", "Price in Foreign Currency?", "Commission in Foreign Currency?"]
    ]
    for history in trade_histories:
        acb_output.append([
            history.settlement_date,
            history.symbol,
            history.activity_description,
            history.price,
            history.quantity,
            commission,
            history.currency,
            "Per Share",
            "Yes",
            "Yes"
        ])
    
    writer = csv.writer(output_file)
    writer.writerows(acb_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transform trade history from IBM IL to ACB.ca format.')
    parser.add_argument('input_file', type=argparse.FileType('r'))
    parser.add_argument('output_file', type=argparse.FileType('w'))
    parser.add_argument('--commission', type=float, default=9.95)
    args = parser.parse_args()

    main(args.input_file, args.output_file, args.commission)
