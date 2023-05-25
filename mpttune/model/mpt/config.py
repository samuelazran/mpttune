class MPT7BConfig:
    name = 'mpt-7b'
    hf_config_name = "mosaicml/mpt-7b"
    hf_tokenizer_config = "EleutherAI/gpt-neox-20b"
    bits = None
    groupsize = None
    max_seq_len = 2048
    attn_impl = 'torch'
    device_map = "auto"


class MPT7BInstructConfig:
    name = 'mpt-7b-instruct'
    hf_config_name = "mosaicml/mpt-7b-instruct"
    hf_tokenizer_config = "EleutherAI/gpt-neox-20b"
    bits = None
    groupsize = None
    max_seq_len = 2048
    attn_impl = 'torch'
    device_map = "auto"


class MPT7BChatConfig:
    name = 'mpt-7b-chat'
    hf_config_name = "mosaicml/mpt-7b-chat"
    hf_tokenizer_config = "EleutherAI/gpt-neox-20b"
    bits = None
    groupsize = None
    max_seq_len = 2048
    attn_impl = 'torch'
    device_map = "auto"


class MPT7BStorywriterConfig:
    name = 'mpt-7b-storywriter'
    hf_config_name = "mosaicml/mpt-7b-storywriter"
    hf_tokenizer_config = "EleutherAI/gpt-neox-20b"
    bits = None
    groupsize = None
    max_seq_len = 5 * 2048
    attn_impl = 'torch'
    device_map = "auto"


class MPT7BStorywriter4BitConfig:
    name = 'mpt-7b-storywriter-4bit'
    hf_config_name = "OccamRazor/mpt-7b-storywriter-4bit-128g"
    hf_tokenizer_config = "EleutherAI/gpt-neox-20b"
    bits = 4
    groupsize = 128
    max_seq_len = 5 * 2048
    attn_impl = 'torch'
    device_map = "auto"
