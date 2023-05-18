import dht
import machine
import network
import urequests
import utime
# Configurando o acesso a internet
WIFI_SSID = 'CLARO_2GAC95AB'
WIFI_PASSWORD = 'B8AC95AB'
# Definindo a key da api
TS_API_KEY = 'P2GUINXUBFW5BK96'
# Definindo qual é o pino em que o sensor está conectado
DHT_PIN = 4
# Inicializa o sensor
dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))
# Estabelecendo a conexão a rede wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi.isconnected():
utime.sleep(1)
print('Wi-Fi conectado:', wifi.ifconfig())
# Define o intervalo em que os dados são enviados em segundos
DELAY_SECONDS = 20
# Definindo a função que irá enviar dados para o Thingspeak
def send_data(temperature, humidity):
ts_api_url = 'https://api.thingspeak.com/update?api_key=' + TS_API_KEY +
'&field1=' + str(temperature) + '&field2=' + str(humidity)
response = urequests.get(ts_api_url)
# Confere se o os dados estão sendo enviados com sucesso
if response.status_code == 200:
print('Dados enviados com sucesso para o ThingSpeak:', ts_api_url)
else:
print('Erro ao enviar os dados para o ThingSpeak')
# Encerra a conexão
response.close()
while True:
try:
# Definindo a leitura do sensor DHT
dht_sensor.measure()
temperature = dht_sensor.temperature()
humidity = dht_sensor.humidity()
# Envia os dados para o Thingspeak
send_data(temperature, humidity)
except Exception as e:
print('Erro', e)
# Define o intervalo em que os dados são enviados em segundos
utime.sleep(DELAY_SECONDS)