#%%
import paho.mqtt.publish as pubish

#%%
def openfile(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    bits = []
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            l = line.rstrip()
            if l.split(',')[0] != 'id':
                bits.append(l)
    return bits
# %%
def sendToServeur(data, topic='v1/devices/me/telemetry', host='62.171.150.214', token= {'username':"sensor", 'password':"passer"}):
    pubish.single(topic, data, qos=1, hostname=host, auth = token, client_id='sensor1')

#%%
def format(data):
    return '{"date": "'+ data[1]+ '", "time": "'+data[2]+'", "temperature": '+data[3] + ', "humidite": '+data[4]+', "vibration": '+data[5]+'}'
#%%
def sendBruitData(data):
    for d in data:
        l = d.split(',')
        #print(l)
        sendToServeur(format(l))
        #print(format(l))
#%%
if __name__ == '__main__' :
    data = openfile('data.csv')
    sendBruitData(data)
# %%
