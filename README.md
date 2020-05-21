# Backend web app

### Host requirements

- Python 3.6+
- Redis must be up and running (port 6379)
- rename _config.py.template_ to _config.py_ and fill-up missing values
- download and extract pretrained model [GoogleNews-vectors-negative300.bin](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)

### Installation
`$ pip install -r requirements.txt`

### Project bootstrap
`$ python manager.py db upgrade`

### Run server
`$ python manager.py`

`$ celery worker -A backend.celery --loglevel=info`

# Frontend web app

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).