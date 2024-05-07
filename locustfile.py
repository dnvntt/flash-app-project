import time
from locust import HttpUser, task, between, tag

class WebTests1(HttpUser):
    wait_time = between(0,1)
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled.
        pass

    def on_stop(self):
        # on_stop is called when the TaskSet is stopping
        pass


    @task(1)
    def testaURL(self):
        response = self.client.post("/predict", json = {"CHAS":{ "0":0},"RM":{"0":16.3575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":326.1},"LSTAT":{"0":42.98}})
