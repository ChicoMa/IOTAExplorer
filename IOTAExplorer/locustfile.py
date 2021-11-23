import time
from locust import HttpUser, task, between

# users that will be simulated, 
class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def transaction(self):
        for item_id in range(10):
            self.client.get("/search/transaction/GDEKAAHYDKIAAXLXMEFEJNNKCVDSLXNNVRCXFWOYFQOJYOTNQMLGICGZPDBSBWEXWUGIGXOENVGP99999")
            time.sleep(1)
           
    @task
    def address(self):
        for item_id in range(10):
            self.client.get(f"/search/address/UDYXTZBE9GZGPM9SSQV9LTZNDLJIZMPUVVXYXFYVBLIEUHLSEWFTKZZLXYRHHWVQV9MNNX9KZC9D9UZWZ")
            time.sleep(1)

    @task 
    def bundle(self):
        for item_id in range(10):
            self.client.get("/search/bundle/NJKVGEP9FW9ERSCAVHQCDFNGI9SNGJFZCQGHCJXZBLWPZGTCLDBTXSZHEUKHHSRUCBGFPSKUX9S9OFWIA")
            time.sleep(1)

    @task
    def tag(self):
        for item_id in range(10):
            self.client.get("/search/tag/WKJZG9999999999999999999999")
            time.sleep(1)
