import requests

def getStrategiesForTokenHash(tokenHash):
    url = "https://api.kamino.finance/strategies/" + tokenHash + "/metrics?env=mainnet-beta"

    print("list strategies")
    print(requests.get(url).text)

def main():

    # get shareholder rewards
    #GET https://api.kamino.finance/strategies/shareholders/:shareholder_pubkey/rewards/history?env={cluster}
    url = "https://api.kamino.finance/strategies/shareholders/3xFbeRW7s44e6oknvkCAgHJhNt8XcwigeEYZBVTcJAnh/rewards/history?env=mainnet-beta"

    yieldsUrl = "https://api.kamino.finance/v2/staking-yields"

    # needs auth
    strategiesUrl =  "https://api.kamino.finance/strategies/3xFbeRW7s44e6oknvkCAgHJhNt8XcwigeEYZBVTcJAnh/rewards/eligible-shareholders?env=mainnet-beta&start=2025-01-01&end=2025-01-07"

    strategiesListUrl = "https://api.kamino.finance/strategies/enabled?env=mainnet-beta"

    # Token strategies
    cbBtc = "7u3HeHxYDLhnCoErrtycNokbQYbWGzLs6JSDqGAv5PfF/37Jk2zkz23vkAYBT66HM2gaqJuNg2nYLsCreQAVt5MWK"

    getStrategiesForTokenHash(cbBtc)

    publicStrategiesUrl = "https://api.kamino.finance/strategies/Cfuy5T6osdazUeLego5LFycBQebm9PP3H7VNdCndXXEN/shareholders/HZYHFagpyCqXuQjrSCN2jWrMHTVHPf9VWP79UGyvo95L/fees-and-rewards?env=mainnet-beta"

    #response = requests.get(strategiesUrl)
    #print(response.text)

if __name__ == "__main__":
    main()
