import boto3, time

client = boto3.client(
    service_name='sqs',
    endpoint_url='https://message-queue.api.cloud.yandex.net',
    region_name='ru-central1'
)

queue_url = 'https://message-queue.api.cloud.yandex.net/.....'

x = 0
t_start = time.perf_counter()
while True:

    messages = client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10
    ).get('Messages')

    for msg in messages:
        client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=msg.get('ReceiptHandle')
        )
        x += 1
        print(f'Message {x}: ' + str(time.perf_counter() - t_start))
        t_start = time.perf_counter()