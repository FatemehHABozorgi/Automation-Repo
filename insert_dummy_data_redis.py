import redis
import random
import string

def generate_random_key():
    return '98912' + ''.join(random.choices(string.digits, k=7))

def generate_random_value():
    part1 = ''.join(random.choices(string.digits, k=12))
    part2 = '4321139' + ''.join(random.choices(string.digits, k=8))
    return f"{part1}-{part2}"

def insert_dummy_data_to_redis(redis_client, num_records):
    for _ in range(num_records):
        key = generate_random_key()
        value = generate_random_value()
        redis_client.set(key, value)

def main():
    redis_client = redis.StrictRedis(host='10.10.10.10', port=6379, db=0)

    num_records = 5000000

    insert_dummy_data_to_redis(redis_client, num_records)
    print(f"Inserted {num_records} records into Redis.")

if __name__ == "__main__":
    main()
