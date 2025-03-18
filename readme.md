# Тестовое задание 

## Установка зависимостей
```shell
pip install -r ./requirements.txt 
```


### Пример добавления фигур.

```shell
python ./service.py add point 3 4
python ./service.py add segment 3 4 1 2
python ./service.py add circle 1 2 3
python ./service.py add square 1 2 3 4
```

### Показ фигур.

```shell
python ./service.py show
```

### Удаление фигур

```shell

python ./service.py delete point 3 4
python ./service.py delete segment 3 4 1 2
python ./service.py delete circle 1 2 3
python ./service.py delete square 1 2 3 4
```

