from transformers_aici import TransformersAici
import time

model_path = r'Qwen/Qwen1.5-14B-Chat-GPTQ-Int4'
tokenizers_path = model_path

model = TransformersAici(tokenizers_path, model_path, 512)

datas = [
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "请列举五个摸鱼方法，仅返回一个列表，不要有多余的解释"}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "请列举五个摸鱼方法"}
        ],
        "add_stop_char": ['<|aici_bos|>', '\n', '\n', '\n', '\n', '\n'],
        "fixed_content": ['1. ', '2. ', '3. ', '4. ', '5. ', '<|im_end|>']
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "请列举五个摸鱼方法"}
        ],
        "add_stop_char": ['<|aici_bos|>'],
        "fixed_content": ['这里是']
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "请列举五个摸鱼方法"}
        ],
        "add_stop_char": ['<|aici_bos|>', '\n', '\n', '\n', '\n'],
        "fixed_content": ['a. ', 'b. ', 'c. ', '4. ', '5. ']
    },
]

# # Speed test data
# batch_size = 1
# data = [
#     {"messages": [{"role": "user", "content": "请写一遍5000字的综述，介绍开源的搜索引擎项目"}]} for _ in range(batch_size)
# ]

start_time = time.perf_counter()
outputs = model.generate(datas)
total_token = 0
for output in zip(*outputs):
    print('--------------------------------------------------------------------------------------------------')
    print(output[0])
    print(f'output tokens: {output[1]}\n')
    total_token += output[1]
print(f'total tokens: {total_token}, {total_token / (time.perf_counter()-start_time)} token/s')
print('batch use time', time.perf_counter() - start_time)
