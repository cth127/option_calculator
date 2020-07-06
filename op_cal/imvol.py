import math
from option_price import BSM
from greeks import Greeks
from argparse import ArgumentParser as Argp


def imvol(n, o, s0, k, v, r, q, t, m) :
    option_price = BSM(o, s0, k, v, r, q, t)
    # Use 1.1 times option price as market price
    if m == None :
        market_price = option_price * 1.1
    else :
        market_price = m
    while abs(market_price - option_price) > n :
        vega = Greeks('vega', o, s0, k, v, r, q, t)
        v -= (option_price - market_price) / vega
        option_price = BSM(o, s0, k, v, r, q, t)
    return v


def main() :
    arg = Argp()
    arg.add_argument('-n', '--parameter', default=0.001, help= "Tolerance Level of Newton Raphson Method (default : 0.001)")
    arg.add_argument('-o', '--option', default = 'call', help = "Option Type (default : call) \"call\" : Call Option / \"put\" : Put Option")
    arg.add_argument('-s0', '--price', default= 100, help = "Current Underlying Asset Price (default : 100)")
    arg.add_argument('-k', '--strike', default = 120, help = "Strike Price (default : 120)")
    arg.add_argument('-v', '--volatility', default = 0.3, help = "Volatility of Underlying Asset (default = 0.3)")
    arg.add_argument('-r', '--rate', default = 0.05, help = "Risk Free Rate (default = 0.05)")
    arg.add_argument('-q', '--dividend', default = 0.02, help = "Dividend Rate (default = 0.02)")
    arg.add_argument('-t', '--maturity', default = 1, help = "Time to Maturity by Year (default = 1)")
    arg.add_argument('-m', '--marketprice', default=None, help= "Market Price of option (default : 1.1 times BSM option price)")
    args = arg.parse_args()

    n = float(args.parameter)
    o = args.option
    s0 = float(args.price)
    k = float(args.strike)
    v = float(args.volatility)
    r = float(args.rate)
    q = float(args.dividend)
    t = float(args.maturity)
    if args.marketprice == None :
        m = None
    else :
        m = float(args.marketprice)
    print("Implied Volatility by Newton Raphson Method : ", imvol(n, o, s0, k, v, r, q, t, m))


if __name__ == '__main__' :
    main()