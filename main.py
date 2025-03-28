import requests

def main():
    url = 'https://hdmn.cloud/ru/demo/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if 'Ваша электронная почта' in response.text:
                email = input('\033[1;30mВведите электронную почту для получения тестового периода:\033[0m ')
                response = requests.post('https://hdmn.cloud/ru/demo/success/', data={
                    "demo_mail": f"{email}"
                })
                if 'Ваш код выслан на почту' in response.text:
                    print('📮 \033[1;32mВаш код уже в пути!\033[0m Проверьте свой почтовый ящик.')
                else:
                    print('❌ \033[1;31mУказанная почта не подходит для получения тестового периода.\033[0m')
            else:
                print('❌ \033[1;31mНе найдено нужной информации.\033[0m Попробуйте отключиться от среды выполнения и удалить ее.')
        else:
            print(f"❌ \033[1;31mОшибка при запросе к странице.\033[0m Код ответа: {response.status_code}")
    except requests.RequestException as e:
        print(f"❌ \033[1;31mОшибка при запросе к сайту:\033[0m {e}")

if __name__ == '__main__':
    main()
