import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    @task(1)
    def index(self):
        self.client.post('/predict', params={'text':'buena onda'})
    
    @task(3)
    def predict(self):
        self.client.get('/')

    def on_start(self):
        pass
