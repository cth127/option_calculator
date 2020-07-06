import random, math
from argparse import ArgumentParser as Argp


def cdf_Z(x) :
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def pdf_Z(x) :
    return 1 / math.sqrt(2 * math.pi) * math.exp(- math.pow(x, 2) / 2)

def random_Z() :
    return random.gauss(0, 1)

def discount(price, r, t) :
    return price * math.exp(-r * t)


# Monte Carlo Simulation
def MCS(n, o, s0, k, v, r, q, t) :
    # 365 days as day count convention
    day_count = 365
    days = int(day_count * t)
    dt = t / day_count
    payoff_list = list()

    for i in range(0, n) :
        path = [s0]
        for j in range(0, days) :
            stock_price = path[j] * math.exp(((r - q) - math.pow(v, 2) / 2) * dt + v * math.sqrt(dt) * random_Z())
            path.append(stock_price)
        if o == 'call' :
            payoff = max(0, path[-1] - k)
        elif o == 'put' :
            payoff = max(0, k - path[-1])
        payoff_list.append(payoff)
    option_price = discount(sum(payoff_list) / len(payoff_list), r, t)
    return option_price


# Clsoed Form with BSM Equation
def BSM(o, s0, k, v, r, q, t) :
    d1 = (math.log(s0 / k) + ((r - q) + math.pow(v, 2) / 2) * t) / (v * math.sqrt(t))
    d2 = d1 - (v * math.sqrt(t))
    if o == 'call' :
        option_price = s0 * cdf_Z(d1) * math.exp(-q * t) - k * math.exp(- r * t) * cdf_Z(d2)
    elif o == 'put' :
        option_price = k * math.exp(- r * t) * cdf_Z(-d2) - s0 * cdf_Z(-d1) * math.exp(-q * t)
    return option_price


# Binomial Tree Method
def TREE(n, o, s0, k, v, r, q, t) :
    dt = t / n
    mu = math.exp((r - q) * dt)
    up = math.exp(v * math.sqrt(dt))
    down = 1 / up
    prop = (mu - down) / (up - down)
    tree = [0] * (n + 1)
    tree[0] = [s0]

    for i in range(0, n) :
        layer = [0] * (i + 2)
        for j in range(0, i + 1) :
            if j == 0 :
                layer[j] = tree[i][j] * up
                layer[j+1] = tree[i][j] * down
            else :
                layer[j+1] = tree[i][j] * down
        tree[i + 1] = layer
        tree[i] = 0

    if o == 'call' :
        payoff = [max(0, i - k) for i in tree[-1]]
    elif o == 'put' :
        payoff = [max(0, k - i) for i in tree[-1]]
    option_tree = [0] * (n + 1)
    option_tree[0] = payoff
    del tree

    for i in range(0, n) :
        layer2 = [0] * (n - i)
        for j in range(0, n - i) :
            layer2[j] = discount(option_tree[i][j] * prop + option_tree[i][j + 1] * (1 - prop), r, dt)
        option_tree[i + 1] = layer2
        option_tree[i] = 0
    option_price = option_tree[-1][-1]
    return option_price


def main() :
    arg = Argp()
    arg.add_argument('-M', '--method', default = 'MCS', help = "Option Pricing Method (default : MC)  \"MCS\" : Monte Carlo Simulation / \"BSM\" : BSM Equation / \"TREE\" : Binomial Tree Method")
    arg.add_argument('-n', '--parameter', default = 100, help = "Parameter (default : 100) \"MCS\" : The Number of Path to Simulate / \"TREE\" : The Number of Time Step")
    arg.add_argument('-o', '--option', default = 'call', help = "Option Type (default : call) \"call\" : Call Option / \"put\" : Put Option (Only Support European Option Pricing Yet)")
    arg.add_argument('-s0', '--price', default= 100, help = "Current Underlying Asset Price (default : 100)")
    arg.add_argument('-k', '--strike', default = 120, help = "Strike Price (default : 120)")
    arg.add_argument('-v', '--volatility', default = 0.3, help = "Volatility of Underlying Asset (default = 0.3)")
    arg.add_argument('-r', '--rate', default = 0.05, help = "Risk Free Rate (default = 0.05)")
    arg.add_argument('-q', '--dividend', default = 0.02, help = "Dividend Rate (default = 0.02)")
    arg.add_argument('-t', '--maturity', default = 1, help = "Time to Maturity by Year (default = 1)")
    args = arg.parse_args()

    n = int(args.parameter)
    o = args.option
    s0 = float(args.price)
    k = float(args.strike)
    v = float(args.volatility)
    r = float(args.rate)
    q = float(args.dividend)
    t = float(args.maturity)

    if args.method == 'MCS' :
        option_price = MCS(n, o, s0, k, v, r, q, t)
        print("Option Price with Monte Carlo Simulation : ", option_price)
    elif args.method == 'BSM' :
        option_price = BSM(o, s0, k, v, r, q, t)
        print("Option Price with BSM Equation : ", option_price)
    elif args.method == 'TREE' :
        option_price = TREE(n, o, s0, k, v, r, q, t)
        print("Option Price with Binomial Tree Method : ", option_price)
    else :
        print("ERROR : {} is not supported method. \n Available : MCS, BSM, TREE".format(args.method))


if __name__ == '__main__' :
    main()