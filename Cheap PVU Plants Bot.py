from web3 import Web3
import requests
import json
import time

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
url_eth = "https://api.bscscan.com/api"

print(web3.isConnected())
print("Block Number: ", web3.eth.blockNumber)

contract_address = '0x5Ab19e7091dD208F352F8E727B6DCC6F8aBB6275'
API_ENDPOINT = url_eth+'?module=account&action=txlist&address='+contract_address+'&page=1&offset=10&sort=desc&apikey='

getAbi = 'https://api.bscscan.com/api?module=contract&action=getabi&address=0x5Ab19e7091dD208F352F8E727B6DCC6F8aBB6275&apikey='
abi = requests.get(url = getAbi)
abi = abi.json()

getBidAbi = 'https://api.bscscan.com/api?module=contract&action=getabi&address=0x926eae99527a9503eaDb4c9e927f21f84f20C977&apikey='
bidAbi = requests.get(url = getBidAbi)
bidAbi = bidAbi.json()

# Initialise marketplace bid contract
bidContract = web3.eth.contract(address='0x926eae99527a9503eaDb4c9e927f21f84f20C977', abi=bidAbi['result'])

def getNewTransactions():
    response = []
    try:
        web3_filter= web3.eth.filter('pending')
        transaction_hashes = web3.eth.getFilterChanges(web3_filter.filter_id)
        for tx in transaction_hashes:
            try:
                txData = web3.eth.getTransaction(tx)
                if(txData['to'] == '0x5Ab19e7091dD208F352F8E727B6DCC6F8aBB6275'):
                    response.append(txData)
            except:
                pass
    except:
        getNewTransactions()
    getPlantPriceInPVU(response)     

