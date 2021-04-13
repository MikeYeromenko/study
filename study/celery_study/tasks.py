from study.celery import app


@app.task()
def send_email(message):
    print(message)
    return False
