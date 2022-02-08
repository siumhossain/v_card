from locust import HttpUser, between, task



class ApiUser(HttpUser):
    wait_time = between(2, 5)
    def on_start(self):
        self.client.headers = {'Authorization': 'Token 95b6aa2dae9c5a6cdba6af8b44bea6f1867cf62a'}
    # @task(1)
    # def medical_data_get(self):
    #     self.client.get('/api/get_medical_record/734-72-5746/')
    @task(1)
    def medical_post(self):
        self.client.post('/api/create_medical_record/878-94-9745/',{
            'bp':'120/80',
            'major_disease':'covid-19'
        })
    