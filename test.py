import requests

#test from GCR
# resp = requests.post("https://yolov3-flask-wx2bjo7cia-df.a.run.app", files={'file': open('data/Test_1.jpeg', 'rb')})
resp = requests.post("http://127.0.0.1:5000/", files={'file': open('data/Test_1.jpeg', 'rb')})
#test locally on image built on external drive
#resp = requests.post("http://0.0.0.0:5000", files={'file': open('../../../Documents/junkboatpic.jpg', 'rb')})

print(resp.json())