def sendDiscord(tokenId, price):
    print("Sending Discord...")
    link = 'https://marketplace.plantvsundead.com/#/plant/' + str(plantID)
    motherTreeLink = 'https://marketplace.plantvsundead.com/#/mother-tree/' + str(plantID)

    hmSpecial = 

    allPlants = 
    motherTree = 
    parasite = 
    fire = 
    electro = 
    wind = 
    ice = 
    water = 
    light = 
    dark = 
    metal = 

    botToken = 

    # Get Plant Details
    getPlantDetails = 'https://backend-farm.plantvsundead.com/get-plant-detail-v2?plantId=' + str(plantID)
    getPlantheaders = { "Authorization":"",
                        "Content-Type":"application/json", }

    r = requests.get(getPlantDetails, headers=getPlantheaders)
    
    plantType = r.json()['data']['plant']['stats']['type']
    
    rarity = r.json()['data']['plant']['rarity']
    le = r.json()['data']['plant']['farmConfig']['le']
    hr = r.json()['data']['plant']['farmConfig']['hours']
    leHR = int(le) / int(hr)
    plantImage = r.json()['data']['plant']['iconUrl']

    hp = r.json()['data']['plant']['stats']['hp']
    defPhysics = r.json()['data']['plant']['stats']['defPhysics']
    defMagic = r.json()['data']['plant']['stats']['defMagic']

    physicsDamage = r.json()['data']['plant']['stats']['damagePhysics']
    physicsMagic = r.json()['data']['plant']['stats']['damageMagic']
    physicsPure = r.json()['data']['plant']['stats']['damagePure']
    physicsHpLoss = r.json()['data']['plant']['stats']['damageHpLoss']
    physicsHpRemove = r.json()['data']['plant']['stats']['damageHpRemove']

    # seller = r.json()['data']['sellerId']

    # Discord Message
    baseURL = "https://discordapp.com/api/channels/{}/messages".format(allPlants)
    headers = { "Authorization":"Bot {}".format(botToken),
                "Content-Type":"application/json", }

    message = 'Type: {}\n\nRarity: {}\n\nLE: {} / {} Hours\n LE / Hour: {}\n\nCost: {} PVU\n\nToken ID: {}\nPlant ID: {}\n\nHP: {}\n\nPhysics Defense: {}\nMagic Defense: {}\n\nPhysic Damage: {}\nMagic Damage: {}\nPure Damage:{}\nHP Loss: {}\nHP Remove: {}\n\nMarketplace Link: {}'.format(
        str(plantType).capitalize(), 
        "Common" if rarity == 0 else "Uncommon" if rarity == 1 else "Rare" if rarity == 2 else "Mythic" if rarity == 3 else "Common", 
        le, 
        hr, 
        str(round(float(leHR),2)), 
        price/1000000000000000000, 
        tokenId, 
        plantID, 
        hp,
        defPhysics,
        defMagic,
        physicsDamage,
        physicsMagic,
        physicsPure,
        physicsHpLoss,
        physicsHpRemove,
        # seller,
        motherTreeLink if int(plantID) > 2000000000 else link)

    messagePlants = 'Type: {}\n\nRarity: {}\n\nLE: {} / {} Hours\n LE / Hour: {}\n\nCost: {} PVU\n\nToken ID: {}\nPlant ID: {}\n\nPhysic Damage: {}\nMagic Damage: {}\nPure Damage:{}\nHP Loss: {}\nHP Remove: {}\n\nMarketplace Link: {}'.format(
            str(plantType).capitalize(), 
            "Common" if rarity == 0 else "Uncommon" if rarity == 1 else "Rare" if rarity == 2 else "Mythic" if rarity == 3 else "Common", 
            le, 
            hr, 
            str(round(float(leHR),2)), 
            price/1000000000000000000, 
            tokenId, 
            plantID, 
            physicsDamage,
            physicsMagic,
            physicsPure,
            physicsHpLoss,
            physicsHpRemove,
            # seller,
            motherTreeLink if int(plantID) > 2000000000 else link)

    data =  json.dumps ( {  
                            "components": [{
                                "type": 1,
                                "components": [{
                                        "type": 2,
                                        "label": "BUY",
                                        "style": 5,
                                        "url": "http://.../Marketplace.html?tokenID={}&price={}".format(tokenId, price)
                                }]
                            }],
                            "embeds": [{
                                "title": "Incoming Money Printer 💸🍀",
                                "description": message if int(plantID) > 2000000000 else messagePlants,
                                "color": 0xffffff if plantType == "light" else 0xf41010 if plantType == "fire" else 0x7bfff8 if plantType == "ice" else 0x5ebdfc if plantType == "water" else 0xecff2f if plantType == "electro" else 0x50ff4b if plantType == "wind" else 0x5c675c if plantType == "dark" else 0xed55fc if plantType == "parasite" else 0xa7a5a5,
                                "thumbnail": { 
                                    "url": plantImage
                                }
                            }]
                        } )
    # All Plants
    response = requests.post(baseURL, headers=headers, data=data)
    print("All Plants",response)

    # # Specific Elements
    data =  json.dumps ( {  
                            "components": [{
                            "type": 1,
                            "components": [{
                                    "type": 2,
                                    "label": "BUY",
                                    "style": 5,
                                    "url": "http://.../Marketplace.html?tokenID={}&price={}".format(tokenId, price)
                            }]
                        }],
                        "embeds": [{
                            "title": "Incoming Money Printer 💸🍀",
                            "description": message if int(plantID) > 2000000000 else messagePlants,
                            "color": 0xE1DDDC if rarity == 0 else 0x7CD4FD if rarity == 1 else 0xFF675D if rarity == 2 else 0xCB55FF,
                            "thumbnail": { 
                                "url": plantImage
                            }
                        }]
                    } )

    baseURL = "https://discordapp.com/api/channels/{}/messages".format(motherTree if int(plantID) > 2000000000 else light if plantType == "light" else fire if plantType == "fire" else ice if plantType == "ice" else water if plantType == "water" else electro if plantType == "electro" else wind if plantType == "wind" else dark if plantType == "dark" else parasite if plantType == "parasite" else metal)
    response = requests.post(baseURL, headers=headers, data=data)
    print(str(plantType), response)

    if(str(plantType).capitalize() == 'Electro' and (price / 1000000000000000000) < 25 ):
        baseURL = "https://discordapp.com/api/channels/{}/messages".format(hmSpecial)
        response = requests.post(baseURL, headers=headers, data=data)
        print(str(plantType), response)


def getPlantPriceInPVU(response):
    global contract
    global func_obj, func_params, plantID
    for i, d in enumerate(response):
        try:
            contract = web3.eth.contract(address='0x5Ab19e7091dD208F352F8E727B6DCC6F8aBB6275', abi=abi['result'])
            func_obj, func_params = contract.decode_function_input(response[i]['input'])
            print(func_params)
            # if(func_params['_startingPrice']/1000000000000000000 < 40):
            plantID = contract.functions.getPlant(func_params['_tokenId']).call()[1]
            print('Token ID: ', func_params['_tokenId'], 'Plant ID:', plantID, 'Cost in PVU: ', func_params['_startingPrice']/1000000000000000000)
            sendDiscord(func_params['_tokenId'], func_params['_startingPrice'])
        except:
            pass

while True:
    getNewTransactions()