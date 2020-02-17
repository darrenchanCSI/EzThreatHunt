
import json
import requests

class Server:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.header = None
        self.cookie = None
        self.events = []
        
class Event:
    def __init__(self, data):
        #self.title = data['title']
        self.id = data['id']
        self.endpoint = data['endpoint']['name']
        self.triggerEvents = data['triggerEvents']
        self.triggerCondition = data['triggerCondition']
        self.triggerApps = []
        for event in self.triggerEvents:
            self.triggerApps.append(event['process']['program'])
        
class apiReply:
    def __init__(self, server, url):
        session = requests.session()
        try:
            response = session.get(server.url + url, headers = server.header, cookies = server.cookie)
            self.status_code = response.status_code
            if self.status_code == 200:
                self.json = json.loads(response.text)
                self.result = self.json['data']
                self.nextPage = self.json['nextPage']
                self.remainingItems = self.json['remainingItems']
                return
        except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:
            self.status_code == 12345
            print("Requests Exception")
        self.json = None
        self.result = None
        self.nextPage = None
        self.remainingItems = None
            
    def length(self):
        return len(self.result)
        
    def events(self):
        if self.result is not "[]":
            events = list()
            for event in self.result:
                events.append(Event(event))
            return events
        return []
    
class Settings:
    def __init__(self):
        self.playOnce = False
        self.disableWinNotifs = False
        self.disableSound = False
        self.disableConnection = False
        self.timeInterval = 30
        self.onTop = False
        self.soundFile = "./Ding.mp3"


class FilterSigner:
    def __init__(self, signer):
        self.Signer = signer
        self.Programs = []