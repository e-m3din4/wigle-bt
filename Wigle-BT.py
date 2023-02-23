import requests
import json

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Error: config file not found')
        return None

def get_location(netid, config):
    headers = {
        'Authorization': 'Basic ' + config['api_auth']
    }

    url = 'https://api.wigle.net/api/v2/bluetooth/search?onlymine=false&netid=' + netid
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Error: ' + response.text)
        return None

    data = response.json()

    if not data['results']:
        print('Error: no results found')
        return None

    location = (data['results'][0]['trilat'], data['results'][0]['trilong'])
    return location

def main():
    config = load_config()
    if not config:
        return

    while True:
        print('------------------------------------------------------')
        print('|                  kkNXK0OOOkkOOO0                   |') 
        print('|              kkkNXK0OOOkkOOO0KXNkkkk               |')
        print('|           dNX0OOkkkkkkkkkkkkkkkkOO0XNd             |')
        print('|         ;N0OkkkkkkkkkkdokkkkkkkkkkkkkkO0N:         |')
        print('|       ,XOkkkkkkkkkkkkkx  okkkkkkkkkkkkkkkOX;       |')
        print('|      OOkkkkkkkkkkkkkkkx    ckkkkkkkkkkkkkkkO0      |')
        print('|     XOkkkkkkkkkkkkkkkkx      :kkkkkkkkkkkkkkOX     |')
        print('|    0kkkkkkkkkkkkkkkkkkx        ;kkkkkkkkkkkkkkK    |')
        print('|   dOkkkkkkkkkkkkkkkkkkx          ,kkkkkkkkkkkkkd   |')
        print('|  .Okkkkkkkkkkkkkkkkkkkx    .o       kkkkkkkkkkkO   |')
        print('|  xkkkkkkkkkd  ;kkkkkkkx    .OKd      .kkkkkkkkkkx  |')
        print('|  Okkkkkkko      ,kkkkkx    .kkOKx      .kkkkkkkkO. |')
        print('| ;kkkkkkkkOXo       kkkx    .kkkk       NOkkkkkkkk: |')
        print('| okkkkkkkkkkOKx      .kx    .kx       N0kkkkkkkkkko |')
        print('| xkkkkkkkkkkkkOKk                  .N0kkkkkkkkkkkkx |')
        print('| kkkkkkkkkkkkkkkOKO              .N0kkkkkkkkkkkkkkk |')
        print('| OkkkkkkkkkkkkkkkkOK0           XOkkkkkkkkkkkkkkkkO |')
        print('| kkkkkkkkkkkkkkkkkkkOKx      .XOkkkkkkkkkkkkkkkkkkk |')
        print('| kkkkkkkkkkkkkkkkkkkc           kkkkkkkkkkkkkkkkkkk |')
        print('| kkkkkkkkkkkkkkkkk:               kkkkkkkkkkkkkkkkk |')
        print('| dkkkkkkkkkkkkkk;           .       xkkkkkkkkkkkkkd |')
        print('| lkkkkkkkkkkkk,      lXx    .0N.      dkkkkkkkkkkkl |')
        print('| ,kkkkkkkkkk       dKOkx    .kk0N.      dkkkkkkkkk, |')
        print('|  kkkkkkkkk      xKOkkkx    .kkkk;      cOkkkkkkkk  |')
        print('|  lkkkkkkkk0N  kKOkkkkkx    .kk       lXOkkkkkkkkl  |')
        print('|  .kkkkkkkkkk0KOkkkkkkkx    ..      dKOkkkkkkkkkk.  |')
        print('|   :kkkkkkkkkkkkkkkkkkkx          xKOkkkkkkkkkkkc   |')
        print('|    dkkkkkkkkkkkkkkkkkkx        kKOkkkkkkkkkkkkd    |')
        print('|     xkkkkkkkkkkkkkkkkkx      0KOkkkkkkkkkkkkkd     |')
        print('|      lkkkkkkkkkkkkkkkkx    KKOkkkkkkkkkkkkkkl      |')
        print('|       .kkkkkkkkkkkkkkkx  N0Okkkkkkkkkkkkkkk.       |')
        print('|          kkkkkkkkkkkkkxN0kkkkkkkkkkkkkkkk.         |')
        print('|            .kkkkkkkkkkOkkkkkkkkkkkkkkk.            |')
        print('|                  dkkkkkkkkkkkkkkd                  |')
        print('|                                                    |')
        print('|----------------------------------------------------|')
        print('|   Wigle-BT --- Bluetooth Device Trilateration Tool |')
        print('|----------------------------------------------------|')
        print('|                1. Get Device Location              |')
        print('|                2. Exit                             |')
        print('|----------------------------------------------------|')
        choice = input('        Enter choice (1/2): ')

        if choice == '1':
            netid = input('Enter Bluetooth network MAC address:')
            location = get_location(netid, config)

            if location:
                print('Location: ' + str(location))
        elif choice == '2':
            break
        else:
            print('Error: invalid choice')

if __name__ == '__main__':
    main()
