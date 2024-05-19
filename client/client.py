import http.client
import time

def get_statistics():
    conn = http.client.HTTPConnection('time-server-service.default.svc.cluster.local', 8888)
    conn.request('GET', '/statistics')
    response = conn.getresponse()
    if response.status == 200:
        statistics = response.read().decode().strip()
        return statistics
    else:
        print(f'Error: {response.status}')
    conn.close()

def write_statistics_to_file(statistics):
    with open('statistics.txt', 'a') as file:
        file.write(f'{statistics}\n')

if __name__ == '__main__':
    while True:
        statistics = get_statistics()
        if statistics:
            write_statistics_to_file(statistics)
        time.sleep(5)

