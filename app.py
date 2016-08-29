from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Welcome to New Docker test application with Jenkins CI/CD. This Application is built on Phyton and Redis cache. Visitor Count :%s .' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
