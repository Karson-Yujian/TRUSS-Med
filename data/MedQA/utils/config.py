import os


huggingface_embeddings_config = {
    "stella-base-en-v2": {
        "model_name": "infgrad/stella-base-en-v2",
        "model_path": "/home/sharefiles/huggingface.co/stella-base-en-v2",
        "encode_kwargs": {"normalize_embeddings": True},
        "max_len": 1024,
    },
    "stella-base-zh-v2": {
        "model_name": "infgrad/stella-base-zh-v2",
        "model_path": "/home/sharefiles/huggingface.co/stella-base-zh-v2",
        "encode_kwargs": {"normalize_embeddings": True},
        "max_len": 1024,
    }
}

