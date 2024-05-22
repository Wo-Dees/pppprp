Чтобы запусть развертывание требуется выполнить:

```shell
./deploy.sh
```

Чтобы отправить запрос получения времени на сервер, требуется выполнить:

```shell
curl http://localhost:8888/time
```

Чтобы отправить запрос на получения статистики по обращениям, требуется выполнить:

```shell
curl http://localhost:8888/statistics
```

Чтобы убедиться, что статистика в файл сохраняется, требуется:

1. Выполнить команду, чтобы получить список подов.
```shell
kubectl get pods
```

2. Взять под с префиксом time-server и выполнить следующую команду:
```shell
kubectl exec -it [[ваше имя пода]] -- sh
```

3. Далее вы будете внутри контейнера, чтобы вывести там статистику, требуется выполнить:
```shell
cat statistics.txt
```

