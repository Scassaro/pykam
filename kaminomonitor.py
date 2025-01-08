import requests

def getStrategiesForTokenHash(tokenHash):
    url = "https://api.kamino.finance/strategies/" + tokenHash + "/metrics?env=mainnet-beta"

    print("list strategies")
    print(requests.get(url).text)

def collectStrategies():
    url = "https://api.kamino.finance/strategies/enabled?env=mainnet"
    print("list strategies")
    print(requests.get(url).text)

def getYields():

    url = "https://api.kamino.finance/v2/staking-yields/median"
    print("list yields")
    print(requests.get(url).text)

def main():

    solscanApiKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE3MzYzMTczNzMyMDcsImVtYWlsIjoic3JjYXNzYXJvQGdtYWlsLmNvbSIsImFjdGlvbiI6InRva2VuLWFwaSIsImFwaVZlcnNpb24iOiJ2MiIsImlhdCI6MTczNjMxNzM3M30.tUqB72JHW34L2BvTiERUGiLk7mcjl-jFUe89Be6ytjA"

    # get shareholder rewards
    #GET https://api.kamino.finance/strategies/shareholders/:shareholder_pubkey/rewards/history?env={cluster}
    url = "https://api.kamino.finance/strategies/shareholders/3xFbeRW7s44e6oknvkCAgHJhNt8XcwigeEYZBVTcJAnh/rewards/history?env=mainnet-beta"

    yieldsUrl = "https://api.kamino.finance/v2/staking-yields"

    # needs auth
    strategiesUrl =  "https://api.kamino.finance/strategies/3xFbeRW7s44e6oknvkCAgHJhNt8XcwigeEYZBVTcJAnh/rewards/eligible-shareholders?env=mainnet-beta&start=2025-01-01&end=2025-01-07"

    strategiesListUrl = "https://api.kamino.finance/strategies/enabled?env=mainnet-beta"

    # Token strategies
    cbBtc = "7u3HeHxYDLhnCoErrtycNokbQYbWGzLs6JSDqGAv5PfF/37Jk2zkz23vkAYBT66HM2gaqJuNg2nYLsCreQAVt5MWK"

    getYields()

    publicStrategiesUrl = "https://api.kamino.finance/strategies/Cfuy5T6osdazUeLego5LFycBQebm9PP3H7VNdCndXXEN/shareholders/HZYHFagpyCqXuQjrSCN2jWrMHTVHPf9VWP79UGyvo95L/fees-and-rewards?env=mainnet-beta"

    #response = requests.get(strategiesUrl)
    #print(response.text)

if __name__ == "__main__":
    main()
