import os, requests, datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("FINNHUB_TOKEN")
STOCK = "AAPL"

def main():

    q = requests.get(
        "https://finnhub.io/api/v1/quote",
        params={"symbol":STOCK,"token":TOKEN}
    ).json()
    print("AAPL snapshot:", q)  # keys: c= current, h/l/o/p, t=unix
    ts = q["t"]
    print("As datetime (UTC):", dt.datetime.utcfromtimestamp(ts))


if __name__=="__main__":
    main()
