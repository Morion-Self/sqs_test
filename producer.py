import boto3, time

client = boto3.client(
    service_name='sqs',
    endpoint_url='https://message-queue.api.cloud.yandex.net',
    region_name='ru-central1'
)

queue_url = 'https://message-queue.api.cloud.yandex.net/.....'

t_start = time.perf_counter()
for x in range(50): 
    client.send_message(
        QueueUrl=queue_url,
        MessageBody=f'Simple message {x+1}'
    )
    print(f'Message {x+1}: ' + str(time.perf_counter() - t_start))
    t_start = time.perf_counter()