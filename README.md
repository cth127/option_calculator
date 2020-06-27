# option_calculator

BSM Equation, Monte Carlo Simulation, Binominall Tree, 세 가지 방법으로 유러피안 옵션을 프라이싱할 수 있는 계산기를 파이썬으로 구현하여 공유한다. 이와 함께 Newton Raphson법을 이용한 내재 변동성 계산기와 BSM Equation을 이용한 그릭(Greeks) 계산기 또한 공유한다.

(7월 초순 업로드 예정)

## 1. option_price.py : 옵션 계산기

사용법 : python3 option_price.py -M "모델명" -n "모수" -o "옵션종류" -s0 "현재가" -k "행사가" -v "변동성" -r "무위험 이자율" -q "연단위 배당율" -t "1년 단위 기간"

#### -M METHOD, --method METHOD

Option Pricing Method (default : MC) "MCS" : Monte Carlo Simulation / "BSM" : BSM Equation / "TREE" : Binomial Tree Method

#### -n PARAMETER, --parameter PARAMETER

Parameter (default : 100) "MCS" : The Number of Path to Simulate / "TREE" : The Number of Time Step

#### -o OPTION, --option OPTION

Option Type (default : call) "call" : Call Option / "put" : Put Option (Only Support European Option Pricing Yet)

#### -s0 PRICE, --price PRICE

Current Underlying Asset Price (default : 100)

#### -k STRIKE, --strike STRIKE

Strike Price (default : 120)

#### -v VOLATILITY, --volatility VOLATILITY

Volatility of Underlying Asset (default = 0.3)

#### -r RATE, --rate RATE  

Risk Free Rate (default = 0.05)

#### -q DIVIDEND, --dividend DIVIDEND

Dividend Rate (default = 0.02)

#### -t MATURITY, --maturity MATURITY

Time to Maturity by Year (default = 1)


## 2. imvol.py : 내재변동성 계산기 with 

사용법 : python3 imvol.py -n "모수" -o "옵션종류" -s0 "현재가" -k "행사가" -v "변동성" -r "무위험 이자율" -q "연단위 배당율" -t "1년 단위 기간" -m "옵션 시장가"

#### -n PARAMETER, --parameter PARAMETER

Tolerance Level of Newton Raphson Method (default : 0.001)

#### -o OPTION, --option OPTION

Option Type (default : call)

#### -s0 PRICE, --price PRICE

Current Underlying Asset Price (default : 100)

#### -k STRIKE, --strike STRIKE

Strike Price (default : 120)

#### -v VOLATILITY, --volatility VOLATILITY

Volatility of Underlying Asset (default = 0.3)

#### -r RATE, --rate RATE  

Risk Free Rate (default = 0.05)

#### -q DIVIDEND, --dividend DIVIDEND

Dividend Rate (default = 0.02)

#### -t MATURITY, --maturity MATURITY

Time to Maturity by Year (default = 1)

#### -m MARKETPRICE, --marketprice MARKETPRICE

"Market Price of option (default : 1.1 times BSM option price)



## 3. greeks.py : 그릭 계산기

사용법 : python3 greeks.py -G "그릭" -o "옵션종류" -s0 "현재가" -k "행사가" -v "변동성" -r "무위험 이자율" -q "연단위 배당율" -t "1년 단위 기간"

#### -G GREEKS, --Greeks GREEKS

Greeks to Calculate (default : delta)

#### -o OPTION, --option OPTION

Option Type (default : call)

#### -s0 PRICE, --price PRICE

Current Underlying Asset Price (default : 100)

#### -k STRIKE, --strike STRIKE

Strike Price (default : 120)

#### -v VOLATILITY, --volatility VOLATILITY

Volatility of Underlying Asset (default = 0.3)

#### -r RATE, --rate RATE  

Risk Free Rate (default = 0.05)

#### -q DIVIDEND, --dividend DIVIDEND

Dividend Rate (default = 0.02)

#### -t MATURITY, --maturity MATURITY

Time to Maturity by Year (default = 1)
