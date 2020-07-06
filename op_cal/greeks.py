import math
from option_price import pdf_Z, cdf_Z
from argparse import ArgumentParser as Argp


def Greeks(G, o, s0, k, v, r, q, t) :
    d1 = (math.log(s0 / k) + ((r - q) + math.pow(v, 2) / 2) * t) / (v * math.sqrt(t))
    d2 = d1 - (v * math.sqrt(t))
    if o == 'call' :
        if G == 'delta' :
            greek = cdf_Z(d1) * math.exp(-q * t)
        elif G == 'gamma' :
            greek = (pdf_Z(d1) * math.exp(-q * t)) / (s0 * v * math.sqrt(t))
        elif G == 'vega' :
            greek = s0 * math.sqrt(t) * pdf_Z(d1) * math.exp(-q * t)
        elif G == 'theta' :
            greek = - (s0 * pdf_Z(d1) * v * math.exp(-q * t)) / (2 * math.sqrt(t)) + q * s0 * cdf_Z(d1) * math.exp(-q * t) - r * k * math.exp(-r * t) * cdf_Z(d2)
        elif G == 'rho' :
            greek = k * t * math.exp(-r * t) * cdf_Z(d2)
    if o == 'put' :
        if G == 'delta' :
            greek = (cdf_Z(d1) - 1) * math.exp(-q * t)
        elif G == 'gamma' :
            greek = (pdf_Z(d1) * math.exp(-q * t)) / (s0 * v * math.sqrt(t))
        elif G == 'vega' :
            greek = s0 * math.sqrt(t) * pdf_Z(d1) * math.exp(-q * t)
        elif G == 'theta' :
            greek = - (s0 * pdf_Z(d1) * v * math.exp(-q * t)) / (2 * math.sqrt(t)) - q * s0 * cdf_Z(-d1) * math.exp(-q * t) + r * k * math.exp(-r * t) * cdf_Z(-d2)
        elif G == 'rho' :
            greek = - k * t * math.exp(-r * t) * cdf_Z(-d2)
    return greek


def main() :
    arg = Argp()
    arg.add_argument('-G', '--Greeks', default="delta", help="Greeks to Calculate (default : delta)")
    arg.add_argument('-o', '--option', default = 'call', help = "Option Type (default : call) \"call\" : Call Option / \"put\" : Put Option")
    arg.add_argument('-s0', '--price', default= 100, help = "Current Underlying Asset Price (default : 100)")
    arg.add_argument('-k', '--strike', default = 120, help = "Strike Price (default : 120)")
    arg.add_argument('-v', '--volatility', default = 0.3, help = "Volatility of Underlying Asset (default = 0.3)")
    arg.add_argument('-r', '--rate', default = 0.05, help = "Risk Free Rate (default = 0.05)")
    arg.add_argument('-q', '--dividend', default = 0.02, help = "Dividend Rate (default = 0.02)")
    arg.add_argument('-t', '--maturity', default = 1, help = "Time to Maturity by Year (default = 1)")
    args = arg.parse_args()

    G = args.Greeks
    o = args.option
    s0 = float(args.price)
    k = float(args.strike)
    v = float(args.volatility)
    r = float(args.rate)
    q = float(args.dividend)
    t = float(args.maturity)
    print("Calculated {0} by BSM Equation : {1}".format(G, Greeks(G, o, s0, k, v, r, q, t)))


if __name__ == '__main__' :
    main()